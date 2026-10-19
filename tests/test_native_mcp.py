"""验证原生 MCP 客户端的真实协议边界，不访问用户工程。"""
import importlib.util
import json
import threading
import unittest
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ENTRY = Path(__file__).resolve().parents[1] / 'skills/easyeda-mcp-setup/scripts/native_mcp.py'


def load_client():
    spec = importlib.util.spec_from_file_location('native_mcp', ENTRY)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class NativeMcpTest(unittest.TestCase):
    def test_rejects_remote_credentials_and_fragments(self):
        m = load_client()
        for endpoint in ['http://example.com/mcp', 'https://example.com/mcp',
                         'http://user:secret@127.0.0.1/mcp', 'http://127.0.0.1/mcp#fragment']:
            with self.subTest(endpoint=endpoint), self.assertRaises(ValueError):
                m.validate_endpoint(endpoint)
        self.assertEqual(m.validate_endpoint('http://127.0.0.1:31637/mcp'),
                         'http://127.0.0.1:31637/mcp')

    def test_missing_project_is_reported_without_open_or_save(self):
        m = load_client()
        calls = []

        class Handler(BaseHTTPRequestHandler):
            def log_message(self, *args):
                pass

            def do_POST(self):
                message = json.loads(self.rfile.read(int(self.headers['Content-Length'])))
                calls.append(message)
                method = message['method']
                if method == 'initialize':
                    value = {'protocolVersion': '2025-06-18', 'capabilities': {'tools': {}},
                             'serverInfo': {'name': 'JLCEDA Pro', 'version': 'fixture'}}
                elif method == 'tools/list':
                    value = {'tools': [{'name': 'LCEDA-Pro.' + n} for n in ['help', 'discover', 'call']]}
                else:
                    args = message['params']['arguments']
                    if message['params']['name'].endswith('.help'):
                        data = {'children': []}
                    elif args['path'] == 'session.list':
                        data = {'ok': True, 'data': [{'sessionId': 's1', 'status': 'alive'}]}
                    elif args['path'] == 'invoke':
                        data = {'ok': True, 'data': {'project': None, 'currentDocument': None}}
                    else:
                        raise AssertionError('unexpected operation: ' + args['path'])
                    value = {'isError': False, 'content': [{'type': 'text', 'text': json.dumps(data)}]}
                encoded = json.dumps({'jsonrpc': '2.0', 'id': message['id'], 'result': value}).encode()
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Content-Length', str(len(encoded)))
                self.end_headers()
                self.wfile.write(encoded)

        server = ThreadingHTTPServer(('127.0.0.1', 0), Handler)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        try:
            client = m.NativeMcp('http://127.0.0.1:%d/mcp' % server.server_port)
            result = client.current_project()
            self.assertEqual(result['status'], 'no_project')
            tool_calls = [c for c in calls if c['method'] == 'tools/call']
            self.assertTrue(tool_calls[0]['params']['name'].endswith('.help'))
            operations = [c['params']['arguments'].get('path') for c in tool_calls]
            self.assertNotIn('open', operations)
            self.assertNotIn('stop', operations)
            source = next(c['params']['arguments']['input']['code'] for c in tool_calls
                          if c['params']['name'].endswith('.call')
                          and c['params']['arguments'].get('path') == 'invoke')
            self.assertNotIn('.save(', source)
            self.assertNotIn('.create', source)
        finally:
            server.shutdown()
            server.server_close()

    def test_nested_native_failure_is_not_success(self):
        m = load_client()
        with self.assertRaises(m.McpError):
            m.unwrap({'isError': False, 'content': [{'type': 'text',
                     'text': '{"ok":false,"error":{"message":"DRC failed"}}'}]})

    def test_ambiguous_sessions_require_selection(self):
        m = load_client()
        client = object.__new__(m.NativeMcp)
        client.call = lambda path, data=None: [
            {'sessionId': 'a', 'status': 'alive'}, {'sessionId': 'b', 'status': 'alive'}]
        with self.assertRaises(m.McpError):
            client.current_project()


if __name__ == '__main__':
    unittest.main()

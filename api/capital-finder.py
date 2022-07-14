from http.server import BaseHTTPRequestHandler
from datetime import datetime

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        #initial deployment
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        message = "Hello World! how are you"
        self.wfile.write(message.encode())
        return

        # s = self.path
        # url_components = parse.urlsplit(s)
        # query_string_list = parse.parse.qsl(url_components.query)
        # dic = dict(query_string_list)
        # name = dic.get("name")
        # message = ""
        # if name:
        #     message = f"Aloha {name}"
        # else:
        #     message = "Aloha stranger"
        #
        # message += f"\nGreetings from Python version {platform.python_version()}"
        #
        # self.send_response(200)
        # self.send_header('Content-type', 'text/plain')
        # self.end_headers()
        # self.wfile.write(message.encode())
        # return
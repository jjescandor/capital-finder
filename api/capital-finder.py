from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests


class handler(BaseHTTPRequestHandler):
    # http://localhost:3000/api/define?word=python
    def do_GET(self):
        s = self.path
        url_components = parse.urlsplit(s)
        query_string_list = parse.parse_qsl(url_components.query)
        dic = dict(query_string_list)

        if "country" in dic:
            url = "https://restcountries.com/v3.1/name/"
            # r = requests.get(url + dic["country"])
            r = requests.get(url)
            data = r.json()
            # definitions = []
            # for word_data in data:
            #     definition = word_data["meanings"][0]["definitions"][0]["definition"]
            #     definitions.append(definition)
            # message = str(definitions)
            message = data[0]
            print("hi")
            print(message)

        else:
            message = "Give me a country to search please"

        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()

        self.wfile.write(message.encode())

        return
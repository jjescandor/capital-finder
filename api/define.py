

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

        if "word" in dic:
            url = "https://api.dictionaryapi.dev/api/v2/entries/en/"
            r = requests.get(url + dic["word"])
            data = r.json()
            definitions = []
            for word_data in data:
                definition = word_data["meanings"][0]["definitions"][0]["definition"]
                definitions.append(definition)
            message = data
            url1 = "https://restcountries.com/v3.1/name/peru"
            r1 = requests.get(url1)
            data1 = r.json()
            message = data1[0]["name"]

        else:
            message = "Give me a word to define please 1"

        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()

        self.wfile.write(message.encode())

        return
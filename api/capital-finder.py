

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
            r = requests.get(url + dic["country"])
            data = r.json()
            message = f'The capital of {dic["country"].upper()} is {str(data[0]["capital"][0].upper())} city'
        elif "capital" in dic:
            url = "https://restcountries.com/v2/capital/"
            r = requests.get(url + dic["capital"])
            data = r.json()
            message = f'The city of {dic["capital"].upper()} is in country {str(data[0]["name"].upper())}'
        else:
            message = "Give me a country or a city to search please! :)"
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

        self.wfile.write(message.encode())

        return

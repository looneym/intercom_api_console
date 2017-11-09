import requests 
import json

class BaseHttpClient:

    def __init__(self, api_base, access_token):
        self.api_base = api_base 
        self.headers = {
            'Authorization': 'Bearer {}'.format(access_token),
            'Accept': 'application/json',
            'Content-Type' : 'application/json'
            }

    def print_status(self, r):
        print "Request completed with status code: {}".format(r.status_code)

    def post(self, url, data):
        r = requests.post(self.api_base + url, headers=self.headers, data=json.dumps(data))
        self.print_status(r)
        return json.loads(r.text)

    def get(self, url):
        r = requests.get(self.api_base + url, headers=self.headers)
        self.print_status(r)
        return json.loads(r.text)

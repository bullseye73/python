import requests, json
from urllib.error import HTTPError

class RsRequest :
    def __init__(self, mHost, mPort):
        self.host = mHost
        self.port = mPort

    def send (self, path, data, headers):
        try :
            url = self.host +':' + str(self.port) + '/' + path
            req = requests.post(url, data=json.dumps(data), headers=headers)
            jsonData = json.loads(req.text)
            return jsonData
        except HTTPError as e:
            print(e)
            return 

import requests, json
from urllib.error import HTTPError
from datetime import datetime

url = 'http://192.168.219.129:8080' 
headers = {'Content-Type': 'application/json; charset=utf-8'}
params = {
    "user_id":"claude",
    "msg":"안녕",
    "timezone":"seoul",
    "platform":"Windows10 PC",
    "msg_id":"testid"
}

def getTime () :
    s = datetime.now().strftime('[%Y-%m-%d %H:%M:%S] : ')
    return s

if __name__ == '__main__':
    try:
        print(getTime() + 'Start')
        req = requests.post(url, data=json.dumps(params), headers=headers)
        jsonData = json.loads(req.text)
        
        print(req.text)
        # Dictionary 데이타 체크
        print(getTime() + jsonData['msg_id'])
        for h in jsonData['utterances']:
            print(h['text'])

        '''print(req.url)'''
        '''print(req.text)'''
    except HTTPError as e:
        print(e)

#!/usr/bin/python3
# encoding=utf8

from datetime import datetime
#import sys
import requests, json
from urllib.error import HTTPError

#reload(sys)
#sys.setdefaultencoding('utf8')

url = 'http://192.168.219.129:8080'
headers = {'Content-Type': 'application/json; charset=utf-8'}
params = {
    "user_id":"claude",
    "msg":"국민청원",
}
print("content-type:text/html; charset=UTF-8\n")

def getTime () :
    s = datetime.now().strftime('[%Y-%m-%d %H:%M:%S] : ')
    return s

def printHtml(_time, body):
    print ( '''
        <!doctype html>
            <html>
                <head>
                    <title>WEB1 - Welcome</title>
                    <meta charset="utf-8">
                </head>
                <body>
                    {_time}{body}<br/>
                                        
                </body>
            </html>
            '''.format(_time=_time,body=body))
    
if __name__ == '__main__':
    try:
        req = requests.post(url, data=json.dumps(params), headers=headers)
        req.encoding = 'euc-kr'
        jsonData = json.loads(req.text)
        bodyData = []
        #printHtml(getTime(), jsonData['utterances'].text)
        bodyData.append(jsonData['msg_id'])
        bodyData.append(jsonData['utterances'][0]['text'])
        printHtml(getTime(),bodyData)

    except HTTPError as e:
        print(e)

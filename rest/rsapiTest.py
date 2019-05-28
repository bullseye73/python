import commTime
import rsapi

url = 'http://192.168.219.129'
prt = 8080
headers = {'Content-Type': 'application/json; charset=utf-8'}
params = {
    "user_id":"claude",
    "msg":"안녕",
    "timezone":"seoul",
    "platform":"Windows10 PC",
    "msg_id":"testid"
}

if __name__ == '__main__':
    commTime.cp(__name__ + ' Start')
    rapi = rsapi.RsRequest(url, prt)
    res = rapi.send('', params, headers)
    if res != None :
        commTime.cp(res['msg_id'])
        for h in res['utterances']:
            commTime.cp(h['text'])

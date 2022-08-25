import json

def readJson(_fileName):
    with open(_fileName) as json_file:
        json_data = json.load(json_file)
    return json_data

def writeJson(_fileName, _data):
    #app_json = json.dumps(_data)
    with open(_fileName, "w", encoding="utf-8") as file :
        json.dump(_data, file, indent="\t", ensure_ascii=False)
    return

def dic2Json(_dict):
    json_val = json.dumps(_dict)
    print("json_val = %s"% json_val)
    print("json_val type = %s"% type(json_val))
    return json_val

def json2Dic(_jsondata):
    dicData = json.loads(_jsondata)
    print("dicData = %s"% dicData)
    print("dicData type= %s"% type(dicData))
    return dicData

def main():
    jsonData = readJson("/Users/chang-hunjeong/workspace/python/example/dic2Json/test.json")
    print("jsonData = %s"% jsonData)
    print("jsonData type= %s"% type(jsonData))
    json2Dic(jsonData)
    #jsonData = dic2Json(DICT)
    #writeJson("./test.json", jsonData)
    pass

if __name__ == '__main__':
    main()
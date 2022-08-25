import json

DICT = {
        "name":"song", 
        "age" : 10
    }

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

def main():
    print("dict = %s"% DICT)
    print("dict type= %s"% type(DICT))
    jsonData = dic2Json(DICT)
    writeJson("./test.json", jsonData)
    pass

if __name__ == '__main__':
    main()
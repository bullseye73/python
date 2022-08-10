#
import os.path, sys
import json
data = {
    "name" : "Tyler",
    "gender" : "male",
    "age" : "28",
    "hobby" : ["dev", "그림 그리기"]
}
JSON_FILE = "./test.json"

def writeJson(_fileName):
    with open(_fileName, "w", encoding="utf-8") as file :
        json.dump(data, file, indent="\t", ensure_ascii=False)
    return

def usage():
    print ("Usage: input full path with filename \n[ex. /path/filename.json]")
    
def usage_ex(_filePath):
    print ("Usage: input full path with filename \n[{}]".format(_filePath))
    
def main():
    jsData = writeJson(JSON_FILE)

if __name__ == '__main__':
    main()

#
import os.path, sys
import json

def readJson(_fileName):
    with open(_fileName) as json_file:
        json_data = json.load(json_file)
    return json_data

def usage():
    print ("Usage: input full path with filename \n[ex. /path/filename.json]")
    
def usage_ex(_filePath):
    print ("Usage: input full path with filename \n[{}]".format(_filePath))
    
def main(_fileName):
    #fname, ext = os.path.splitext(_fileName)
    #print("fname:{}, ext:{}".format(fname, ext))
    jsData = readJson(_fileName)
    print(jsData)
    print(jsData["DEFAULT"])
    print(jsData["DEFAULT"]["ADMIN_NAME"])
    print(jsData["DEFAULT"]["SECRET_KEY"])
    print(jsData["TEST"])
    print(jsData["CI"])

if __name__ == '__main__':
    if len(sys.argv) != 2:
        usage()       
        sys.exit()
    if os.path.isfile(sys.argv[1]) :
        main(sys.argv[1])
    else :
        usage_ex(sys.argv[1])
        sys.exit()

    


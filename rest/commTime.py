from datetime import datetime

def getTime () :
    s = datetime.now().strftime('[%Y-%m-%d %H:%M:%S.%f] : ')
    return s

def cp(log) :
    print(str(getTime()) + str(log))
    #print(log )
    
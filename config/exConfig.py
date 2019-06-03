import configparser

class exConfig:
    def __init__(self, filename):
        config = configparser.ConfigParser()
        config.read(filename)

    def getSessionList(self):
        return
    def getSessionData(self, sname):
        return

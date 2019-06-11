from backports import configparser

class exConfig(object):
    def __init__(self, filename):
        self.filename = filename
        self.config = configparser.ConfigParser()
        self.config.read(self.filename)

    def getSectionList(self):
        return self.config.sections()

    def getSectionlength(self, sname):
        nlen = len(self.config[sname])
        return nlen

    def getSectionData(self, sname, idx):
        return self.config[sname][idx]

    def getDefaultData(self):
        return self.config.defaults()

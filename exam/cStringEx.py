from OCR.libs import cStringUtil
from random import randint

class cStringEx(cStringUtil.cStringUtil):
    colorList = {
        'white': "\x1b[37m",
        'yellow': "\x1b[33m",
        'green': "\x1b[32m",
        'blue': "\x1b[34m",
        'cyan': "\x1b[36m",
        'red': "\x1b[31m",
        'magenta': "\x1b[35m",
        'black': "\x1b[2m",

        'darkwhite': "\x1b[39m",
        'darkblack': "\x1b[30m",

        'BgBlack' : "\x1b[40m",
        'BgRed' : "\x1b[41m",
        'BgGreen' : "\x1b[42m",
        'BgYellow' : "\x1b[43m",
        'BgBlue' : "\x1b[44m",
        'BgMagenta' : "\x1b[45m",
        'BgCyan' : "\x1b[46m",
        'BgWhite' : "\x1b[47m",
        'off': "\x1b[0m"
    }

    def func1(self):
        print("func 1")

    def cprint(self, data, color='red'):
        color = self.colorList.keys()[randint(0, len(self.colorList)-1)] if color == 'rand' else color
        try:
            print ('%s%s%s' % (self.colorList[color], data, self.colorList['off']))
        except KeyError:
            print ('[-] Not exist color \'%s\'' % color)
            print ('===== sample =====')
            print('\'%s\'' % self.colorList)


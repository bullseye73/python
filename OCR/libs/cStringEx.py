#
# sample : https://pypi.org/project/colorama/
# ansicolor : https://github.com/shiena/ansicolor/blob/master/README.md
# Copyright Jonathan Hartley 2013. BSD 3-Clause license; see LICENSE file.
#
from OCR.libs import cStringUtil
from random import randint

class cStringEx(cStringUtil.cStringUtil):
    colorList = {
        'Dim': "\x1b[2m",
        'Underscore': "\x1b[4m",
        'Blink': "\x1b[5m",
        'Reverse': "\x1b[7m",

        'white': "\x1b[37m",
        'black': "\x1b[2m",
        'darkwhite': "\x1b[39m",
        'darkblack': "\x1b[30m",

        'yellow': "\x1b[93;1m",   # bold체 "\x1b[93;1m"
        'green': "\x1b[92m",
        'blue': "\x1b[94m",
        'cyan': "\x1b[96m",
        'red': "\x1b[91m",
        'magenta': "\x1b[95m",

        'darkyellow': "\x1b[33m",
        'darkgreen': "\x1b[32m",
        'darkblue': "\x1b[34m",
        'darkcyan': "\x1b[36m",
        'darkred': "\x1b[31m",
        'darkmagenta': "\x1b[35m",

        'BgBlack' : "\x1b[49m",
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


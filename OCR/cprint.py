from random import randint
from sys import platform

#if platform.startswith('win'):
#    from colorama import init
#    init()
 
colorList = {
'white':    "\x1b[39m",
'yellow':   "\x1b[33m",
'green':    "\x1b[32m",
'blue':     "\x1b[34m",
'cyan':     "\x1b[36m",
'red':      "\x1b[31m",
'magenta':  "\x1b[35m",
'black':      "\x1b[2m",
'darkwhite':  "\x1b[37m",
'darkyellow': "\x1b[33m",
'darkgreen':  "\x1b[32m",
'darkblue':   "\x1b[34m",
'darkcyan':   "\x1b[36m",
'darkred':    "\x1b[31m",
'darkmagenta':"\x1b[35m",
'darkblack':  "\x1b[30m",
'off':        "\x1b[0m"
}
 
 
def cprint(data, color='white'):
    color = colorList.keys()[randint(0, len(colorList)-1)] if color == 'rand' else color
    try:
        print ('%s%s%s' % (colorList[color], data, colorList['off']))
    except KeyError:
        print ('[-] Not exist color \'%s\'' % color)
        print ('===== sample =====')
        color_sample()
 
def craw_input(data, color='white'):
    color = colorList.keys()[randint(0, len(colorList)-1)] if color == 'rand' else color
    try:
        return raw_input('%s%s%s' % (colorList[color], data, colorList['off']))
    except KeyError:
        print ('[-] Not exist color \'%s\'' % color)
        print ('===== sample =====')
        color_sample()
         
def color_sample():
    for color in colorList:
        cprint(color, color)

def main():
    cprint("test 입니다.", 'cyan')
    
if __name__=='__main__': 
     main()
COLORS = dict(zip(range(1, 10), 'black red green yellow blue magenta'
                  ' cyan white reset'.split()))


class BG:
    black = '\033[40m'
    red = '\033[41m'
    green = '\033[42m'
    yellow = '\033[43m'
    blue = '\033[44m'
    magenta = '\033[45m'
    cyan = '\033[46m'
    white = '\033[47m'
    reset = '\033[49m'


class FG:
    black = '\033[30m'
    red = '\033[31m'
    green = '\033[32m'
    yellow = '\033[33m'
    blue = '\033[34m'
    magenta = '\033[35m'
    cyan = '\033[36m'
    white = '\033[37m'
    reset = '\033[39m'


class BRIGHT:
    bright = '\033[1m'
    dim = '\033[2m'
    normal = '\033[22m'


class Color:
    resetall = '\033[0m'

    @classmethod
    def colored(self, msg, foreground='white', background='black', bright=0):
        xBRIGHT, xBG, xFG = '', '', ''
        if bright is 1:
            xBRIGHT = BRIGHT.bright
        elif bright is 2:
            xBRIGHT = BRIGHT.dim
        else:
            xBRIGHT = BRIGHT.normal
        if hasattr(BG, background):
            xBG = getattr(BG, background)
        if hasattr(FG, foreground):
            xFG = getattr(FG, foreground)
        return '{}{}{}{}{}'.format(
                xBRIGHT, xBG, xFG, msg, Color.resetall)


if __name__ == '__main__':
    #msg = input('>>> ')
    msg = ' Hello world!'
    colors = list(COLORS.values())
    for i in range(0, len(colors), 3):
        for fg in colors:
            line = ' '.join([''.join(Color.colored(msg, fg, colors[i+x], y)
                             for y in (1, 2, 0))
                            for x in range(3)])
            print(line)
        print()
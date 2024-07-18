RESET = '\x1b[0m'
CSI = '\x1b['

BLACK = 0
RED = 1
GREEN = 2
YELLOW = 3
BLUE = 4
MAGENTA = 5
CYAN = 6
WHITE = 7


class Color:
    black = '0'
    red = '1'
    green = '2'
    yellow = '3'
    blue = '4'
    magenta = '5'
    cyan = '6'
    white = '7'


class Style:
    bold = ';1m'


class Layer:
    fore = '3'
    back = '4'


def set_style(color: Color=Color.white, style: Style=None, layer: Layer=Layer.fore):
    result = f'{CSI+layer+color}m'
    if style:
        result = result[:-1] + style

    if color == RESET:
        print(RESET, end='')
        return

    print(result, end='')

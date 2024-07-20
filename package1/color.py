import enum


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


class Color(enum.Enum):
    reset = '\x1b[0m'
    black = '0'
    red = '1'
    green = '2'
    yellow = '3'
    blue = '4'
    magenta = '5'
    cyan = '6'
    white = '7'


class Style(enum.Enum):
    bold = ';1m'
    normal = ''


class Layer(enum.Enum):
    fore = '3'
    back = '4'


def get_style(color: Color = Color.white, style: Style = Style.normal,
              layer: Layer = Layer.fore) -> str:
    if color == Color.reset:
        return Color.reset.value

    result = f'{CSI + layer.value + color.value}m'
    if style.value:
        result = result[:-1] + style.value

    return result


def set_style(color: Color = Color.white, style: Style = Style.normal,
              layer: Layer = Layer.fore) -> None:
    if color == Color.reset:
        print(Color.reset.value, end='')
        return

    result = f'{CSI + layer.value + color.value}m'
    if style.value:
        result = result[:-1] + style.value

    print(result, end='')

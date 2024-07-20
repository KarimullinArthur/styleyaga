import functools

from package1 import *
from package1.color import *


def set_link(link):
    def decorator(func):
        @functools.wraps(func)
        def wrapper():
            label = func()
            return create_link(link, label)
        return wrapper
    return decorator


@set_link(link='https://google.com')
def get_google() -> str:
    googles_colors = (Color.blue, Color.red, Color.yellow,
                      Color.blue, Color.green, Color.red)
    google = list(map(lambda x, y: {x: y}, 'Google', googles_colors))

    result = []
    for _dict in google:
        char = tuple(_dict.items())[0][0]
        color = tuple(_dict.items())[0][1]
        style = get_style(color=color)
        result.append(char + style)

    return ''.join(result)


def main():
    set_style(color=Color.red)
    print(create_link("https://ya.ru", "Yandex"))

    print(get_google())

    set_style(color=Color.magenta, style=Style.bold)
    print(create_link("https://yahoo.com", "Yahoo"))

    set_style(color=Color.white, layer=Layer.back)
    set_style(color=Color.black, layer=Layer.fore)
    print(create_link("https://wikipedia.org", "Wikipedia"))

    set_style(color=Color.reset)


if __name__ == '__main__':
    main()

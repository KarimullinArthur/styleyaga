from package1 import *
from package1.color import *



def main():
    set_style(color=Color.red)
    print(create_link("https://ya.ru", "Yandex"))

    googles_colors = (Color.blue, Color.red, Color.yellow,
                     Color.blue, Color.green, Color.red)
    google = list(map(lambda x, y: {x: y}, 'Google', googles_colors))

    for _dict in google:
        char = tuple(_dict.items())[0][0]
        color = tuple(_dict.items())[0][1]
        set_style(color=color)
        print(char, end='')
#        print(create_link("https://google.com", "Google"))

    print()
    set_style(color=Color.magenta, style=Style.bold)
    print(create_link("https://yahoo.com", "Yahoo"))
    set_style(color=RESET)



if __name__ == '__main__':
    main()

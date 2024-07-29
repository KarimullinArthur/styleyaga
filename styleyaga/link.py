import functools


def create_link(uri: str, label=None) -> str:
    if label is None:
        label = uri

    parameters = ""

    # OSC 8 ; params ; URI ST <name> OSC 8 ;; ST
    escape_mask = "\033]8;{};{}\033\\{}\033]8;;\033\\"

    return escape_mask.format(parameters, uri, label)


def set_link(link: str):
    def decorator(func):
        @functools.wraps(func)
        def wrapper():
            label = func()
            return create_link(link, label)

        return wrapper

    return decorator

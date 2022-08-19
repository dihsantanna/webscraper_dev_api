from colorama import Fore, Style, init

init()


def print_color(text, color):
    print(getattr(Fore, color) + text + Style.RESET_ALL)

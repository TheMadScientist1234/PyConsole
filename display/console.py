import colorama
from enum import Enum

# Colors that can be printed to the console
class ConsoleColor(Enum):
    BLACK = 1
    RED = 2
    GREEN = 3
    BLUE = 4
    YELLOW = 5
    MAGENTA = 6
    CYAN = 7
    WHITE = 8
    DARK_RED = 9
    DARK_GREEN = 10
    DARK_BLUE = 11
    DARK_YELLOW = 12
    DARK_MAGENTA = 13
    DARK_CYAN = 14
    DARK_WHITE = 15
    BRIGHT_RED = 16
    BRIGHT_GREEN = 17
    BRIGHT_BLUE = 18
    BRIGHT_YELLOW = 19
    BRIGHT_MAGENTA = 20
    BRIGHT_CYAN = 21

class Console:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def cprint(self, text: str, color=ConsoleColor.WHITE, newline=True):
        # Clear the style
        print(colorama.Style.RESET_ALL, end='')

        # Determine colorama style tags
        color_switch = {
            ConsoleColor.BLACK: colorama.Fore.BLACK,
            ConsoleColor.RED: colorama.Fore.RED,
            ConsoleColor.GREEN: colorama.Fore.GREEN,
            ConsoleColor.BLUE: colorama.Fore.BLUE,
            ConsoleColor.YELLOW: colorama.Fore.YELLOW,
            ConsoleColor.MAGENTA: colorama.Fore.MAGENTA,
            ConsoleColor.CYAN: colorama.Fore.CYAN,
            ConsoleColor.WHITE: colorama.Fore.WHITE,
            ConsoleColor.DARK_RED: colorama.Style.DIM + colorama.Fore.RED,
            ConsoleColor.DARK_GREEN: colorama.Style.DIM + colorama.Fore.GREEN,
            ConsoleColor.DARK_BLUE: colorama.Style.DIM + colorama.Fore.BLUE,
            ConsoleColor.DARK_YELLOW: colorama.Style.DIM + colorama.Fore.YELLOW,
            ConsoleColor.DARK_MAGENTA: colorama.Style.DIM + colorama.Fore.MAGENTA,
            ConsoleColor.DARK_CYAN: colorama.Style.DIM + colorama.Fore.CYAN,
            ConsoleColor.DARK_WHITE: colorama.Style.DIM + colorama.Fore.WHITE,
            ConsoleColor.BRIGHT_RED: colorama.Style.BRIGHT + colorama.Fore.RED,
            ConsoleColor.BRIGHT_GREEN: colorama.Style.BRIGHT + colorama.Fore.GREEN,
            ConsoleColor.BRIGHT_BLUE: colorama.Style.BRIGHT + colorama.Fore.BLUE,
            ConsoleColor.BRIGHT_YELLOW: colorama.Style.BRIGHT + colorama.Fore.YELLOW,
            ConsoleColor.BRIGHT_MAGENTA: colorama.Style.BRIGHT + colorama.Fore.MAGENTA,
            ConsoleColor.BRIGHT_CYAN: colorama.Style.BRIGHT + colorama.Fore.CYAN
        }
        if newline:
            print(color_switch[color] + text)
        else:
            print(color_switch[color] + text, end='')

    def clear(self):
        for i in range(self.height):
            print(colorama.Style.RESET_ALL)

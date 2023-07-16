import colorama
from colorama import Fore

class CustomNotifs:
    @staticmethod
    def message(title_fore, title, description):
        if title_fore == 1:
            title_fore = Fore.RED
        elif title_fore == 2:
            title_fore = Fore.GREEN
        elif title_fore == 3:
            title_fore = Fore.YELLOW
        elif title_fore == 4:
            title_fore = Fore.BLUE
        elif title_fore == 5:
            title_fore = Fore.MAGENTA
        elif title_fore == 6:
            title_fore = Fore.WHITE
        print(f"{title_fore}{title}{Fore.RESET}: {description}")
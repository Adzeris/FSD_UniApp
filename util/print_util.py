
class PrintUtil:

    @staticmethod
    def print_red(content):
        red = '\033[91m'
        reset = '\033[0m'
        print(f"{red}{content}{reset}")

    @staticmethod
    def print_white(content):
        white = '\033[97m'  # White text
        reset = '\033[0m'
        print(f"{white}{content}{reset}")

    @staticmethod
    def print_green(content):
        green = '\033[92m'  # White text
        reset = '\033[0m'
        print(f"{green}{content}{reset}")

    @staticmethod
    def print_yellow(content):
        yellow = '\033[93m'  # White text
        reset = '\033[0m'
        print(f"{yellow}{content}{reset}")

    @staticmethod
    def print_blue(content):
        blue = '\033[94m'  # White text
        reset = '\033[0m'
        print(f"{blue}{content}{reset}")

    @staticmethod
    def input_cyan(content):
        light_blue = '\033[96m'  # ANSI escape code for light blue/cyan
        reset = '\033[0m'  # Reset to default color
        return input(f"{light_blue}{content}{reset}")

import os

def clear(lines = 0):
    clear_lines=f'\033[{lines}A'
    
    if lines > 0:
        print(clear_lines)
        print('\033[J')
    else:
        # for windows
        if os.name == 'nt':
            _ = os.system('cls')
    
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = os.system('clear')

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def print_c(string,color):
    print(f"{color}{string}{bcolors.ENDC}")
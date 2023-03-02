import os
from datetime import datetime
import console
import login

class Controller:
    def __init__(self):
        self.init = True
        self.init_time = datetime.now()


    def title_ascii_art(self):
        print(r"""
 ______   ______     ______  
/\__  _\ /\  __ \   /\__  _\ 
\/_/\ \/ \ \ \/\ \  \/_/\ \/ 
   \ \_\  \ \_____\    \ \_\ 
    \/_/   \/_____/     \/_/ 
        
    -[ Tasks on Timer ]-
            
        """)

    def print_title(self):
        console.clear()
        self.print_time()
        self.title_ascii_art()
        
    def print_time(self):
        time = datetime.now()
        formatted_time = time.strftime("%Y-%m-%d %H:%M:%S")
        print(formatted_time)

    def print_menu(self, title, options):
        options_string = ''

        for option in options:
            options_string += f'[{options[option]}] {option}    '

        print(f'----- {title} ' + '-'*(len(options_string) - len(title) - 6))
        print(options_string)
        print('-'*len(options_string)+'\n',end="")

    def menu_main(self):
        menu_options = {
            "New Task":"N",
            "Select Task":"A",
            "Options":"O"
        }

        self.print_menu("Main Menu", menu_options)
        print("\nChoose an option:", end="")

        selection = False

        while selection == False:
            char = input('\n').upper()
            for option in menu_options:
                if menu_options[option] == char:
                    selection = True
            if not selection:
                console.clear(4)
                console.print_c("Not a valid option, try again:\033[A",console.bcolors().WARNING)
        
    def run(self):
        self.print_title()
        login.run()
        self.menu_main()
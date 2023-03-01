from os import system, name
import getpass
from datetime import datetime
   
def clear(lines = 0):
    clear_lines=f'\033[{lines}A'
    
    if lines > 0:
        print(clear_lines)
        print('\033[J')
    else:
        # for windows
        if name == 'nt':
            _ = system('cls')
    
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')
        
def title_ascii_art():
    print(r"""
 ______   ______     ______  
/\__  _\ /\  __ \   /\__  _\ 
\/_/\ \/ \ \ \/\ \  \/_/\ \/ 
   \ \_\  \ \_____\    \ \_\ 
    \/_/   \/_____/     \/_/ 
    
     -[ Tasks on Timer ]-
        
    """)
    
def print_title():
    clear()
    print_time()
    title_ascii_art()
    
def print_time():
    time = datetime.now()

    formatted_time = time.strftime("%Y-%m-%d %H:%M:%S")
    print(formatted_time)
    
def user_login(guest):
    username = 'guest'
    password = ''
    
    clear(2)

    if not guest:
        print('Enter Credentials')
        
        username = input("Username: ")
        try:
            password = getpass.getpass()
            print()
        except Exception as error:
            print('ERROR', error)
    
    if user_auth(username,password):
        clear(9)
        print(f'{username}')
        return True
    else:
        print(f'Login attempt failed')
        return False
            
def user_auth(username,password):
    if username:
        return True
    
def login():
    login_option = input('[ENTER] to Login' +
          ' | [G] Continue as Guest\n')
    
    if login_option == '':
        user_login(False)
    elif login_option.upper() == 'G':
        user_login(True)
    
def menu():
    print(' [N] New Tasks')
    
def main():
    print_title()
    login()

if __name__ == "__main__":
    main()

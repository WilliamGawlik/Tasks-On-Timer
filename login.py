import console
import getpass

def user_login(guest):
    username = 'guest'
    password = ''
    
    console.clear(2)

    if not guest:
        print('Enter Credentials')
        username = input("Username: ")
        try:
            password = getpass.getpass()
            print()
            console.clear(9)
            
        except Exception as error:
            print('ERROR', error)
    else:
        console.clear(6)
        
    if user_auth(username,password):
        console.print_c(f'[{username}]',console.bcolors.HEADER)
        return True
    else:
        print(f'Login attempt failed')
        return False
            
def user_auth(username,password):
    if username:
        return True
    
def run():
    login_option = input('[ENTER] to Login' +
          ' | [G] Continue as Guest\n')
    
    if login_option == '':
        user_login(False)
    elif login_option.upper() == 'G':
        user_login(True)

    print()
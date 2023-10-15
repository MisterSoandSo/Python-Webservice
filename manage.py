import getpass
import sys

from backend import UserManagement

arguments = sys.argv
conn = UserManagement('user.db')

def userMenu():
    print("~~~~~ Profile ~~~~~")
    print("1. Change Username")
    print("2. Change Password")
    print("3. Delete User")
    print("4. Exit")

def mainMenu():
    print("~~~~~ User Manager System ~~~~~")
    print("1. Register User")
    print("2. List User")
    print("3. Modify User")
    print("4. Exit")

def option1():
    user = input("Enter your Username: ")
    password = getpass.getpass("Enter your password: ")
    if conn.register_user(user, password):
        print(f"Credentials of {user} saved in the database")
    else:
        print(f"Username {user} already exists")

def option2():
    print(conn.list_users())

def option3():
    print("Which user to modify? :")
    option2()
    user = input("Select by id: ")
    userMenu()
    conn.remove_user(user)

def main():
    menu_options = {
        '1': option1,
        '2': option2,
        '3': option3,
        '4': exit
    }
    
    if len(arguments) > 1:
        if arguments[1] in menu_options:
            menu_options[arguments[1]]()
    else:
        while True:
            mainMenu()
            choice = input("Select >> ")
            if choice in menu_options:
                menu_options[choice]()
            else:
                print("Invalid Input")

if __name__ == '__main__':
    main()

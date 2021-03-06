#!/usr/bin/env python3.6
import random
import string

from locker import User
from locker import Credentials

def create_user(tname,tusername,tpassword):
    '''
    Function to create a new user
    '''
    new_user=User(tname,tusername,tpassword)
    return new_user

def save_users(user):
    '''
    Function to save users
    '''
    user.save_user()

def del_user(user):
    '''
    Function to delete a user
    '''
    user.del_user()

def find_user(tname):
    '''
    Function tha finds a contact by the twitter name and returns the user
    '''
    return User.find_by_tname(tname)

def check_existing_user(tname):
    '''
    Function that checks if a user exists with the tname
    '''
    return User.user_exist(tname)

def display_users():
    '''
    Function that returns all the saved users
    '''
    return User.display_users()

def copy_tusername(cls,tname):
    '''
    Function to copy data on the clipboard
    '''
    user_found = User.find_by_tname(tname)
    pyperclip.copy(user_found.tusername)



def create_credentials(media,username,password):
    '''
    Function to create a new credential
    '''
    new_credentials=Credentials(media,username,password)
    return new_credentials

def save_credentials(credentials):
    '''
    Function to save credentials
    '''
    credentials.save_credentials()

def del_credentials(credentials):
    '''
    Function to delete a user
    '''
    credentials.del_credentials()

def find_credentials(media):
    '''
    Function tha finds credentials by media name
    '''
    return Credentials.find_by_media(media)

def check_existing_credentials(media):
    '''
    Function that checks if credentials exist
    '''
    return Credentials.credentials_exist(media)

def display_credentials():
    '''
    Function that returns the saved credentials
    '''
    return Credentials.display_credentials()

def copy_username(cls,media):
    '''
    Function to copy data on the clipboard
    '''
    credentials_found = Credentials.find_by_media(media)
    pyperclip.copy(credentials_found.username)

def randomStringDigits(stringLength=6):
    """
    Generate a random string of letters and digits
    """
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))



def read_credentials():
    '''
    Functions that reads credentials to the user
    '''
    while True:
        print("Use these short codes; Enter : cc - create new credentials, dc - display your all credentials, fc -find credentials, ex -exit the credentials list, rc -Delete credentials")
        short_code = input().lower()

        if short_code == 'cc':
            print("New Credentials")
            print("-"*10)

            print ("media name ....")
            media = input()

            print("username ...")
            username = input()

            print (f"Is this {media} account not created yet? Generating a password for you?(y/n)")
            answer = input()
            if answer == 'y':
                password = randomStringDigits(8)
                print ("Your password is  ", password)
                handle = open("cred.txt", "a")
                handle.write(media)
                handle.write(username)
                handle.write(password)
                handle.close()
            elif answer == 'n':
                print("enter the desired password.")
                print("Password ...")
                password = input()

                handle = open("cred.txt", "a")
                handle.write(media)
                handle.write(username)
                handle.write(password)
                handle.close()

            save_credentials(create_credentials(media,username,password))
            print ('\n')
            print(f"New Credentials of {media} created")
            print ('\n')

        elif short_code == 'dc':

            if display_credentials():
                print("Here is a list of all your credentials")
                print('\n')

                for credentials in display_credentials():
                    print(f"{credentials.media} \n Username:{credentials.username} \n Password:{credentials.password}")

                    print('\n')
            else:
                print('\n')
                print("You don't seem to have such credentials saved yet")
                print('\n')

        elif short_code == 'fc':

            print("Enter the credentilas' media name you want to search for")

            search_name = input()
            if check_existing_credentials(search_name):
                search_credentials = find_credentials(search_name)
                print(f"{search_credentials.media} '\n' {search_credentials.username} {search_credentials.password}")
                print('-' * 20)
            else:
                print("That media credentials do not exist")

        elif short_code == 'rc':
            print("Enter the name of the user you want to delete")
            media = input()
            if check_existing_credentials(media):
                media = find_credentials(media)
                if del_credentials(media):
                    print(f"The credentials {media}are deleted")

            else:
                print("That media credentials do not exist")

if __name__ == '__read_credentials__':
    read_credentials()




def main():
    print("Hello Welcome to the user list. What is your name?")
    name = input()

    print(f"Hello {name}. what would you like to do?")
    print('\n')

    while True:
        print("Use these short codes : cu - create a new user, du - display users, fu -find a user, ex -exit the user list, li -log into your account, ru -Delete a user")

        short_code = input().lower()

        if short_code == 'cu':
            print("New User")
            print("-"*10)

            print ("twitter name ....")
            tname = input()

            print("twitter username ...")
            tusername = input()

            print("Password ...")
            tpassword = input()

            handle = open("user.txt", "a")
            handle.write(tname+'\n')
            handle.write(tusername+' ')
            handle.write(tpassword+'\n')
            handle.close()

            save_users(create_user(tname,tusername,tpassword))
            print("\n")
            print(f"New User {tname} created")
            print('\n')

        elif short_code == 'du':

            if display_users():
                print("Here is a list of all your users")
                print('\n')

                for user in display_users():
                    with open("user.txt","r") as handle:
                        count = 0
                        for line in handle:
                            count+=1
                            if count%2==1:
                                print(line)
                        # data = handle.readline()
                        # print(data+'\n')

                print('\n')
            else:
                print('\n')
                print("You don't seem to have that account saved yet")
                print('\n')

        elif short_code == 'fu':

            print("Enter the twitter name you want to search for")

            search_name = input()
            if check_existing_user(search_name):
                search_user = find_user(search_name)
                print(f"{search_user.tname} {search_user.tusername}")
                print('-' * 20)
            else:
                print("That user does not exist\n")

        elif short_code == 'li':
            print("Enter your twitter name")
            username = input()
            if check_existing_user(username):
                username = find_user(username)
                print("Enter the password")
                password = input()
                if check_existing_user(password):
                    password = find_user(password)

                    if read_credentials():
                        handle = open("cred.txt", "a")
                        handle.write(media)
                        handle.write(username)
                        handle.write(password)
                        handle.close()

        elif short_code == "ex":
            print("Bye .......")
            break

        elif short_code == 'ru':
            print("Enter the name of the user you want to delete")
            user = input()
            if check_existing_user(user):
                user = find_user(user)
                print("Enter the password")
                password = input()
                if check_existing_user(password):
                    password = find_user(password)
                    if del_user(user):
                        print("The user is deleted")


        else:
            print("I really didn't get that. Please use the short codes")

if __name__ == '__main__':
    main()

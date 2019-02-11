#!/usr/bin/env python3.6
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
    user.delete_user()

def find_user(fname):
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
    new_credentials=User(media,username,password)
    return new_credentials

def save_credential(credentials):
    '''
    Function to save credentials
    '''
    credentials.save_credentials()

def del_credentials(credentials):
    '''
    Function to delete a user
    '''
    credentials.delete_credentials()

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

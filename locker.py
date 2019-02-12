import pyperclip

class User:
    """
    Class that generates new instances of Users
    """

    user_list = []

    def __init__(self,tname,tusername,tpassword):

        '''
        __init__ method that helps us define properties for our objects.

        Args:
            tname: twitter name.
            tusername: twitter username.
            tpassword: twitter password.
        '''
        self.tname = tname
        self.tusername = tusername
        self.tpassword = tpassword

    def save_user(self):
        '''
        save_user method saves user objects into user_list
        '''
        User.user_list.append(self)

    def delete_user(self):
        '''
        delete_user method deletes a saved user from the user_list
        '''
        User.user_list.remove(self)

    @classmethod
    def find_by_tname(cls,tname):
        '''
        Method that takes in twitter credentials and returns a user that matches that twitter.

        Args:
            tname: twitter name to search for
        Returns :
            User that matches the twitter name.
        '''

        for user in cls.user_list:
            if user.tname == tname:
                return user

    @classmethod
    def user_exist(cls,tname):
        '''
        Method that checks if a user exists from the user list.
        Args:
            tname: twitter name to search if it exists
        Returns :
            Boolean: True or false depending if the user exists
        '''
        for user in cls.user_list:
            if user.tname == tname:
                    return True

        return False

    @classmethod
    def display_users(cls):
        '''
        method that returns the user_list
        '''
        return cls.user_list

    @classmethod
    def copy_tusername(cls,tname):
        user_found = User.find_by_tname(tname)
        pyperclip.copy(user_found.tusername)

class Credentials:
    """
    Class that generates new instances of Credentials
    """
    credentials_list = []

    def __init__(self,media,username,password):

        '''
        __init__ method that helps us define properties for our objects.

        Args:
            username: New user username.
            password: New user password.
        '''
        self.media = media
        self.username = username
        self.password = password

    def save_credentials(self):
        '''
        save_user method saves user objects into user_list
        '''
        Credentials.credentials_list.append(self)

    def delete_credentials(self):
        '''
        delete_credentials method deletes a saved credential from the credentials_list
        '''
        Credentials.credentials_list.remove(self)

    @classmethod
    def find_by_media(cls,media):
        '''
        Method that takes in media name and returns credentials that matches that media.

        Args:
            media: media name to search for
        Returns :
            credentials that matches the media name.
        '''

        for credentials in cls.credentials_list:
            if credentials.media == media:
                return credentials

    @classmethod
    def credentials_exist(cls,media):
        '''
        Method that checks if a credential exists from the credentials list.
        Args:
            media: media name to search if it exists
        Returns :
            Boolean: True or false depending if the credential exists
        '''
        for credentials in cls.credentials_list:
            if credentials.media == media:
                    return True

        return False

    @classmethod
    def display_credentials(cls):
        '''
        method that returns the credentials list
        '''
        return cls.credentials_list

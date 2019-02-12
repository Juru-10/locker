import unittest
import pyperclip
import readfiles

from locker import User
from locker import Credentials

class TestUser(unittest.TestCase):
    '''
    Test that defines test cases for the user class behaviours

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test caseself.
        '''
        self.new_user = User("Juru","juru","1234")

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.tname,"Juru")
        self.assertEqual(self.new_user.tusername,"juru")
        self.assertEqual(self.new_user.tpassword,"1234")

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.user_list = []

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into the user user_list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

    def test_save_multiple_user(self):
        '''
        test_save_multiple_user to check if we can save multiple user objects to our user_list
        '''
        self.new_user.save_user()
        test_user = User("Test","user","test")
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)

    def test_delete_user(self):
        '''
        test_delete_user to test if we can remove a user from our user list
        '''
        self.new_user.save_user()
        test_user = User("Test","user","test") # new user
        test_user.save_user()

        self.new_user.delete_user()# Deleting a user object
        self.assertEqual(len(User.user_list),1)

    def test_find_user_by_tname(self):
        '''
        test to check if we can find a user by twitter credentials and display information
        '''
        self.new_user.save_user()
        test_user = User("Juru","juru","test") # new user
        test_user.save_user()

        found_user = User.find_by_tname("Juru")

        self.assertEqual(found_user.tusername,test_user.tusername)

    def test_user_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the user.
        '''
        self.new_user.save_user()
        test_user = User("Test","user","test")
        test_user.save_user()

        user_exists = User.user_exist("Test")

        self.assertTrue(user_exists)

    def test_display_all_users(self):
        '''
        method that returns a list of all users saved
        '''
        self.assertEqual(User.display_users(),User.user_list)

    def test_copy_tusername(self):
        '''
        Test to confirm that we are copying the twitter name fromm a found user
        '''
        self.new_user.save_user()
        User.copy_tusername("Juru")
        self.assertEqual(self.new_user.tusername,pyperclip.paste())

    class TestReadFiles(unittest.TestCase):
    '''
    Class to test the  functions on the  readfiles module

    Args:
        unittest.TestCase: Class from the unittest module to create unit tests
    '''

    def test_get_data(self):
        """
        Test case to confirm that we are getting data from the file
        """
        with open("test.txt","r") as handle:
            data = handle.read()
            self.assertEqual(data,readfiles.read_file("test.txt"))

if __name__ == '__main__':
    unittest.main()


class TestCredentials(unittest.TestCase):
    '''
    Test that defines test cases for the Credentials class behaviours

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test caseself.
        '''
        self.new_credentials = Credentials("FB","Ajuru","F1234")

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_credentials.media,"FB")
        self.assertEqual(self.new_credentials.username,"Ajuru")
        self.assertEqual(self.new_credentials.password,"F1234")

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Credentials.credentials_list = []

    def test_save_credentials(self):
        '''
        test_save_credentials test case to test if the user object is saved into the user credentials_list
        '''
        self.new_credentials.save_credentials()
        sels.assertEqual(len(Credentials.credentials_list),1)

    def test_save_multiple_credentials(self):
        '''
        test_save_multiple_credentials to check if we can save multiple credentials objects to our credentials_list
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials("Test","credentials","test")
        test_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),2)

    def test_delete_credentials(self):
        '''
        test_delete_credentials to test if we can remove a credential from our credentials list
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials("Test","credentials","test") # new credentials
        test_credentials.save_credentials()

        self.new_credentials.delete_credentials()# Deleting a credentials object
        self.assertEqual(len(Credentials.credentials_list),1)

    def test_find_credentials_by_media(self):
        '''
        test to check if we can find a credentials by twitter credentials and display information
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials("FB","Ajuru","test") # new contact
        test_credentials.save_credentials()

        found_credentials = Credentials.find_by_media("FB")

        self.assertEqual(found_credentials.username,test_credentials.username)

    def test_credentials_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the credentials.
        '''

        self.new_credentials.save_credentials()
        test_credentials = Credentials("Test","user","test") # new credentials
        test_credentials.save_credentials()

        credentials_exists = Credentials.credentials_exist("Test")

        self.assertTrue(credentials_exists)

    def test_display_all_credentials(self):
        '''
        method that returns a list of all credentials saved
        '''
        self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)

if __name__ == '__main__':
    unittest.main()

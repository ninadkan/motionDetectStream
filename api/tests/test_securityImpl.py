# This will unit test the securityImpl.py
import unittest
import sys
sys.path.insert(0,'..')
sys.path.insert(0, '../..')
import securityImpl
import os

class Test_storageBlobService(unittest.TestCase):
    def setUp(self):
        '''
        problem is that this setUp is getting called before every test
        Which is ok for testing, but not ideal, as it means that the 
        storageBlobServiceWrapper gets created far too many times. 
        Not ideal but ok for the time being. 
        '''
        ACCOUNT_NAME=os.getenv('AZURE_STORAGE_ACCOUNT_NAME')
        STORAGE_KEY=os.getenv('AZURE_STORAGE_KEY')
        return

    def test_validateRequest(self):
        return

    def test_validateUserCredentials(self):
        return

    def test_get_token_with_authorization_code(self):
        return

if __name__ == '__main__':
    unittest.main()

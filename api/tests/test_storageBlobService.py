# This will unit test the storageBlobService.py
import unittest
import sys
sys.path.insert(0,'..')
import storageBlobService
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
        self.service=storageBlobService.StorageBlobServiceWrapper(account_name=ACCOUNT_NAME)
        STORAGE_KEY=os.getenv('AZURE_STORAGE_KEY')
        self.service.set_storageKey(storageKey=STORAGE_KEY)
        return

    def test_getBlobContent(self):
        self.assertIsNotNone(self.service)
        content=self.service.get_blob_content()
        self.assertEqual(type(content), bytes)
        self.assertIsNotNone(content)
        return

    def test_updateBlobContent(self):
        self.assertIsNotNone(self.service)
        textToBeUpdated=u'MyTextToBeIncluded'
        self.service.update_blob_content(textToBeUpdated)
        content=self.service.get_blob_content()
        self.assertEqual(type(content), bytes)
        strContent=str(content, 'utf-8')
        self.assertEqual(textToBeUpdated,strContent)
        return

if __name__ == '__main__':
    unittest.main()

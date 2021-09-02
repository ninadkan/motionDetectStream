import io
import os
import random
import time
import uuid

from azure.storage.blob import (
    BlobServiceClient, ContainerClient, BlobClient
)

from azure.core.exceptions import ResourceNotFoundError, ResourceExistsError

class StorageBlobServiceWrapper():
    """
    This class wraps the Blob storage. Should be created in two phases. First passing the 
    account name and second passing the accountkey from the KeyValut. After this the service 
    object is created and can be used to access the blob items 
    Everything needs to be re-written as the base class no longer exists in the latest python module and 
    has been replaced by the BlobServiceClient module!!! Charming
    """

    def __init__(self, account_name): 
        self.account_name=account_name
        self.account_key=None 
        self.service = None 
        self.container_name = 'listcontainer'
        self.blob_name = 'listblob'
        # our flag to ensure that the container and blobs are already created
        self._container_blob_created = False
        return


    '''
    four options for passing credentials, we are using option 2
    1. To use a shared access signature (SAS) token,
    provide the token as a string.If your account URL includes 
    the SAS token, omit the credential parameter.
    2. To use a storage account shared access key, 
    provide the key as a string.
    3. To use an Azure Active Directory (AAD) token credential, 
    provide an instance of the desired credential type obtained from 
    the azure-identity library.
    4.To use anonymous public read access, simply omit the credential parameter.
    '''

    def set_storageKey(self,storageKey):
        self.account_key=storageKey
        self.connectionString="DefaultEndPointsProtocol=https;AccountName={0};AccountKey={1};EndpointSuffix=core.windows.net".format(self.account_name, self.account_key)
        self.service = BlobServiceClient.from_connection_string(self.connectionString)
        return

    def get_blob_content(self):
        self._check_create_container_blob()
        blob_client = self.service.get_blob_client(self.container_name, self.blob_name)
        content = blob_client.download_blob().readall()
        return content

    def update_blob_content(self, txtcontent):
        self._check_create_container_blob()
        blob_client = self.service.get_blob_client(self.container_name, self.blob_name)
        blob_client.upload_blob(txtcontent, overwrite=True)
        return

    # This function checks that container and blob are created and if not 
    # creates them and sets a flag to indicate that they've been created. 
    def _check_create_container_blob(self):
        if (not self.service):
            return 
        # our floag indicates that we don't know if the container or blog have 
        # been created/exist 
        if (not self._container_blob_created):
            self._container_exists_create()
            self._blob_exists_create()
            # Assuming the everything worked and we are going to set our flag
            self._container_blob_created = True

    # check if the container exists and if not creates it 
    def _container_exists_create(self):
        container = ContainerClient.from_connection_string(self.connectionString, self.container_name)
        if not container.exists():
            container = container.create_container()
        return container

    # checks if Blob exists and if not creates it 
    def _blob_exists_create(self):
        try:
            blob_client = self.service.get_blob_client(self.container_name, self.blob_name) 
            blob_client.get_blob_properties() 
        except ResourceNotFoundError:
            # create an empty blob
            blob_client = blob_client.upload_blob(u'')
        return blob_client





   


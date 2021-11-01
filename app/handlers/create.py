from uuid import uuid4 as uuid
import datetime
from google.cloud import storage
import cryptocode
import os

class Save:
    def __init__(self, secret, password):
        self.secret = secret
        self.password = password
        self.date = datetime.datetime.today().strftime ('%d-%m-%Y')
        self.uid = str(uuid())
        self.encryptionPass = self.password+self.date

    def createFile(self):
        encoded = cryptocode.encrypt(self.secret, self.encryptionPass)
        client = storage.Client()
        bucket = client.get_bucket(os.environ.get("BUCKET"))
        filename = self.uid
        blob = bucket.blob(filename)
        blob.upload_from_string(encoded)
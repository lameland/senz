from google.cloud import storage
import cryptocode
import os
import logging


class Get:
    def __init__(self, uid, password, date):
        self.uid = (uid,)
        self.password = (password,)
        self.date = date
        self.client = storage.Client()
        self.bucket = self.client.get_bucket(os.environ.get("BUCKET"))

    def decrypt(self):
        try:

            filename = self.uid[0]
            password = self.password[0]
            blob = self.bucket.blob(filename)
            blob = blob.download_as_text()
            decryptionPass = password + self.date
            decoded = cryptocode.decrypt(blob, decryptionPass)
            return decoded
        except Exception as ex:
            logging.info(ex)
            return False

    def destroy(self):

        try:
            blob = self.bucket.blob(self.uid[0])
            blob.delete()
            return True
        except Exception as ex:
            logging.info(ex)
            return False

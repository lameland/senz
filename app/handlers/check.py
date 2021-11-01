from google.cloud import storage
import os


class Check:
    def __init__(self, uid) -> None:
        self.uid = uid

    def checkExist(self):
        client = storage.Client()
        bucket = client.get_bucket(os.environ.get("BUCKET"))
        filename = self.uid
        blob = bucket.blob(filename)
        return blob.exists()

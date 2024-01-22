import os
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


MODULE_PATH = os.path.dirname(os.path.abspath(__file__))
CREDENTIALS_PATH = os.path.join(MODULE_PATH, 'credentials.json')


class Google:
    def __init__(self, service_name, service_version, scopes, file_id):
        self.credentials = None
        if os.path.exists(CREDENTIALS_PATH):
            self.credentials = Credentials.from_service_account_file(CREDENTIALS_PATH)
        else:
            print("There aren't credentials.")
        self.service = None
        if self.credentials:
            try:
                self.service = build(service_name, service_version, credentials=self.credentials.with_scopes(scopes))
            except HttpError as error:
                print(f"An error occurred: {error}.")
        self.file_id = file_id

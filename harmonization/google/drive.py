# Source:
# - https://developers.google.com/drive/api/quickstart/python?hl=es-419
# - https://developers.google.com/drive/api/reference/rest/v3/comments/list


from harmonization.google.google import Google


SCOPES = [
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/drive.file',
    'https://www.googleapis.com/auth/drive.readonly'
]


class Drive(Google):
    def __init__(self, file_id):
        super().__init__('drive', 'v3', SCOPES, file_id)
        self.comments = []

    def get_comments(self):
        if self.service:
            self.comments = self.service.comments().list(fileId=self.file_id, fields='comments').execute()
        print(self.comments)

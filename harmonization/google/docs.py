# Source:
# - https://developers.google.com/docs/api/quickstart/python?hl=es-419
# - https://developers.google.com/docs/api/how-tos/suggestions#python


from harmonization.google.google import Google


SCOPES = [
    'https://www.googleapis.com/auth/documents'
]

SUGGEST_MODE="SUGGESTIONS_INLINE"


class Docs(Google):
    def __init__(self, file_id):
        super().__init__('docs', 'v1', SCOPES, file_id)
        self.suggestions = {}
    
    def get_suggestions(self):
        document_with_suggestions = []
        if self.service:
            document_with_suggestions = self.service.documents().get(documentId=self.file_id, suggestionsViewMode=SUGGEST_MODE).execute()
        suggestions = []
        if 'body' in document_with_suggestions:
            if 'content' in document_with_suggestions['body']:
                for content in document_with_suggestions['body']['content']:
                    if 'paragraph' in content:
                        if 'elements' in content['paragraph']:
                            for element in content['paragraph']['elements']:
                                if 'textRun' in element:
                                    if 'suggestedInsertionIds' in element['textRun']:
                                        suggestions.append(element)
                                    if 'suggestedDeletionIds' in element['textRun']:
                                        suggestions.append(element)
        self.suggestions['suggestions'] = suggestions
        print(self.suggestions)

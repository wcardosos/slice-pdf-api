class DocumentNotFoundException(Exception):
    '''
        Exception that will raise when a Firestore document not exists.
    '''
    def __init__(self):
        Exception.__init__(self, 'Document not found')
        self.message = 'Document not found'

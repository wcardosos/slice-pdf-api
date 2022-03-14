class PDFFileNotFoundException(Exception):
    '''
        Exception that will raise when a PDF file not exists.
    '''
    def __init__(self):
        Exception.__init__(self, 'PDF file not found')
        self.message = 'PDF file not found'

class FileNotFoundException(Exception):
    '''
        Exception that will raise when a file not exists.
    '''
    def __init__(self, filepath: str):
        Exception.__init__(self, f'File {filepath} not found')
        self.message = f'File {filepath} not found'

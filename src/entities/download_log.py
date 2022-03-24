from datetime import datetime


class DownloadLog:
    '''
        Class to represent a download log.
    '''
    def __init__(
        self,
        pdf_file: str,
        timestamp: datetime
    ):
        self.pdf_file = pdf_file
        self.timestamp = timestamp

    def to_dict(self) -> dict:
        return {
            'pdf_file': self.pdf_file,
            'timestamp': self.timestamp
        }

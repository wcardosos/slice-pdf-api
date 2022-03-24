from pydantic import BaseModel  # pylint: disable=no-name-in-module


class DownloadLogModel(BaseModel):
    '''
        Class to represent the download log payload
    '''
    pdf_file: str

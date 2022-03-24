from pydantic import BaseModel


class DownloadLogModel(BaseModel):
    pdf_file: str

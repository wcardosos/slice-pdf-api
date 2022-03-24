from datetime import datetime
from fastapi import FastAPI, UploadFile
from entities.download_log import DownloadLog
from src.controllers.downloads import DownloadsController
from src.controllers.health_check import HealthCheckController
from src.controllers.slice import SliceController
from src.models.download_log import DownloadLogModel

app = FastAPI()


@app.post('/slice')
async def slice_pdf(pdf_file: UploadFile):
    '''
        Slice PDF endpoint
    '''
    return await SliceController.post(pdf_file)


@app.get('/downloads')
def get_downloads_count():
    '''
        Get downloads count
    '''
    return DownloadsController.get()


@app.post('/downloads')
def post_download_log(log: DownloadLogModel):
    '''
        Create a new download log
    '''
    return DownloadsController.post(log.pdf_file)


@app.put('/downloads')
def update_downloads_count():
    '''
        Update downloads count
    '''
    return DownloadsController.put()


@app.get('/health-check')
def health_check():
    '''
        Health check endpoint
    '''
    return HealthCheckController.get()

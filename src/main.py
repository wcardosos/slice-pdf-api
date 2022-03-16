from fastapi import FastAPI, UploadFile
from src.controllers.health_check import HealthCheckController
from src.controllers.slice import SliceController


app = FastAPI()


@app.post('/slice')
async def slice_pdf(pdf_file: UploadFile):
    '''
        Slice PDF endpoint
    '''
    return await SliceController.post(pdf_file)


@app.get('/health-check')
def health_check():
    '''
        Health check endpoint
    '''
    return HealthCheckController.get()

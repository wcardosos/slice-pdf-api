from fastapi import FastAPI
from controllers.health_check import HealthCheckController


app = FastAPI()


@app.get('/health-check')
def health_check():
    '''
        Health check endpoint
    '''
    return HealthCheckController.get()

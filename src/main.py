import json
from fastapi import FastAPI, Response


app = FastAPI()


@app.get('/health-check')
def health_check():
    '''
        Health check endpoint
    '''
    return Response(content=json.dumps({}))

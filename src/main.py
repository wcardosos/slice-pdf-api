from fastapi import FastAPI, Response
import json


app = FastAPI()

@app.get('/health-check')
def health_check():
    return Response(content=json.dumps({}))

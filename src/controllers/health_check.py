import json
from fastapi import Response


class HealthCheckController:
    '''
        Health check controller
    '''
    @staticmethod
    def get():
        '''
            Responsible method to handle 'GET' requests
        '''
        return Response(content=json.dumps({}), status_code=200)

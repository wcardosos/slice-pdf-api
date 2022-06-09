import json
from fastapi import Response


class DownloadsController:
    '''
        Downloads controller.
    '''
    @staticmethod
    def get() -> Response:
        '''
            Responsible method to return the downloads count.
        '''
        try:
            return Response(
                content=json.dumps({
                    'message': 'This feature will be implemented soon'
                }),
                status_code=501
            )
        except Exception as error:  # pylint: disable=(broad-except)
            return Response(
                content=json.dumps({'error': str(error)}),
                status_code=500
            )

    @staticmethod
    def post(pdf_file: str):
        '''
            Responsible to add download logs
        '''
        try:
            return Response(
                content=json.dumps({
                    'message': 'This feature will be implemented soon'
                }),
                status_code=501
            )
        except Exception as error:  # pylint: disable=(broad-except)
            return Response(
                content=json.dumps({'error': str(error)}),
                status_code=500
            )

    @staticmethod
    def put():
        '''
            Responsible method to update the downloads count.
        '''
        try:
            return Response(
                content=json.dumps({
                    'message': 'This feature will be implemented soon'
                }),
                status_code=501
            )
        except Exception as error:  # pylint: disable=(broad-except)
            return Response(
                content=json.dumps({'error': str(error)}),
                status_code=500
            )

import json
from fastapi import Response
from src.errors.firestore.document_not_found_exception import (
    DocumentNotFoundException
)
from src.repositories.Firestore.downloads_count_firestore_repository import (
    DownloadsCountFirestoreRepository
)


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
            downloads_count_repository = DownloadsCountFirestoreRepository()
            downloads_count = downloads_count_repository.get()

            return Response(
                content=json.dumps({'count': downloads_count}),
                status_code=200
            )
        except DocumentNotFoundException:
            return Response(
                content=json.dumps({'error': 'The downloads count not found'}),
                status_code=500
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
            downloads_count_repository = DownloadsCountFirestoreRepository()
            downloads_count_repository.update()

            return Response(
                content=json.dumps({}),
                status_code=200
            )
        except Exception as error:  # pylint: disable=(broad-except)
            return Response(
                content=json.dumps({'error': str(error)}),
                status_code=500
            )

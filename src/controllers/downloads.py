import json
from fastapi import Response
from src.entities.DownloadLog import DownloadLog
from src.repositories.Firestore.downloads_count_firestore_repository import (
    DownloadsCountFirestoreRepository
)
from src.repositories.Firestore.download_logs_firestore_repository import (
    DownloadLogsFirestoreRepository
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
            download_logs_repository = DownloadLogsFirestoreRepository()
            downloads_count = download_logs_repository.get_downloads_count()

            return Response(
                content=json.dumps({'count': downloads_count}),
                status_code=200
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

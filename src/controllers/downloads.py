import json
from datetime import datetime
from fastapi import Response
from entities.download_log import DownloadLog
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
    def post(pdf_file: str):
        '''
            Responsible to add download logs
        '''
        try:
            timestamp = datetime.now()
            download_log = DownloadLog(pdf_file, timestamp)
            download_logs_repository = DownloadLogsFirestoreRepository()
            download_logs_repository.add_log(download_log)

            return Response(
                content=json.dumps({}),
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

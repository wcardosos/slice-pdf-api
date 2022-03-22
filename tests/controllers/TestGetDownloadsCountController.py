import json
from unittest import TestCase, main
from unittest.mock import patch, MagicMock
from src.controllers.downloads import DownloadsController
from src.errors.firestore.document_not_found_exception import DocumentNotFoundException
from src.repositories.Firestore.downloads_count_firestore_repository import DownloadsCountFirestoreRepository


class TestGetDownloadsCountController(TestCase):
    def test_should_get_downloads_count(self):
        with patch('src.controllers.downloads.Response') as response_mock:
            with patch.object(DownloadsCountFirestoreRepository, 'get') as get_downloads_count_mock:
                get_downloads_count_mock.return_value = 1

                DownloadsController.get()

                response_mock.assert_called_once_with(
                    content=json.dumps({ 'count': 1 }),
                    status_code=200
                )

    def test_should_return_error_message_when_firestore_doc_not_found(self):
        with patch('src.controllers.downloads.Response') as response_mock:
            with patch.object(DownloadsCountFirestoreRepository, 'get') as get_downloads_count_mock:
                get_downloads_count_mock.side_effect = DocumentNotFoundException()

                DownloadsController.get()

                response_mock.assert_called_once_with(
                    content=json.dumps({ 'error': 'The downloads count not found' }),
                    status_code=500
                )

    def test_should_return_generic_error(self):
        with patch('src.controllers.downloads.Response') as response_mock:
            with patch.object(DownloadsCountFirestoreRepository, 'get') as get_downloads_count_mock:
                get_downloads_count_mock.side_effect = Exception('error')

                DownloadsController.get()

                response_mock.assert_called_once_with(
                    content=json.dumps({ 'error': 'error' }),
                    status_code=500
                )

if __name__ == '__main__':
    main()

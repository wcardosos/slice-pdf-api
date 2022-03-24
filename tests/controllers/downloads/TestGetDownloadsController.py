import json
from unittest import TestCase, main
from unittest.mock import patch, MagicMock
from src.controllers.downloads import DownloadsController
from src.errors.firestore.document_not_found_exception import DocumentNotFoundException


class TestGetDownloadsCountController(TestCase):
    def test_should_get_downloads_count(self):
        with patch('src.controllers.downloads.Response') as response_mock:
            with patch('src.controllers.downloads.DownloadLogsFirestoreRepository') as download_logs_class_mock:
                download_logs_mock = MagicMock()
                download_logs_mock.get_downloads_count.return_value = 1
                download_logs_class_mock.return_value = download_logs_mock

                DownloadsController.get()

                response_mock.assert_called_once_with(
                    content=json.dumps({ 'count': 1 }),
                    status_code=200
                )

    def test_should_return_generic_error(self):
        with patch('src.controllers.downloads.Response') as response_mock:
            with patch('src.controllers.downloads.DownloadLogsFirestoreRepository') as download_logs_class_mock:
                download_logs_class_mock.side_effect = Exception('error')

                DownloadsController.get()

                response_mock.assert_called_once_with(
                    content=json.dumps({ 'error': 'error' }),
                    status_code=500
                )

if __name__ == '__main__':
    main()

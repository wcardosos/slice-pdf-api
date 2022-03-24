import json
from unittest import TestCase, main
from unittest.mock import patch, MagicMock
from src.controllers.downloads import DownloadsController
from src.errors.firestore.document_not_found_exception import DocumentNotFoundException
from src.repositories.Firestore.downloads_count_firestore_repository import DownloadsCountFirestoreRepository


class TestPutDownloadsCountController(TestCase):
    def test_should_get_downloads_count(self):
        with patch('src.controllers.downloads.Response') as response_mock:
            with patch('src.controllers.downloads.DownloadsCountFirestoreRepository') as downloads_count_repository_class_mock:
                downloads_count_repository_mock = MagicMock()
                downloads_count_repository_mock.update = MagicMock()
                downloads_count_repository_class_mock.return_value = downloads_count_repository_mock

                DownloadsController.put()

                downloads_count_repository_mock.update.assert_called_once()
                response_mock.assert_called_once_with(
                    content=json.dumps({}),
                    status_code=200
                )

if __name__ == '__main__':
    main()

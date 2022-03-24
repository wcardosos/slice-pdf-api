from unittest import TestCase, main
from unittest.mock import patch, MagicMock
from src.entities.DownloadLog import DownloadLog
from src.errors.firestore.document_not_found_exception import DocumentNotFoundException
from src.repositories.Firestore.download_logs_firestore_repository import DownloadLogsFirestoreRepository
from tests.__mocks__.firestore_client_mock import FirestoreClientMock


class TestDownloadLogsFirestoreRepository(TestCase):
    def test_should_create_new_firebase_app_and_set_firestore_client(self):
        with patch.dict('src.repositories.Firestore.base_firestore_repository.firebase_apps', { '[DEFAULT]': None }) as firebase_apps_mock:
            with patch('src.repositories.Firestore.base_firestore_repository.credentials.Certificate') as credentials_certificate_mock:
                with patch('src.repositories.Firestore.base_firestore_repository.initialize_app') as initialize_app_mock:
                    with patch('src.repositories.Firestore.base_firestore_repository.firestore.client') as firestore_client_mock:
                        initialize_app_mock.return_value = 'app'
                        credentials_certificate_mock.return_value = 'credentials'

                        DownloadLogsFirestoreRepository()

                        credentials_certificate_mock.assert_called_once()
                        initialize_app_mock.assert_called_once_with('credentials')
                        firestore_client_mock.assert_called_once_with('app')
    
    def test_should_set_firebase_app_when_it_already_exists_and_set_firestore_client(self):
        with patch.dict('src.repositories.Firestore.base_firestore_repository.firebase_apps', { '[DEFAULT]': 'app' }) as firebase_apps_mock:
            with patch('src.repositories.Firestore.base_firestore_repository.credentials.Certificate') as credentials_certificate_mock:
                with patch('src.repositories.Firestore.base_firestore_repository.initialize_app') as initialize_app_mock:
                    with patch('src.repositories.Firestore.base_firestore_repository.firestore.client') as firestore_client_mock:
                        DownloadLogsFirestoreRepository()

                        credentials_certificate_mock.assert_not_called()
                        initialize_app_mock.assert_not_called()
                        firestore_client_mock.assert_called_once_with('app')
    
    def test_should_get_collection(self):
        with patch.dict('src.repositories.Firestore.base_firestore_repository.firebase_apps', { '[DEFAULT]': 'app' }) as firebase_apps_mock:
            with patch('src.repositories.Firestore.base_firestore_repository.firestore.client', autospec=True) as firestore_client_mock:
                firestore_client_mock.return_value = FirestoreClientMock(has_doc=True)

                downloads_count_firestore_repository = DownloadLogsFirestoreRepository()

                result = downloads_count_firestore_repository.get_collection()

                # This assert check if the result is a collection instance.
                self.assertTrue(hasattr(result, 'document'))
    
    def test_should_add_log(self):
        with patch.dict('src.repositories.Firestore.base_firestore_repository.firebase_apps', { '[DEFAULT]': 'app' }) as firebase_apps_mock:
            with patch('src.repositories.Firestore.base_firestore_repository.firestore.client', autospec=True) as firestore_client_mock:
                with patch.object(DownloadLogsFirestoreRepository, 'get_collection') as get_collection_mock:
                    collection_mock = MagicMock()
                    collection_mock.add = MagicMock()
                    get_collection_mock.return_value = collection_mock
                    firestore_client_mock.return_value = FirestoreClientMock(has_doc=True)
                    download_log_mock = DownloadLog('file', 'date')

                    downloads_count_firestore_repository = DownloadLogsFirestoreRepository()

                    downloads_count_firestore_repository.add_log(download_log_mock)

                    collection_mock.add.assert_called_once_with({
                        'pdf_file': 'file',
                        'timestamp': 'date'
                    })

    def test_should_get_downloads_count(self):
        with patch.dict('src.repositories.Firestore.base_firestore_repository.firebase_apps', { '[DEFAULT]': 'app' }) as firebase_apps_mock:
            with patch('src.repositories.Firestore.base_firestore_repository.firestore.client', autospec=True) as firestore_client_mock:
                with patch.object(DownloadLogsFirestoreRepository, 'get_collection') as get_collection_mock:
                    collection_mock = MagicMock()
                    collection_mock.get = MagicMock()
                    collection_mock.get.return_value = ['item 1', 'item2']
                    get_collection_mock.return_value = collection_mock
                    firestore_client_mock.return_value = FirestoreClientMock(has_doc=True)

                    downloads_count_firestore_repository = DownloadLogsFirestoreRepository()

                    result = downloads_count_firestore_repository.get_downloads_count()

                    self.assertEqual(result, 2)

if __name__ == '__main__':
    main()

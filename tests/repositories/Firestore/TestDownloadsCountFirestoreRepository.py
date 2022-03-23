from unittest import TestCase, main
from unittest.mock import patch, MagicMock
from src.errors.firestore.document_not_found_exception import DocumentNotFoundException
from src.repositories.Firestore.downloads_count_firestore_repository import DownloadsCountFirestoreRepository
from tests.__mocks__.firestore_client_mock import FirestoreClientMock, DocumentMock, ReferenceSucessMock


class TestDownloadsCountFirestoreRepository(TestCase):
    def test_should_create_new_firebase_app_and_set_firestore_client(self):
        with patch.dict('src.repositories.Firestore.base_firestore_repository.firebase_apps', { '[DEFAULT]': None }) as firebase_apps_mock:
            with patch('src.repositories.Firestore.base_firestore_repository.credentials.Certificate') as credentials_certificate_mock:
                with patch('src.repositories.Firestore.base_firestore_repository.initialize_app') as initialize_app_mock:
                    with patch('src.repositories.Firestore.base_firestore_repository.firestore.client') as firestore_client_mock:
                        initialize_app_mock.return_value = 'app'
                        credentials_certificate_mock.return_value = 'credentials'

                        DownloadsCountFirestoreRepository()

                        credentials_certificate_mock.assert_called_once()
                        initialize_app_mock.assert_called_once_with('credentials')
                        firestore_client_mock.assert_called_once_with('app')
    
    def test_should_set_firebase_app_when_it_already_exists_and_set_firestore_client(self):
        with patch.dict('src.repositories.Firestore.base_firestore_repository.firebase_apps', { '[DEFAULT]': 'app' }) as firebase_apps_mock:
            with patch('src.repositories.Firestore.base_firestore_repository.credentials.Certificate') as credentials_certificate_mock:
                with patch('src.repositories.Firestore.base_firestore_repository.initialize_app') as initialize_app_mock:
                    with patch('src.repositories.Firestore.base_firestore_repository.firestore.client') as firestore_client_mock:
                        DownloadsCountFirestoreRepository()

                        credentials_certificate_mock.assert_not_called()
                        initialize_app_mock.assert_not_called()
                        firestore_client_mock.assert_called_once_with('app')
    
    def test_should_get_firestore_document(self):
        with patch.dict('src.repositories.Firestore.base_firestore_repository.firebase_apps', { '[DEFAULT]': 'app' }) as firebase_apps_mock:
            with patch('src.repositories.Firestore.base_firestore_repository.firestore.client', autospec=True) as firestore_client_mock:
                    firestore_client_mock.return_value = FirestoreClientMock(has_doc=True)

                    downloads_count_firestore_repository = DownloadsCountFirestoreRepository()

                    result = downloads_count_firestore_repository.get_document()

                    # This assert check if the result is a document instance.
                    self.assertTrue(hasattr(result, 'get'))

    def test_should_get_downloads_count_data(self):
        with patch.dict('src.repositories.Firestore.base_firestore_repository.firebase_apps', { '[DEFAULT]': 'app' }) as firebase_apps_mock:
            with patch('src.repositories.Firestore.base_firestore_repository.firestore.client', autospec=True) as firestore_client_mock:
                    firestore_client_mock.return_value = FirestoreClientMock(has_doc=True)

                    downloads_count_firestore_repository = DownloadsCountFirestoreRepository()

                    result = downloads_count_firestore_repository.get_downloads_count_data()

                    # This assert check if the result is a doc reference instance.
                    self.assertTrue(hasattr(result, 'exists'))

    def test_should_raises_error_when_firestore_doc_do_not_exists(self):
        with patch.dict('src.repositories.Firestore.base_firestore_repository.firebase_apps', { '[DEFAULT]': 'app' }) as firebase_apps_mock:
            with patch('src.repositories.Firestore.base_firestore_repository.firestore.client', autospec=True) as firestore_client_mock:
                    firestore_client_mock.return_value = FirestoreClientMock(has_doc=False)

                    downloads_count_firestore_repository = DownloadsCountFirestoreRepository()

                    self.assertRaises(DocumentNotFoundException, downloads_count_firestore_repository.get_downloads_count_data)

    def test_should_get_downloads_count(self):
        with patch.dict('src.repositories.Firestore.base_firestore_repository.firebase_apps', { '[DEFAULT]': 'app' }) as firebase_apps_mock:
            with patch('src.repositories.Firestore.base_firestore_repository.firestore.client', autospec=True) as firestore_client_mock:
                with patch.object(DownloadsCountFirestoreRepository, 'get_downloads_count_data') as get_downloads_count_data_mock:
                    firestore_client_mock.return_value = FirestoreClientMock(has_doc=False)
                    get_downloads_count_data_mock.return_value = ReferenceSucessMock()
                    
                    downloads_count_firestore_repository = DownloadsCountFirestoreRepository()
                    result = downloads_count_firestore_repository.get()

                    self.assertEqual(result, 1)
    
    def test_should_update_downloads_count(self):
        with patch.dict('src.repositories.Firestore.base_firestore_repository.firebase_apps', { '[DEFAULT]': 'app' }) as firebase_apps_mock:
            with patch('src.repositories.Firestore.base_firestore_repository.firestore.client', autospec=True) as firestore_client_mock:
                with patch.object(DownloadsCountFirestoreRepository, 'get') as get_downloads_count_mock:
                    with patch.object(DownloadsCountFirestoreRepository, 'get_document') as get_document_mock:
                        document_mock = MagicMock()
                        document_mock.update = MagicMock()
                        get_document_mock.return_value = document_mock
                        firestore_client_mock.return_value = FirestoreClientMock(has_doc=False)
                        get_downloads_count_mock.return_value = 1
                        
                        downloads_count_firestore_repository = DownloadsCountFirestoreRepository()
                        downloads_count_firestore_repository.update()

                        document_mock.update.assert_called_once()

if __name__ == '__main__':
    main()

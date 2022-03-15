from unittest import TestCase, main
from unittest.mock import patch, MagicMock
from src.errors.files.file_not_found_exception import FileNotFoundException
from src.providers.file_handler import FileHandler


class TestFileHandler(TestCase):
    def test_should_delete_file(self):
        with patch('src.providers.file_handler.os') as os_mock:
            file_mock = 'file'
            os_mock.path.exists = MagicMock()
            os_mock.remove = MagicMock()
            os_mock.path.exists.return_value = True

            FileHandler.delete(file_mock)

            os_mock.remove.assert_called_once_with('file')

    def test_should_raise_file_not_found_exception(self):
        with patch('src.providers.file_handler.os') as os_mock:
            os_mock.path.exists = MagicMock()
            os_mock.path.exists.return_value = False

            self.assertRaises(FileNotFoundException, FileHandler.delete, 'file')
    
    def test_should_delete_many_files(self):
        files_mock = ['file 1', 'file 2', 'file 3']
        with patch.object(FileHandler, 'delete') as file_handler_delete_mock:
            FileHandler.delete_many(files_mock)

            self.assertEqual(file_handler_delete_mock.call_count, 3)


if __name__ == '__main__':
    main()

from unittest import TestCase, main
from unittest.mock import patch, MagicMock
from src.errors.pdf.pdf_file_not_found_exception import PDFFileNotFoundException
from src.providers.pdf_handler import PDFHandler


class TestPDFHandler(TestCase):
    def test_should_extract_pages_to_images_correctly(self):
        with patch('src.providers.pdf_handler.file_exists') as file_exists_mock:
            file_exists_mock.return_value = True

            with patch('src.providers.pdf_handler.convert_from_path') as convert_from_path_mock:
                pages_mock = MagicMock()
                pages_mock.save = MagicMock()

                convert_from_path_mock.return_value = [pages_mock, pages_mock]

                PDFHandler.extract_pages_to_images('path')

                convert_from_path_mock.assert_called_once_with('path')
                assert pages_mock.save.call_count == 2
    
    def test_should_raise_exception_when_file_not_exists(self):
        with patch('src.providers.pdf_handler.file_exists') as file_exists_mock:
            file_exists_mock.return_value = False

            self.assertRaises(PDFFileNotFoundException, PDFHandler.extract_pages_to_images, 'path')

if __name__ == '__main__':
    main()

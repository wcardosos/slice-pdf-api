from subprocess import call
from unittest import TestCase, main
from unittest.mock import patch, MagicMock
from src.errors.pdf.pdf_file_not_found_exception import PDFFileNotFoundException
from src.providers.pdf_handler import PDFHandler
from fpdf import FPDF


class TestPDFHandler(TestCase):
    def test_should_extract_pages_to_images_correctly(self):
        with patch('src.providers.pdf_handler.file_exists') as file_exists_mock:
            file_exists_mock.return_value = True

            with patch('src.providers.pdf_handler.convert_from_path') as convert_from_path_mock:
                pages_mock = MagicMock()
                pages_mock.save = MagicMock()
                expected_result = [
                    'page1.jpg',
                    'page2.jpg'
                ]

                convert_from_path_mock.return_value = [pages_mock, pages_mock]

                result = PDFHandler.extract_pages_to_images('path')

                convert_from_path_mock.assert_called_once_with('path')
                self.assertEqual(pages_mock.save.call_count, 2)
                self.assertEqual(result, expected_result)
    
    def test_should_raise_exception_when_file_not_exists(self):
        with patch('src.providers.pdf_handler.file_exists') as file_exists_mock:
            file_exists_mock.return_value = False

            self.assertRaises(PDFFileNotFoundException, PDFHandler.extract_pages_to_images, 'path')
    
    def test_should_create_pdf(self):
        with patch.object(FPDF, 'add_page') as fpdf_add_page_mock:
            with patch.object(FPDF, 'image') as fpdf_image_mock:
                with patch.object(FPDF, 'output') as fpdf_output_mock:
                    with patch.object(FPDF, 'close') as fpdf_close_mock:
                        images_list_mock = ['image 1', 'image 2']
                        filename_mock = 'file'

                        PDFHandler.create_from_images(images_list_mock, filename_mock)

                        self.assertEqual(fpdf_add_page_mock.call_count, 2)
                        self.assertEqual(fpdf_image_mock.call_count, 2)
                        fpdf_output_mock.assert_called_once_with('file', 'F')
                        fpdf_close_mock.assert_called_once()

if __name__ == '__main__':
    main()

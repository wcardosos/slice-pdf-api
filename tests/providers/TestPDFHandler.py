from unittest import TestCase, main
from unittest.mock import patch, MagicMock
from src.errors.pdf.pdf_file_not_found_exception import PDFFileNotFoundException
from src.providers.pdf_handler import PDFHandler
from src.providers.random_generator import RandomGenerator
from fpdf import FPDF


class TestPDFHandler(TestCase):
    def test_should_extract_pages_to_images_from_path_correctly(self):
        with patch('src.providers.pdf_handler.os') as os_mock:
            os_mock.path.exists = MagicMock()
            os_mock.getenv = MagicMock()
            os_mock.path.exists.return_value = True
            os_mock.getenv.return_value = 'home'
            pdf_handler = PDFHandler()

            with patch('src.providers.pdf_handler.convert_from_path') as convert_from_path_mock:
                with patch.object(RandomGenerator, 'generate_str') as generate_random_str_mock:
                    generate_random_str_mock.return_value = 'random'
                    pages_mock = MagicMock()
                    pages_mock.save = MagicMock()
                    expected_result = [
                        'home/.slicepdf/random.jpg',
                        'home/.slicepdf/random.jpg'
                    ]

                    convert_from_path_mock.return_value = [pages_mock, pages_mock]

                    result = pdf_handler.extract_pages_to_images_from_path('path')

                    convert_from_path_mock.assert_called_once_with('path')
                    self.assertEqual(pages_mock.save.call_count, 2)
                    self.assertEqual(result, expected_result)
    
    def test_should_extract_pages_to_images_from_bytes_correctly(self):
        with patch('src.providers.pdf_handler.os') as os_mock:
            os_mock.getenv = MagicMock()
            os_mock.getenv.return_value = 'home'
            pdf_handler = PDFHandler()

            with patch('src.providers.pdf_handler.convert_from_path') as convert_from_bytes_mock:
                with patch.object(RandomGenerator, 'generate_str') as generate_random_str_mock:
                    generate_random_str_mock.return_value = 'random'
                    pages_mock = MagicMock()
                    pages_mock.save = MagicMock()
                    expected_result = [
                        'home/.slicepdf/random.jpg',
                        'home/.slicepdf/random.jpg'
                    ]

                    convert_from_bytes_mock.return_value = [pages_mock, pages_mock]

                    result = pdf_handler.extract_pages_to_images_from_path('path')

                    convert_from_bytes_mock.assert_called_once_with('path')
                    self.assertEqual(pages_mock.save.call_count, 2)
                    self.assertEqual(result, expected_result)
    
    def test_should_raise_exception_when_file_not_exists(self):
        with patch('src.providers.pdf_handler.os') as os_mock:
            pdf_handler = PDFHandler()
            os_mock.path.exists = MagicMock()
            os_mock.path.exists.return_value = False

            self.assertRaises(PDFFileNotFoundException, pdf_handler.extract_pages_to_images_from_path, 'path')
    
    def test_should_create_pdf(self):
        with patch.object(FPDF, 'add_page') as fpdf_add_page_mock:
            with patch.object(FPDF, 'image') as fpdf_image_mock:
                with patch.object(FPDF, 'output') as fpdf_output_mock:
                    with patch.object(FPDF, 'close') as fpdf_close_mock:
                        pdf_handler = PDFHandler()
                        images_list_mock = ['image 1', 'image 2']
                        filename_mock = 'file'

                        pdf_handler.create_from_images(images_list_mock, filename_mock)

                        self.assertEqual(fpdf_add_page_mock.call_count, 2)
                        self.assertEqual(fpdf_image_mock.call_count, 2)
                        fpdf_output_mock.assert_called_once_with('file', 'F')
                        fpdf_close_mock.assert_called_once()

if __name__ == '__main__':
    main()

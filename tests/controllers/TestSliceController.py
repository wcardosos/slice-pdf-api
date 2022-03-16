from asyncio import Future
from fastapi.responses import FileResponse
from unittest import IsolatedAsyncioTestCase, main
from unittest.mock import patch, MagicMock
from src.providers.file_handler import FileHandler
from src.providers.image_handler import ImageHandler
from src.controllers.slice import SliceController
from src.providers.pdf_handler import PDFHandler


class TestSliceController(IsolatedAsyncioTestCase):
    @patch('src.controllers.slice.Logger')
    async def test_should_return_file(self, logger_mock):
        with patch('src.controllers.slice.os') as os_mock:
            with patch.object(PDFHandler, 'extract_pages_to_images_from_bytes') as extract_pages_to_images_from_bytes_mock:
                with patch.object(ImageHandler, 'halve') as halve_image_mock:
                    with patch.object(PDFHandler, 'create_from_images') as create_from_images_mock:
                        with patch.object(FileHandler, 'delete_many') as delete_many_files_mock:
                            with patch('src.controllers.slice.Image.open') as image_open_mock:
                                os_mock.getenv = MagicMock()
                                os_mock.path.exists = MagicMock()
                                os_mock.path.exists_mock.return_value = True
                                pdf_file_mock = MagicMock()
                                pdf_file_mock.read = MagicMock()
                                future_read_mock_result = Future()
                                future_read_mock_result.set_result('pdf content')
                                pdf_file_mock.read.return_value = future_read_mock_result

                                extract_pages_to_images_from_bytes_mock.return_value = ['image 1', 'image 2']

                                result = await SliceController.post(pdf_file_mock)

                                extract_pages_to_images_from_bytes_mock.assert_called_once_with('pdf content')
                                self.assertEqual(image_open_mock.call_count, 2)
                                self.assertEqual(halve_image_mock.call_count, 2)
                                create_from_images_mock.assert_called_once()
                                delete_many_files_mock.assert_called_once()
                                self.assertIsInstance(result, FileResponse)

    @patch('src.controllers.slice.Logger')
    async def test_should_return_file_and_create_app_dir_when_not_exists(self, logger_mock):
        with patch('src.controllers.slice.os') as os_mock:
            with patch.object(PDFHandler, 'extract_pages_to_images_from_bytes') as extract_pages_to_images_from_bytes_mock:
                with patch.object(ImageHandler, 'halve') as halve_image_mock:
                    with patch.object(PDFHandler, 'create_from_images') as create_from_images_mock:
                        with patch.object(FileHandler, 'delete_many') as delete_many_files_mock:
                            with patch('src.controllers.slice.Image.open') as image_open_mock:
                                os_mock.getenv = MagicMock()
                                os_mock.path.exists = MagicMock()
                                os_mock.mkdir = MagicMock()
                                os_mock.getenv.return_value = 'test'
                                os_mock.path.exists.return_value = False
                                pdf_file_mock = MagicMock()
                                pdf_file_mock.read = MagicMock()
                                future_read_mock_result = Future()
                                future_read_mock_result.set_result('pdf content')
                                pdf_file_mock.read.return_value = future_read_mock_result

                                extract_pages_to_images_from_bytes_mock.return_value = ['image 1', 'image 2']

                                result = await SliceController.post(pdf_file_mock)

                                os_mock.mkdir.assert_called_once_with('test/.slicepdf')
                                extract_pages_to_images_from_bytes_mock.assert_called_once_with('pdf content')
                                self.assertEqual(image_open_mock.call_count, 2)
                                self.assertEqual(halve_image_mock.call_count, 2)
                                create_from_images_mock.assert_called_once()
                                delete_many_files_mock.assert_called_once()
                                self.assertIsInstance(result, FileResponse)
if __name__ == '__main__':
    main()

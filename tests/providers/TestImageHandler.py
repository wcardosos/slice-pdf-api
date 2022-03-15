from unittest import TestCase, main
from unittest.mock import patch, MagicMock
from src.providers.image_handler import ImageHandler


class TestImageHandler(TestCase):
    def test_should_crop_image(self):
        image_handler = ImageHandler()
        image_mock = MagicMock()
        image_cropped_mock = MagicMock()
        image_cropped_mock.save = MagicMock()
        image_mock.crop = MagicMock()
        image_mock.crop.return_value = image_cropped_mock

        image_handler.crop(
            (1, 1, 1, 1),
            'new file',
            image_mock
        )

        image_mock.crop.assert_called_once_with((1,1,1,1))
        image_cropped_mock.save.assert_called_once_with('new file')
    
    def test_should_halve_image(self):
        image_handler = ImageHandler()
        image_mock = MagicMock()
        image_mock.size = (1000, 1000)
        image_handler.crop = MagicMock()

        expected_first_call_args = (
            (0, 0, 500, 1000),
            'test 1',
            image_mock
        ),
        expected_second_call_args = (
            (500, 0, 1000, 1000),
            'test 2',
            image_mock
        ),

        image_handler.halve(
            image_mock,
            'test 1',
            'test 2'
        )

        self.assertEqual(image_handler.crop.call_count, 2)
        self.assertEqual(image_handler.crop.call_args_list[0], expected_first_call_args)
        self.assertEqual(image_handler.crop.call_args_list[1], expected_second_call_args)


if __name__ == '__main__':
    main()

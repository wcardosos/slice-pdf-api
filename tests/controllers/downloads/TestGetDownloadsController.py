import json
from unittest import TestCase, main
from unittest.mock import patch, MagicMock
from src.controllers.downloads import DownloadsController


class TestGetDownloadsCountController(TestCase):
    def test_should_get_downloads_count(self):
        '''
            Should return not implemented status
        '''
        with patch('src.controllers.downloads.Response') as response_mock:
            DownloadsController.get()

            response_mock.assert_called_once_with(
                content=json.dumps({ 'message': 'This feature will be implemented soon' }),
                status_code=501
            )


if __name__ == '__main__':
    main()

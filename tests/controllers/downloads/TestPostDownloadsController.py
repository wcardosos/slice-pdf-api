import json
from unittest import TestCase, main
from unittest.mock import patch, MagicMock
from src.controllers.downloads import DownloadsController


class TestPostDownloadsController(TestCase):
    def test_should_create_download_log(self):
        '''
            Should return not implemented status
        '''
        with patch('src.controllers.downloads.Response') as response_mock:
            DownloadsController.post('pdf')

            response_mock.assert_called_once_with(
                content=json.dumps({ 'message': 'This feature will be implemented soon' }),
                status_code=501
            )

if __name__ == '__main__':
    main()

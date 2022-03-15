from unittest import TestCase, main
from unittest.mock import MagicMock, patch
from src.providers.logger import Logger


class TestLogger(TestCase):
    def setUp(self) -> None:
        self.logger = Logger('service')
    
    def test_should_print_info(self):
        with patch('src.providers.logger.datetime') as datetime_mock:
            datetime_mock.now = MagicMock()
            datetime_mock.now.return_value = 'date'
            with patch('builtins.print') as print_mock:
                with patch('src.providers.logger.colored') as colored_mock:
                    self.logger.info('log')

                    print_mock.assert_called_once()
                    colored_mock.assert_called_once_with('date [service] - log', 'white')
    
    def test_should_print_warning(self):
        with patch('src.providers.logger.datetime') as datetime_mock:
            datetime_mock.now = MagicMock()
            datetime_mock.now.return_value = 'date'
            with patch('builtins.print') as print_mock:
                with patch('src.providers.logger.colored') as colored_mock:
                    self.logger.warn('log')

                    print_mock.assert_called_once()
                    colored_mock.assert_called_once_with('date [service] - log', 'yellow')
    
    def test_should_print_error(self):
        with patch('src.providers.logger.datetime') as datetime_mock:
            datetime_mock.now = MagicMock()
            datetime_mock.now.return_value = 'date'
            with patch('builtins.print') as print_mock:
                with patch('src.providers.logger.colored') as colored_mock:
                    self.logger.error('log')

                    print_mock.assert_called_once()
                    colored_mock.assert_called_once_with('date [service] - log', 'red')

if __name__ == '__main__':
    main()

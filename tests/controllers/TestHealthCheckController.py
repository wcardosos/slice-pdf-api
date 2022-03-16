import json
from unittest import TestCase, main
from unittest.mock import patch
from src.controllers.health_check import HealthCheckController


class TestHealthCheckController(TestCase):
    def test_get_should_returns_response(self):
        with patch('src.controllers.health_check.Response') as response_mock:
            HealthCheckController.get()

            response_mock.assert_called_once_with(content=json.dumps({}), status_code=200)

if __name__ == '__main__':
    main()

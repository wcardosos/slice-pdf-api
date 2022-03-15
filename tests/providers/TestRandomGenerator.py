from unittest import TestCase, main
from unittest.mock import patch, MagicMock
from src.providers.random_generator import RandomGenerator


class TestRandomGenerator(TestCase):
    def test_should_return_random_str(self):
        with patch('src.providers.random_generator.uuid4') as uuid_mock:
            uuid_mock.return_value = 'random'

            result = RandomGenerator.generate_str()

            self.assertEqual(result, 'random')

if __name__ == '__main__':
    main()
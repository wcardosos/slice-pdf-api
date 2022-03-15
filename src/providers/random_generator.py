from uuid import uuid4


class RandomGenerator:
    '''
        Class to generate random values.
    '''

    @staticmethod
    def generate_str() -> str:
        '''
            Generates a random string.
        '''
        random_str = str(uuid4())

        return random_str

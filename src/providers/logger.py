from datetime import datetime
from termcolor import colored
from typing import Any, Callable


def log_message_decorator(log_method: Callable) -> str:
    def compose_log_message(ref: Any, message: str):
        now = Logger.get_now()
        log_message = f'{now} [{ref.service}] - {message}'

        return log_method(ref, log_message)

    return compose_log_message

class Logger:
    '''
        Class to log infos, warnings and errors.
    '''
    def __init__(self, service: str) -> None:
        self.service = service

    @classmethod
    def get_now(cls) -> str:
        '''
            Return the actual timestamp.
        '''
        return str(datetime.now())
    

    @log_message_decorator
    def info(self, message: str) -> None:
        '''
            Logs a info.
        '''
        print(colored(message, 'white'))

    @log_message_decorator
    def warn(self, message: str) -> None:
        '''
            Logs a warning.
        '''
        print(colored(message, 'yellow'))

    @log_message_decorator
    def error(self, message: str) -> None:
        '''
            Logs a error.
        '''
        print(colored(message, 'red'))

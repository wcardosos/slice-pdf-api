import os
from abc import ABC
from firebase_admin import (
    _apps as firebase_apps,
    credentials,
    initialize_app,
    firestore
)


FIREBASE_CREDENTIALS_FILEPATH = os.getenv('FIREBASE_CREDENTIALS_FILEPATH')


class BaseFirestoreRepository(ABC):
    '''
        Abstract class to automated Firebase apps assignment.
    '''
    def __init__(self):
        if not firebase_apps.get('[DEFAULT]'):
            cred = credentials.Certificate(FIREBASE_CREDENTIALS_FILEPATH)
            self.app = initialize_app(cred)
        else:
            self.app = firebase_apps['[DEFAULT]']

        self.db = firestore.client(self.app)  # pylint: disable=invalid-name

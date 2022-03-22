import os
from src.errors.firestore.document_not_found_exception import (
    DocumentNotFoundException
)
from src.repositories.Firestore.base_firestore_repository import (
    BaseFirestoreRepository
)


FIREBASE_COLLECTION = os.getenv('FIREBASE_COLLECTION')


class DownloadsCountFirestoreRepository(BaseFirestoreRepository):
    '''
        Class to communicate with Firestore downloads collection.
    '''
    def get(self) -> int:
        '''
            Get the downloads count.
        '''
        doc_ref = self.db.collection(FIREBASE_COLLECTION).document('downloads')

        downloads = doc_ref.get()

        if not downloads.exists:
            raise DocumentNotFoundException()

        count = downloads.to_dict()['count']

        return count

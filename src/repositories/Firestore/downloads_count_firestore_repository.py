import os
from typing import Any
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
    def get_document(self) -> Any:
        '''
             Get the document reference of downloads count.
        '''
        doc_ref = self.db.collection(FIREBASE_COLLECTION).document('downloads')

        return doc_ref

    def get_downloads_count_data(self) -> Any:
        '''
            Get the downloads count data.
        '''
        doc_ref = self.get_document()
        downloads_count_data = doc_ref.get()

        if not downloads_count_data.exists:
            raise DocumentNotFoundException()

        return downloads_count_data

    def get(self) -> int:
        '''
            Get the downloads count.
        '''
        downloads_count_data = self.get_downloads_count_data()

        count = downloads_count_data.to_dict()['count']

        return count

    def update(self) -> None:
        '''
            Update the downloads count.
        '''
        actual_count = self.get()

        new_count = actual_count + 1

        doc_ref = self.get_document()

        doc_ref.update({'count': new_count})

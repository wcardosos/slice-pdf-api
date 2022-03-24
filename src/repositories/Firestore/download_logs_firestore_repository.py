import os
from typing import Any
from src.entities.DownloadLog import DownloadLog
from src.errors.firestore.document_not_found_exception import (
    DocumentNotFoundException
)
from src.repositories.Firestore.base_firestore_repository import (
    BaseFirestoreRepository
)


FIREBASE_COLLECTION = os.getenv('FIREBASE_COLLECTION')


class DownloadLogsFirestoreRepository(BaseFirestoreRepository):
    '''
        Class to communicate with Firestore downloads collection.
    '''
    def get_collection(self) -> Any:
        '''
             Get the document reference of downloads count.
        '''
        collection = self.db.collection(FIREBASE_COLLECTION)

        return collection
    
    def add_log(self, log: DownloadLog) -> None:
        collection = self.get_collection()

        collection.add(log.to_dict())
    
    def get_downloads_count(self) -> int:
        collection = self.get_collection()

        snapshot = collection.get()

        downloads_count = len(snapshot)

        return downloads_count

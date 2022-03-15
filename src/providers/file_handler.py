import os
from src.errors.files.file_not_found_exception import FileNotFoundException


class FileHandler:
    '''
        Class to handle files in the system.
    '''

    @staticmethod
    def delete(filepath: str) -> None:
        if not os.path.exists(filepath):
            raise FileNotFoundException(filepath)
        
        os.remove(filepath)
    
    @staticmethod
    def delete_many(files_list: list) -> None:
        for file in files_list:
            FileHandler.delete(file)

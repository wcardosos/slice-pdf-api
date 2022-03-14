from os.path import exists as file_exists
from pdf2image import convert_from_path
from src.errors.pdf.pdf_file_not_found_exception import (
    PDFFileNotFoundException
)


class PDFHandler:
    '''
        Class to handler PDF files.
    '''
    @staticmethod
    def extract_pages_to_images(filepath: str) -> None:
        '''
            Extract PDF's pages as images and save it.
        '''
        if not file_exists(filepath):
            raise PDFFileNotFoundException()

        pages = convert_from_path(filepath)

        for index, page in enumerate(pages):
            page.save(f'page{index + 1}.jpg', 'JPEG')

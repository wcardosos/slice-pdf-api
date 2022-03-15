# pylint: disable=import-error
from os.path import exists as file_exists
from pdf2image import convert_from_path
from fpdf import FPDF
from src.errors.pdf.pdf_file_not_found_exception import (
    PDFFileNotFoundException
)


class PDFHandler:
    '''
        Class to handler PDF files.
    '''

    @staticmethod
    def extract_pages_to_images(filepath: str) -> list:
        '''
            Extract PDF's pages as images and save it.
        '''
        if not file_exists(filepath):
            raise PDFFileNotFoundException()

        pages = convert_from_path(filepath)
        filename_list = []

        for index, page in enumerate(pages):
            filename = f'page{index + 1}.jpg' 
            page.save(filename, 'JPEG')
            filename_list.append(filename)
        
        return filename_list
    
    @staticmethod
    def create_from_images(images_list: list, filename: str) -> None:
        pdf = FPDF()

        for image in images_list:
            pdf.add_page()
            pdf.image(image, 0, 0, pdf.w, pdf.h)
        
        pdf.output(filename, 'F')
        pdf.close()

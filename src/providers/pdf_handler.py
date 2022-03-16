# pylint: disable=no-self-use
import os
from pdf2image import convert_from_bytes, convert_from_path
from fpdf import FPDF
from src.errors.pdf.pdf_file_not_found_exception import (
    PDFFileNotFoundException
)
from src.providers.random_generator import RandomGenerator


class PDFHandler:
    '''
        Class to handler PDF files.
    '''
    def __init__(self):
        HOME_FOLDER = os.getenv('HOME')  # pylint: disable=invalid-name
        self.processing_folder = f'{HOME_FOLDER}/.slicepdf'

    def extract_pages_to_images_from_path(self, filepath: str) -> list:
        '''
            Extract PDF's pages as images and save it.
        '''
        # pylint: disable=line-too-long
        if not os.path.exists(filepath):
            raise PDFFileNotFoundException()

        pages = convert_from_path(filepath)
        filename_list = []

        for page in pages:
            filename = f'{self.processing_folder}/{RandomGenerator.generate_str()}.jpg'  # noqa: E501
            page.save(filename, 'JPEG')
            filename_list.append(filename)

        return filename_list

    def extract_pages_to_images_from_bytes(self, file: bytes) -> list:
        '''
            Extract PDF's pages as images and save it.
        '''
        # pylint: disable=line-too-long
        pages = convert_from_bytes(file)
        filename_list = []

        for page in pages:
            filename = f'{self.processing_folder}/{RandomGenerator.generate_str()}.jpg'  # noqa: E501
            page.save(filename, 'JPEG')
            filename_list.append(filename)

        return filename_list

    def create_from_images(self, images_list: list, filename: str) -> None:
        '''
            Create a PDF file from a image list.
        '''
        pdf = FPDF()

        for image in images_list:
            pdf.add_page()
            pdf.image(image, 0, 0, pdf.w, pdf.h)

        pdf.output(filename, 'F')
        pdf.close()

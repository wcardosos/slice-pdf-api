import os
import json
from fastapi import UploadFile, Response
from fastapi.responses import FileResponse
from PIL import Image
from src.providers.file_handler import FileHandler
from src.providers.image_handler import ImageHandler
from src.providers.logger import Logger
from src.providers.pdf_handler import PDFHandler
from src.providers.random_generator import RandomGenerator


class SliceController:
    '''
        Slice PDF files controller.
    '''
    @staticmethod
    async def post(pdf_file: UploadFile):
        '''
            Slice PDF uploaded file and return a new PDF file with
            original pages halved.
        '''
        # pylint: disable=line-too-long,too-many-locals
        home_folder = os.getenv('HOME')
        processing_folder = f'{home_folder}/.slicepdf'

        if not os.path.exists(processing_folder):
            os.mkdir(processing_folder)

        pdf_handler = PDFHandler()
        image_handler = ImageHandler()
        logger = Logger('slice-pdf')
        logger.warn('Starting processing')

        try:
            logger.info('Reading PDF file ...')
            content = await pdf_file.read()
            logger.info('PDF read successfully')

            logger.info('Starting pages extraction')
            extracted_images = pdf_handler.extract_pages_to_images_from_bytes(content)  # noqa: E501
            logger.info(f'{len(extracted_images)} pages extracted')
            logger.info('Pages extraction successfully')

            logger.info('Starting to halve the extracted images')
            halved_images = []
            for extracted_image in extracted_images:
                logger.info(f'Image to halve: {extracted_image}')
                with Image.open(extracted_image) as image:
                    first_half_filename = f'{processing_folder}/{RandomGenerator.generate_str()}.jpg'  # noqa: E501
                    second_half_filename = f'{processing_folder}/{RandomGenerator.generate_str()}.jpg'  # noqa: E501
                    logger.info('Halving image')
                    image_handler.halve(
                        image,
                        first_half_filename,
                        second_half_filename
                    )
                    logger.info('Image halved')
                    halved_images.append(first_half_filename)
                    halved_images.append(second_half_filename)
            logger.info('Images halved successfully')

            logger.info('Starting to create the new PDF file')
            new_pdf_filename = f'{processing_folder}/SLICE-PDF {pdf_file.filename}'  # noqa: E501
            logger.info(f'New PDF filename: {new_pdf_filename}')
            logger.info('Creating PDF file ...')
            pdf_handler.create_from_images(halved_images, new_pdf_filename)
            logger.info('PDF file created successfully')

            logger.info('Starting to remove created images')
            all_images_created = extracted_images + halved_images
            logger.info(f'{len(all_images_created)} images created on processing')  # noqa: E501
            FileHandler.delete_many(all_images_created)
            logger.info('Images removed successfully')

            logger.warn('Processing ended')

            return FileResponse(
                new_pdf_filename,
                headers={
                    'Access-Control-Allow-Origin': '*'
                }
            )
        except Exception as error:  # pylint: disable=(broad-except)
            message = f'An error occurred: {str(error)}'
            logger.error(message)

            return Response(
                content=json.dumps({
                    'message': message
                }),
                status_code=400
            )

from PIL.Image import Image


class ImageHandler:
    '''
        Class to handle images.
    '''

    def crop(
        self,
        measurements: tuple,
        new_filename: str,
        image: Image,
    ) -> None:
        '''
            Crop a image.
        '''
        # pylint: disable=no-self-use

        left, top, right, bottom = measurements
        image_cropped = image.crop((left, top, right, bottom))
        image_cropped.save(new_filename)

    def halve(
        self,
        image: Image,
        first_half_filename: str,
        second_half_filename: str
    ) -> None:
        '''
            Halve a image.
        '''
        image_width, image_height = image.size
        half_width = int(image_width / 2)

        self.crop(
            (0, 0, half_width, image_height),
            first_half_filename,
            image
        )

        self.crop(
            (half_width, 0, image_width, image_height),
            second_half_filename,
            image
        )

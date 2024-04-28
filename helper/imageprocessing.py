from helper.base64toimage import Base64ToNumpy
import cv2
import numpy as np

class ImageProcessor():

    def __init__(self, base64):
        self.base64 = base64

    def prepareImage(self, x=28, y=28):
        try:
            data = Base64ToNumpy(self.base64)
            image_data = data.b64tonumpy()
            image_data = np.squeeze(image_data)

            image_data = cv2.cvtColor(image_data, cv2.COLOR_RGB2GRAY)
            image_data = cv2.blur(image_data, (2, 2))
            image_data = cv2.resize(image_data, (x, y), cv2.INTER_AREA)

            image_data = 255 - image_data

            image_data = image_data / 255

            image_data = (np.expand_dims(image_data, 0))

            return image_data
        except Exception as e:
            raise
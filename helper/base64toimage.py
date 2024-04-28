import io
import base64
import numpy as np
from PIL import Image

class Base64ToNumpy:
	
	def __init__(self, base64):
		self.base64 = base64

	def b64tonumpy(self):
		try:
			image = base64.decodebytes(self.base64)
			image = np.array([Image.open(io.BytesIO(image))])
			return image
		except Exception as e:
			raise
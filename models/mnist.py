from tensorflow.keras.models import load_model
import numpy as np

class MNIST:
    def __init__(self):
        self.model = load_model('models/mnist.keras')
    
    def identify(self, image):
        predictions = self.model.predict(image)
        return np.argmax(predictions)
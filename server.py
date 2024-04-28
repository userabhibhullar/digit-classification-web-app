from helper.imageprocessing import ImageProcessor
from models.mnist import MNIST
from flask import Flask, request, json
from werkzeug.exceptions import MethodNotAllowed

app = Flask(__name__)
model = MNIST()

@app.route('/')
def home():
    return app.send_static_file('index.html')

@app.route('/api/mnist', methods=['POST'])
def handle_api():
    data = request.data
    processor = ImageProcessor(data)
    image = processor.prepareImage()
    prediction = model.identify(image)
    response = json.jsonify({'prediction': str(prediction)})
    return response

@app.errorhandler(MethodNotAllowed)
def handle_bad_request(e):
    return app.send_static_file('405.html')
    

if __name__ == '__main__':
    app.run()
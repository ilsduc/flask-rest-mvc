from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from configparser import ConfigParser

from controller import *

app = Flask(__name__)
CORS(app)

# Get all demos
@app.route('/demos', methods=['GET'])
def get_demos():
    return DemoController.getList()

# Create demo
@app.route('/demos', methods=['POST'])
def post_demos():
    return DemoController.create(request.get_json(), ['name']) # require name

# Get one demo
@app.route('/demos/<id>', methods=['GET'])
def get_demo(id):
    return DemoController.getItem(id)

# Update demo
@app.route('/demos/<id>', methods=['PUT'])
def put_demo(id):
    return DemoController.update(id, request.json)

# Delete demo
@app.route('/demos/<id>', methods=['DELETE'])
def delete_demo(id):
    return DemoController.delete(id)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    
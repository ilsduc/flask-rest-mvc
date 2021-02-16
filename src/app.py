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

########################
## Constraints routes ##
########################
# Get all constraints filenames
@app.route('/constraints', methods=['GET'])
def get_constraints():
    return ConstraintController.getList()
# Upload file
@app.route('/constraints', methods=['POST'])
def post_constraint():
    print('request.files', request.files)
    return ConstraintController.create(request.files)
# Get constraint file content
@app.route('/constraints/<name>', methods=['GET'])
def get_constraint(name):
    return ConstraintController.get_one(name)
# Update constraint file
@app.route('/constraints/<name>', methods=['PUT'])
def put_constraint(name):
    return ConstraintController.replace(name, request.files)
@app.route('/constraints/<name>', methods=['DELETE'])
# Delete constraint file
def delete_constraint(name):
    return ConstraintController.delete(name)
# Download constraint file
@app.route('/constraints/<name>/download', methods=['GET'])
def download_constraint(name):
    return ConstraintController.download_file(name)

####################
# Optimizer routes #
####################
# Run Optimizer
@app.route('/optimize', methods=['POST'])
def optimize():
    return OptimizerController.optimize(request.files)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    
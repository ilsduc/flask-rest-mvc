from flask import jsonify

# Expose some good methods to handle API Response
# Let's create some as your needs
class APIController:

    @classmethod
    def success (that, res, code=200):
        if res is not None:
            return jsonify(res), code

        return that.error('Error')

    @classmethod
    def error (that, message='Server error occured', code=400):
        return jsonify({'message': message}), code
    
    @classmethod
    def respond (that, res, error):
        if error:
            return that.error(error.message, error.status_code)
        
        return that.success(res)

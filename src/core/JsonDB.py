import json

class JsonDB:
    @classmethod
    def write (that, file_name, data):
        try:
            with open(file_name, 'w') as outfile:
                json.dump(data, outfile)
                return True
        except:
            return False

    @classmethod
    def read (that, file_name):
        try:
            with open(file_name, 'r') as json_file:
                data = json.load(json_file)
                return data
        except:
            return None
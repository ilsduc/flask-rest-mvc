from core.JsonSerializable import JsonSerializable
import json
import os.path
from os import path

class JSONFileModel(JsonSerializable):

    name = None
    root_path = None
    content = None
    file_path = None

    def __init__ (self, root_path, name):
        self.root_path = root_path
        self.name = name.replace('.json', '')
        self.file_path = '{root_path}/{name}.json'.format(
            root_path=self.root_path,
            name=self.name,
        )
        try :
            with open(self.file_path) as json_file:
                self.content = json.load(json_file)
        except Exception as e:
            print('Error when opening file', e)
            return
    
    def get_property (self, prop):
        return self.get_recursively(self.get_content(), prop)
            
    def get_recursively (self, obj, prop):
        if prop.find('.') >= 0:
            props = prop.split('.')
            if len(props) > 1:
                look_for = props[0]
                if look_for in obj:
                    return self.get_recursively(obj.get(look_for), '.'.join(props[1:]))
                else:
                    return None
            else:
                return obj.get(props[0]) if props[0] in obj else None
        else:
            return obj.get(prop) if prop in obj else None

    def is_valid (self):
        return path.exists(self.get_file_path())

    def get_name (self):
        return self.name
    
    def get_file_name (self):
        return '{name}.json'.format(name=self.name)

    def get_content (self):
        return self.content

    def get_root_path (self):
        return self.root_path

    def get_file_path (self):
        return self.file_path
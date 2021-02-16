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
        self.name = name
        self.file_path = '{root_path}/{name}.json'.format(
            root_path=self.root_path,
            name=self.name,
        )
        try :
            with open(self.file_path) as json_file:
                self.content = json.load(json_file)
        except:
            return
    
    # def get_property (self, prop):
    #     return self._get_item(self.get_content(), prop)
            
    # def _get_item (self, obj, prop):
    #     if prop.find('.') >= 0:
    #         props = prop.split('.')
    #         if len(props) > 1:
    #             look_for = props[0]
    #             if obj.has_key(look_for):
    #                 return self._get_item(obj.get(look_for), '.'.join(props[1:]))
    #             else:
    #                 return None
    #         else:
    #             return obj.get(props[0]) if obj.has_key(props[0]) else None
    #     else
    #         return obj.get(prop) if obj.has_key(prop) else None

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
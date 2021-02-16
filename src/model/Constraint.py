from model.JSONFileModel import JSONFileModel

class Constraint(JSONFileModel):
    
    root_path = 'datas/constraints'

    def __init__ (self, name):
        super().__init__(self.root_path, name)
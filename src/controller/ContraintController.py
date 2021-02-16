import os
from flask import send_file
from controller.APIController import APIController
from service.DirectoryParser import DirectoryParser
from model.Constraint import Constraint
from werkzeug.utils import secure_filename
from service.FileUploader import FileUploader

def format_constraint (constraint_name):
    constraint = Constraint(constraint_name)
    content = constraint.get_content()
    return {
        'name': constraint.get_name(),
        'content': content,
    }

class ConstraintController(APIController):

    @classmethod
    def getList(self):
        constraints = DirectoryParser.read_directory('datas/constraints')
        res = []
        for constraint_name in constraints:
            res.append(format_constraint(constraint_name))
        return self.success(res)
        
    @classmethod
    def get_one(self, name):
        constraint = Constraint(name)
        if not constraint.is_valid():
            return self.error('Item not found')
        return self.success(constraint.get_content())
        
    @classmethod
    def download_file(self, name):
        constraint = Constraint(name)
        return send_file(constraint.get_file_path(),  as_attachment=True)
        
    @classmethod
    def create(self, files):
        # Check if file exists
        file = FileUploader.ensure_file(files)
        if file is None:
            return self.error('Bad request')
            
        constraint_name = file.filename.replace('.json', '')
        constraint = Constraint(constraint_name)
        if constraint.is_valid():
            return self.error('Already exists')

        filename = FileUploader.single_upload(path='datas/constraints', file=file, allowed_extensions={'json'})
        
        constraint = Constraint(constraint_name)
        return self.success(constraint.get_file_name())


    @classmethod
    def replace(self, name, files):
        file = FileUploader.ensure_file(files)
        constraint_name = file.filename.replace('.json', '')
        if file is None:
            return self.error('Bad request')

        constraint = Constraint(name)
        if not constraint.is_valid():
            return self.error('Bad request')

        if not constraint.get_name() == constraint_name:
            return self.error('The filename should be <constraint_name>.json')
        
        filename = FileUploader.single_upload(path='datas/constraints', file=file, allowed_extensions={'json'}, rename='{name}.json'.format(name=name))
        
        return self.success(constraint.get_content())
            
    @classmethod
    def delete(self, name):
        constraint = Constraint(name)
        if not constraint.is_valid():
            return self.error('Bad request')

        os.remove(constraint.get_file_path())
        
        return self.success(constraint.get_name())
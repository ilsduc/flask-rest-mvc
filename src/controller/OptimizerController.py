from controller.APIController import APIController
from service.FileUploader import FileUploader
from service.OptimizerService import OptimizerService
from flask import send_file
from model.Constraint import Constraint

class OptimizerController(APIController):

    @classmethod
    def optimize(self, files):
        
        constraints = DirectoryParser.read_directory('datas/constraints')
        constraintObjects = []
        for constraint_name in constraints:
            constraintObject = Constraint(constraint_name)
            constraintObjects.append(constraintObject)
        
        """
            constraintObject contains an array of 
            Constraint object --> constraintObjects[0].get_content() // dict
        """

        xls_file = FileUploader.ensure_file(files)
        print(xls_file)

        # Do something with the xls files and constraints filenames
        result_xls_file = OptimizerService.process(xls_file, constraintObjects)
        
        # send for download
        return send_file(result_xls_file, as_attachment=True)

        
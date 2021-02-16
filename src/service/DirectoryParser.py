import os

class DirectoryParser:

    @classmethod
    def read_directory (self, dir_name):
        obj = os.scandir(dir_name) 
        files = []
        for entry in obj : 
            if entry.is_file(): 
                files.append(entry.name)
        
        obj.close()

        return files

import os
from werkzeug.utils import secure_filename

class FileUploader:

    @classmethod
    def single_upload (self, path, file, allowed_extensions = None, rename = None):
        if file and self.allowed_file(file.filename, allowed_extensions):
            filename = secure_filename(file.filename if rename is None else rename)
            file.save(os.path.join(path, filename))
            return filename
        
    @classmethod
    def allowed_file(self, filename, allowed_extensions):
        return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in allowed_extensions

    @classmethod
    def ensure_file (self, files):
        if 'file' not in files:
            return None
        file = files['file']
        if file.filename == '':
            return None

        return file
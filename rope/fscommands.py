import os
import shutil

try:
    import pysvn
except ImportError:
    pass


def create_fscommands(project):
    root = project.get_root_folder()
    if False and 'pysvn' in globals() and root.has_child('.svn'):
        return SubversionCommands()
    return FileSystemCommands()


class FileSystemCommands(object):
    
    def create_file(self, path):
        open(path, 'w').close()
    
    def create_folder(self, path):
        os.mkdir(path)
    
    def move(self, path, new_location):
        shutil.move(path, new_location)
    
    def remove(self, path):
        if os.path.isfile(path):
            os.remove(path)
        else:
            shutil.rmtree(path)


class SubversionCommands(object):
    
    def __init__(self):
        self.normal_actions = FileSystemCommands()
        self.client = pysvn.Client()
    
    def create_file(self, path):
        self.normal_actions.create_file(path)
        self.client.add(path)
    
    def create_folder(self, path):
        self.normal_actions.create_folder(path)
        self.client.add(path)
    
    def move(self, path, new_location):
        self.client.move(path, new_location, force=True)
    
    def remove(self, path):
        self.client.remove(path)

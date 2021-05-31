from datetime import datetime


class FileCSV(object):
    def __init__(self, nameProject: str, file):
        self.nameProject = nameProject
        self.file = file
        self.date = datetime.datetime.now()

from INFRA import db
from repo.modelProject import fileCSV


class Repository(object):
    def __init__(self):
        self.db = db
    @staticmethod
    def saveModelProject( modelProject: fileCSV):
        try:
            if not db.name_model.find({"nameProject": modelProject.nameProject}):
                db.name_model.insert_one(modelProject)

            # pending catch the exception
        finally:
            None
    @staticmethod
    def getModelProjectByName( nameProject: str):
        try:
            return db.name_model.find({"nameProject": nameProject})
        finally:
            None
    @staticmethod
    def deleteModelProjectByName( nameProject: str):
        db.name_model.delete_one({"nameProject": nameProject})
    @staticmethod
    def getByQuery(dictQuery: dict):        # make it able to accept regex
        return db.name_model.find(dictQuery)
    @staticmethod
    def saveManyModelProjects(listModels: list):
        db.name_model.insert_many(listModels)   

from dao.repo import Repository
from repo.modelProject import FileCSV


class ServiceModelProject(object):
    def saveService(self,nameProject,file):
        modelToSave = FileCSV(nameProject,file)
        Repository.saveModelProject(modelToSave)
        return True
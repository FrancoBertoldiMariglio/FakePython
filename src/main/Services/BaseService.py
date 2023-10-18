from abc import ABC, abstractmethod

class BaseService(ABC):

    def __init__(self, baseRepository):
        self.baseRepository = baseRepository
    @abstractmethod
    def findAll(self):
        pass

    @abstractmethod
    def findOne(self, id):
        pass

    @abstractmethod
    def save(self, entity):
        pass

    @abstractmethod
    def update(self, entity, id):
        pass

    @abstractmethod
    def delete(self, id):
        pass
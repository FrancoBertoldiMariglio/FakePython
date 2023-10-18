from .BaseService import BaseService

class BaseServiceImplement(BaseService):

    def __int__(self, baseRepository):
        self.baseRepository = baseRepository

    def findAll(self):
        try:
            return self.baseRepository.findAll()
        except Exception as e:
            raise Exception(str(e))

    def findOne(self, id):
        try:
            return self.baseRepository.findOne(id)
        except Exception as e:
            raise Exception(str(e))

    def save(self, entity):
        try:
            return self.baseRepository.save(entity)
        except Exception as e:
            raise Exception(str(e))

    def update(self, entity, id):
        try:
            optEntity = self.baseRepository.findOne(id)
            if optEntity != None:
                entityUpdate = self.baseRepository.save(entity)
                return entityUpdate
        except Exception as e:
            raise Exception(str(e))


    def delete(self, id):
        try:
            if self.baseRepository.findOne(id) != None:
                self.baseRepository.deleteById(id)
                return True
            else:
                raise Exception()
        except Exception as e:
            raise Exception(str(e))
from .BaseServiceImp import BaseServiceImplement

class DomicilioServiceImp(BaseServiceImplement):

    def __init__(self, domicilioRepository):
        super().__init__(domicilioRepository)
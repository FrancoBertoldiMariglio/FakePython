from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class BaseRepository:
    def __init__(self, database_url):
        self.engine = create_engine(database_url)
        self.Session = sessionmaker(bind=self.engine)

    def save(self, objeto):
        session = self.Session()
        session.add(objeto)
        session.commit()
        session.close()

    def findById(self, entidad, identificador):
        session = self.Session()
        objeto = session.query(entidad).get(identificador)
        session.close()
        return objeto

    def update(self, objeto):
        session = self.Session()
        session.add(objeto)
        session.commit()
        session.close()

    def delete(self, objeto):
        session = self.Session()
        session.delete(objeto)
        session.commit()
        session.close()

    def findAll(self, entidad):
        session = self.Session()
        objetos = session.query(entidad).all()
        session.close()
        return objetos

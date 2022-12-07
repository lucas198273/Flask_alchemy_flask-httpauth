from sqlalchemy import create_engine,Column,Integer,String, ForeignKey
#Bibliotecas cria tabela,coluna, tipo : inteiro e string
from sqlalchemy.orm import scoped_session,sessionmaker, relationship
# criação com escopo, e criador de sessão
from sqlalchemy.ext.declarative import declarative_base
#Base declarativa




#cria banco e estabelece nome
engine = create_engine('sqlite:///atividades.db', convert_unicode=True)  #erro 
db_session = scoped_session(sessionmaker(autocommit=True,
                                         bind = engine))
Base = declarative_base()
Base.query = db_session.query_property()

class Pessoas(Base):
    __tablename__= "pessoas"
    id = Column(Integer,primary_Key=True)
    #index nao ativado
    nome = Column(String(40),index=True)
    idade = Column(Integer)

    def __repr__(self):
        return '<Pessoa {}>'.format(self.nome)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

class Atividades(Base):
    __tablename__ = 'atividades'
    id = Column(Integer,primary_key=True)
    nome= Column(String(40))
    pessoa_id= Column(Integer,ForeignKey('pessoas.id'))
    pessoa = relationship("Pessoas")

    def __repr__(self):
        return"<Atividades {}>".format(self.nome)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

class Usuarios(Base):
    __tablename__='usuarios'
    id = Column(Integer,primary_key=True)
    login = Column(String(15), unique=True)
    senha = Column(String(15))

    def __repr__(self):
        return'Usuarios {}'.format(self.login)
    def save(self):
        db_session.add(self) #adiciona
        db_session.commit() #Atualiza
    def delete(self):
        db_session.delete(self)
        db_session.commit()

def init_db():
    Base.metadata.create_all(bind=engine)


if __name__ =='__main__':
   init_db()
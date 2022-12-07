from models import Pessoas, db_session, Usuarios
from flask_httpauth import HTTPBasicAuth                                          ## Este arquivo possibilita inserir,excluir, consultar, alterar dados e usuarios


def inserir_pessoas():
    pessoa = Pessoas(nome='Rafael',idade=19)
    print(pessoa)
    pessoa.save()

def consulta():
    pessoa = Pessoas.query.all()
    pessoa= Pessoas.query.filter_by(nome='Rafael').first()
    print(pessoa.idade)

def altera():
    pessoa= Pessoas.query.filter_by(nome="Rafael").first()
    pessoa.idade = 21
    pessoa.save

def excluir():
    pessoa = Pessoas.query.filter_by(nome="Rafael").first()
    pessoa.delete()

def insere_usuario(login,senha):
    usuario = Usuarios(login=login,senha=senha)
    usuario.save()

def consulta_todos_usuarios ():
    usuarios = Usuarios.query.all()
    print(usuarios)


if __name__ == '__main__':
    consulta_todos_usuarios()
    #inserir_pessoas()
    #consulta()
    #altera()
    #excluir

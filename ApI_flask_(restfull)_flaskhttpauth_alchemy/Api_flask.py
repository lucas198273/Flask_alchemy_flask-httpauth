from flask import Flask, request
from flask_restful import Resource,Api
from models import Pessoas,Atividades,Usuarios            # Api é utilizada para pegar informações do banco de dados criado no arquivo models.py enviando para uma pagina  
from flask_httpauth import HTTPBasicAuth                  # Utilizando o flaskhttpauth eu inseri uma requisição basica de login e senha nas classes Pessoas e Lista_pessoas

auth = HTTPBasicAuth()
app = Flask(__name__)
api= Api(app)


usuarios = {
    "Diogo": '7139',
    "Gustavo":"4758",
    "marcio": "2536",
    "Erik": "7436",
    "Douglas": "5879"
}

@auth.verify_password
def verificação(login,senha):
    if not(login,senha):
        return False
    return Usuarios.query.filter_by(login=login, senhas=senha).first()


class Pessoa(Resource):
    @auth.login_required
    def get(self,nome):                #" .first()" é utilizado para acessar o objeto nome
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        try:
            resource = {
            "nome": pessoa.nome,
            "idade": pessoa.idade,
            "id":pessoa.id
        }
        except AttributeError:
             response ={
              "status": "Error",
              "Menssagem": "Pessoa nao encontrada"
             }
        return response

    def put(self,nome):

        pessoa = Pessoas.query.filter_by(nome=nome).first()
        dados = request.json
        # Vai alterar
        if "nome" in dados:
            pessoa.nome = dados["nome"]
        if "idade" in dados:
            pessoa.idade = dados['idade']
        pessoa.save()
        response = {
            'id':pessoa.id,
            'nome': pessoa.nome,
            'idade': pessoa.idade
        }

        return response

    def delete(self,nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        menssagem = 'pessoa {} excluida com sucesso'.format(pessoa.nome)
        pessoa.delete()
        return {"status":'sucesso','mensagem':'pessoa'}




class Lista_pessoas(Resource):
    @auth.login_required
    def get(self):
        pessoas = Pessoas.query.all()
        response = [{"id":i.id,"nome":i.nome,"idade":i.idade}for i in pessoas] #for_line
        return response

    def post(self):

        dados = request.json
        pessoa = Pessoas(nome=dados["nome"] ,idade=dados['idade'])
        pessoa.save()
        response = {
            "id":pessoa.id,
            "nome":pessoa.nome,
            "idade":pessoa.idade
            }
        return response


class Lista_atividades(Resource):
    def get(self):
        atividades = Atividades.query.all()
        response = [{"id":i.id, 'nome': i.nome, 'pessoa': i.pessoa.nome}for i in atividades]
        return  response

    def post(self):
        dados = request.json
        pessoa = Pessoa.query.filter_by(nome=dados["pessoa"]).first()
        atividades = Atividades(nome=dados['nome'], pessoa=pessoa)
        atividades.save()
        response = {
            'pessoa': atividades.pessoa.nome,
            'nome':atividades.nome,
            'id':atividades.id
            }
        return response


api.add_resource(Pessoa,"/pessoa/<string:nome>/")
api.add_resource(Lista_pessoas,'/pessoa/')
api.add_resource(Lista_atividades,"/atividades/")






if __name__ == '__main__':
    app.run(debug=True)

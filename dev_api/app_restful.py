from flask import Flask, request
from flask_restful import Resource, Api
from habilidades import Habilidades, ListaHabilidades
import json

desenvolvedores =[{

        'id': '0',
        'nome': 'Alessandro',
        'habilidades': ['.Net, c#', 'SQL']
    },

    {
        'id': '1',
        'nome': 'Maykon',
        'habilidades': ['Java', 'postgresSQL']
     },
    {
        'id': '2',
        'nome': 'Sivio',
        'habilidades': ['JavaScript', 'MongoDB']
     },
    {
        'id': '3',
        'nome': 'João',
         'habilidades': ['Python', 'oracle']}
]




app = Flask(__name__)
api = Api(app)

class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desenvolvedor com ID {} não existe!!'.format(id)
            response = {'status': 'erro', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Procure o administrador da API'
            response = {'status': 'erro', 'mensagem': mensagem}
        return response

    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados


    def delete(self, id):
        desenvolvedores.pop(id)
        return {'satus': 'sucesso', 'mensagem': 'Registro excluido'}


class ListaDesenvolvedores(Resource):
    def get(self):
        return desenvolvedores

    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return desenvolvedores[posicao]


api.add_resource(Desenvolvedor, '/dev/<int:id>/')
api.add_resource(ListaDesenvolvedores, '/dev/')
api.add_resource(ListaHabilidades, '/habilidades/')


if __name__ == '__main__':
    app.run(debug=True)


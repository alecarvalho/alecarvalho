from flask_restful import Resource, request
import json

lista_habilidades = [{
            'id':'0',
            'habilidade': 'Python'
        },
        {
            'id':'1',
            'habilidade': 'Java'
        },
        {
          'id':'2',
           'habilidade': 'Flask'
        },
        {
            'id':'3',
            'habilidades': 'dotNet'
        }]

class Habilidades(Resource):
    def get(self, id):
        try:
            response = lista_habilidades[id]
        except IndexError:
            mensagem = 'Habilidade com ID {} não existe!!'.format(id)
            response = {'status': 'erro', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Procure o administrador da API'
            response = {'status': 'erro', 'mensagem': mensagem}
        return response

    def put(self, id):
        dados = json.loads(request.data)
        lista_habilidades[id] = dados
        return dados

    def delete(self, id):
        lista_habilidades.pop(id)
        return {'satus': 'sucesso', 'mensagem': 'Registro excluido'}

class ListaHabilidades(Resource):
        def get(self):
            return lista_habilidades

        def post(self):
            dados = json.loads(request.data)
            posicao = len(lista_habilidades)
            dados['id'] = posicao
            lista_habilidades.append(dados)
            return lista_habilidades[posicao]
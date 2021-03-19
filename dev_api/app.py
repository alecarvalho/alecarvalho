from flask import Flask, jsonify, request
import json

app = Flask(__name__)

desenvolvedores =[{
    'nome': 'Alessandro',
        'habilidades': ['.Net, c#', 'SQL']
    },
    {'nome': 'Maykon',
        'habilidades': ['Java', 'postgresSQL']
     },
    {'nome': 'Sivio',
        'habilidades': ['JavaScript', 'MongoDB']
     },
    {'nome': 'João',
         'habilidades': ['Python', 'oracle']}
]
#devolve um desenvolvedor pelo id altera e deleta
@app.route('/dev/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desenvolvedor com ID {} não existe!!'.format(id)
            response = {'status': 'erro', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Procure o administrador da API'
            response = {'status': 'erro', 'mensagem': mensagem}
        return jsonify(response)
    elif request.method =='PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'satus': 'sucesso', 'mensagem': 'Registro excluido'})

#Listar todos e inclusão de desenvolvedores
@app.route('/dev/', methods=['GET', 'POST'])
def lista_desenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return jsonify(desenvolvedores[posicao])
    elif request.method == 'GET':
        return jsonify(desenvolvedores)


if __name__=='__main__':
    app.run()
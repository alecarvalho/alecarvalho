import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('Servidor: Socket Criado com sucesso!!')

host = 'localhost'
port = 5432

s.bind((host, port))
mensagem = 'Servidor: Ola Cliente!!!!'

while 1:
    dados, end = s.recvfrom(4096)
    if dados:
        print('Servidor: enviando mensagem!!')
        s.sendto(dados + (mensagem.encode()), end)



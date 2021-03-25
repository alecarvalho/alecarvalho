import socket


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('Cliente: Socket criado com sucesso!!!')

host = 'localhost'
porta = 5433
mensagem = 'Cliente: Ola servidor de rede!!\n'

try:
    print('Cliente: {} '.format(mensagem))
    s.sendto(mensagem.encode(), (host, int(5432)))

    dados, servidor = s.recvfrom(4096)
    dados = dados.decode()
    print('Cliente: {} '.format(dados))
finally:
    print('Cliente: Fechando a conexão')
    s.close()
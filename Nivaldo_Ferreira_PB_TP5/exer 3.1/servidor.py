import socket
import ssl

def servidor_tls():
    contexto = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    contexto.load_cert_chain(certfile="certificado.pem", keyfile="chave.pem")

    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind(('127.0.0.1', 12345))
    servidor.listen(1)
    print("Aguardando conexao...")

    conexao, endereco = servidor.accept()
    conexao_ssl = contexto.wrap_socket(conexao, server_side=True)
    print(f'Conexao estabelecida com {endereco}')

    dados = conexao_ssl.recv(1024)
    print(f'Recebido: {dados.decode()}')
    conexao_ssl.send(dados)

    conexao_ssl.close()

if __name__ == '__main__':
    servidor_tls()
import socket
import ssl

def cliente_tls():
    contexto = ssl.create_default_context()
    contexto.check_hostname = False
    contexto.verify_mode = ssl.CERT_NONE
    conexao = contexto.wrap_socket(socket.socket(socket.AF_INET), server_hostname='127.0.0.1')
    conexao.connect(('127.0.0.1', 12345))
    
    print("Cliente: conexao estabelecida")
    conexao.send(b"Ola, servidor TLS!")
    
    dados = conexao.recv(1024)
    print(f"Cliente: recebido: {dados.decode()}")
    
    conexao.close()

if __name__ == '__main__':
    cliente_tls()

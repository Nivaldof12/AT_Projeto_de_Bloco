import socket
import ssl

def interceptar_envio(original_send):
    def novo_send(dados, *args, **kwargs):
        print(f"Interceptado (envio): {dados}")
        return original_send(dados, *args, **kwargs)
    return novo_send

def interceptar_recebimento(original_recv):
    def novo_recv(*args, **kwargs):
        dados = original_recv(*args, **kwargs)
        print(f"Interceptado (recebido): {dados}")
        return dados
    return novo_recv

def cliente_tls():
    contexto = ssl.create_default_context()
    contexto.check_hostname = False
    contexto.verify_mode = ssl.CERT_NONE
    
    sock = socket.create_connection(('127.0.0.1', 12345))
    conexao = contexto.wrap_socket(sock, server_hostname='localhost')

    conexao.send = interceptar_envio(conexao.send)
    conexao.recv = interceptar_recebimento(conexao.recv)
    
    mensagem = b"Mensagem segura com logging de pacotes"
    conexao.send(mensagem)
    resposta = conexao.recv(1024)
    
    conexao.close()
    
if __name__ == "__main__":
    cliente_tls()

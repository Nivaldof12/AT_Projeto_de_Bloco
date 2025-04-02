import subprocess
import sys

def varredura_portas(ip):
    comando = ["nmap", "-sV", ip]
    try:
        resultado = subprocess.check_output(comando, stderr=subprocess.STDOUT)
        print(resultado.decode())
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar nmap: {e.output.decode()}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Por favor, forneça um IP para a varredura.")
    else:
        ip = sys.argv[1]
        varredura_portas(ip)

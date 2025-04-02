import time
import sys
from collections import deque

def ler_arquivos(nome_arquivo):
    with open(nome_arquivo, "r") as f:
        return [linha.strip() for linha in f.readlines()]

def medir_acesso(estrutura, posicoes, tipo):
    inicio = time.time()
    memoria = sys.getsizeof(estrutura)

    elementos = {}
    for pos in posicoes:
        if 0 <= pos < len(estrutura):
            if tipo == "hashtable":
                elementos[pos] = estrutura.get(pos)
            else:
                elementos[pos] = estrutura[pos]

    fim = time.time()
    tempo_total = fim - inicio

    return elementos, tempo_total, memoria

arquivos = ler_arquivos("listagem_tp1.txt")

posicoes = [0, 99, 999, 4999, len(arquivos) - 1]

hashtable = {i: arquivos[i] for i in range(len(arquivos))}
pilha = list(arquivos)  
fila = deque(arquivos)  

elementos_ht, tempo_ht, memoria_ht = medir_acesso(hashtable, posicoes, "hashtable")
elementos_pilha, tempo_pilha, memoria_pilha = medir_acesso(pilha, posicoes, "pilha")
elementos_fila, tempo_fila, memoria_fila = medir_acesso(fila, posicoes, "fila")

def imprimir_resultados(nome_estrutura, elementos, tempo, memoria):
    print(f"\n{nome_estrutura}:")
    print(f"Tempo: {tempo:.6f}s | Memória: {memoria} bytes")
    print("Posições e arquivos encontrados:")
    for pos, arquivo in elementos.items():
        print(f"Posição {pos + 1}: {arquivo}")

imprimir_resultados("Hashtable", elementos_ht, tempo_ht, memoria_ht)
imprimir_resultados("Pilha", elementos_pilha, tempo_pilha, memoria_pilha)
imprimir_resultados("Fila", elementos_fila, tempo_fila, memoria_fila)

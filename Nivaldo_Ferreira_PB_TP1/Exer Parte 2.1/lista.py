import time

def ler_arquivos(nome_arquivo):
    with open(nome_arquivo, "r") as f:
        return [linha.strip() for linha in f.readlines()]

def bubble_sort(lista):
    inicio = time.time()
    n = len(lista)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    fim = time.time()
    return lista, fim - inicio

def selection_sort(lista):
    inicio = time.time()
    n = len(lista)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if lista[j] < lista[min_idx]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    fim = time.time()
    return lista, fim - inicio

def insertion_sort(lista):
    inicio = time.time()
    n = len(lista)
    for i in range(1, n):
        chave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = chave
    fim = time.time()
    return lista, fim - inicio

arquivos = ler_arquivos("listagem_tp1.txt")

ordenado_bubble, tempo_bubble = bubble_sort(arquivos.copy())
ordenado_selection, tempo_selection = selection_sort(arquivos.copy())
ordenado_insertion, tempo_insertion = insertion_sort(arquivos.copy())

print("\nLista ordenada pelo Bubble Sort:")
print(ordenado_bubble)
print("\nLista ordenada pelo Selection Sort:")
print(ordenado_selection)
print("\nLista ordenada pelo Insertion Sort:")
print(ordenado_insertion)

print(f"Tempo Bubble Sort: {tempo_bubble:.6f} segundos")
print(f"Tempo Selection Sort: {tempo_selection:.6f} segundos")
print(f"Tempo Insertion Sort: {tempo_insertion:.6f} segundos")
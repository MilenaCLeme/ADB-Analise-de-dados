"""

5. Ordenação de Listas
   - Implemente uma função que receba uma lista de números ou strings e a ordene usando um algoritmo de ordenação de sua escolha (por exemplo, QuickSort, MergeSort). A função deve permitir escolher entre ordem crescente ou decrescente.

"""

print("5. Ordenação de Listas")

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def opcao(escolha, lista):
    # nova_Lista = sorted(lista) - Um jeito de fazer com função sort do python
    nova_lista = quicksort(lista)
    if escolha == 1: 
        print(nova_lista)
    elif escolha == 2:
        print(nova_lista[::-1])
    else:
        print('Opcao errada!')
    

lista_numero = [5, 7, 80, 9, 8, 1, 85, 3]
lista_nome = ['Thais', 'Alex', 'Mariana', 'Milena', 'Dienyffer']  

print("Tipo de ordenação", "01-crescente", "02-decrescente")
opcao_escolhida = int(input("Digite o tipo de ordenação: "))

opcao(opcao_escolhida, lista_numero)
opcao(opcao_escolhida, lista_nome)


"""

5. Ordenação de Listas
Tipo de ordenação 01-crescente 02-decrescente
Digite o tipo de ordenação: 1
[1, 3, 5, 7, 8, 9, 80, 85]
['Alex', 'Dienyffer', 'Mariana', 'Milena', 'Thais']

5. Ordenação de Listas
Tipo de ordenação 01-crescente 02-decrescente
Digite o tipo de ordenação: 2
[85, 80, 9, 8, 7, 5, 3, 1]
['Thais', 'Milena', 'Mariana', 'Dienyffer', 'Alex']

"""
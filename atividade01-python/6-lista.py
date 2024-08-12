'''
6.1. Crie uma lista com os nomes de cinco amigos. Imprima o nome do terceiro
amigo na lista.

'''

lista_de_amigos = ["Romulo", "Keite", "Douglas", "Pedro", "Amanda"]

print(lista_de_amigos[2]) # Douglas

'''
6.2. Adicione um novo nome à lista de amigos e remova o primeiro nome.
Imprima a lista atualizada.
'''

lista_de_amigos.append("Neto") # adicionando nome á listas de amigos
lista_de_amigos.pop(0) # removendo o primeiro da lista 

print(lista_de_amigos) # ['Keite', 'Douglas', 'Pedro', 'Amanda', 'Neto']

'''
6.3. Crie uma lista com as idades dos seus amigos e:
Imprima a idade do amigo mais velho.
Imprima a idade do amigo mais novo.
Calcule e imprima a soma das idades.
'''

lista_de_idade = [35, 80, 45, 60, 40]

def idade_mais_velha(lista):
    x = 0
    for i in range(len(lista)):
        if x < lista[i]:
            x = lista[i]
    return x

def idade_mais_nova(lista):
    x = 0
    for i in range(len(lista)):
        if x == 0 or x > lista[i]:
            x = lista[i]
    return x

def soma_das_idades(lista):
    x = 0
    for i in range(len(lista)):
        x += lista[i] 
    return x

print(idade_mais_velha(lista_de_idade)) # 80

print(idade_mais_nova(lista_de_idade)) # 35

print(soma_das_idades(lista_de_idade)) # 260

"""

Douglas
['Keite', 'Douglas', 'Pedro', 'Amanda', 'Neto']
80
35
260

"""
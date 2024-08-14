"""
11. Gerador de Números Aleatórios
   - Desenvolva uma função que gere uma lista de números aleatórios dentro de um intervalo específico e calcule a média, mediana, e moda dos números gerados.

"""

import statistics
import random

list_numeros = []

def numero_aleatorio(min=1, max=10):
    return random.randint(min, max)

def calcule_media_list(list):
    x = 0
    for i in range(len(list)):
        x += list[i]
    return x / len(list)

def calcular_mediana_list(list):
    return statistics.median(list)


def calcular_moda_list(list):
    return statistics.mode(list)

def menu():
    print("---MENU---", "01-Gerar numero aleatorio dentro de um intervalo específico", "02-Gerar os calculos da média, mediana, e moda dos números gerados ", "03-Exit", sep="\n")
    opcao = int(input("Digite a opção: "))
    
    if opcao == 1:
        numero = int(input("Digite o numero do intervalo entre 1 e: "))
        list_numeros.append(numero_aleatorio(1, numero))
        print("-------------Inserido com sucesso---------------")
        menu()
    elif opcao == 2:
        print(f"A media nos valores é {calcule_media_list(list_numeros)}. A mediana da lista é {calcular_mediana_list(list_numeros)}. A moda da lista é {calcular_moda_list(list_numeros)}")
        print("-----------------------------------------------")
        menu()
    elif numero == 3:
        print("Até a próxima!!")
    else:
        print("Error! tente novamente!", "-------------------------", sep="\n")
        menu()

menu()
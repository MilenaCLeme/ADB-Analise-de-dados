"""
1. Calculadora Científica
   - Escreva uma função que simule uma calculadora científica, capaz de realizar operações básicas como adição, subtração, multiplicação, e divisão, além de funções trigonométricas, exponenciação, e logaritmos.

"""

import math

print("1. Calculadora Científica")

list = []

def adicao(x, y):
    return x+y
# outra forma soma = lambda a,b: a + b

def subtracao(x, y):
    return x-y

def multiplicacao(x,y):
   return x*y

def divisao(x, y):
    if y != 0:
        return x / y
    else:
        return "Erro: Divisão por zero."

def exponenciacao(x,y):
    return x ** y

def logaritmos(x, y):
    return math.log(x/y)

def seno(angulo_graus):
    angulo_radianos = math.radians(angulo_graus)
    return round(math.sin(angulo_radianos), 3)
def cosseno(angulo_graus):
    angulo_radianos = math.radians(angulo_graus)
    return round(math.cos(angulo_radianos), 3)

def tangente(angulo_graus):
    angulo_radianos = math.radians(angulo_graus)
    return round(math.tan(angulo_radianos), 3)

def trigonometricas(numero, opcao):
    if opcao == 1:
        return f"O valor no seno é {seno(numero)}"
    elif opcao == 2:
        return f"O valor do cosseno é {cosseno(numero)}"
    else:
        return f"O valor da tangente é {tangente(numero)}"


def menu():
    numero1 = 0
    numero2 = 0
    print("Escolha um número para realizar a operação","01 - adição" , "02 - subtração", 
        "03- multiplicação", "04-divisão" , "05-trigonométricas", "06-exponenciação", "07-logaritmos", sep=".\n")
    opcao = int(input("Digite sua escolha: "))

    if opcao == 1:
        numero1 = float(input("Digite o primeiro numero: "))
        numero2 = float(input("Digite o segundo numero: "))
        print(f"O resultado atualmente é {adicao(numero1, numero2)}")
    elif opcao == 2:
        numero1 = float(input("Digite o primeiro numero: "))
        numero2 = float(input("Digite o segundo numero: "))
        print(f"O resultado atualmente é {subtracao(numero1, numero2)}")
    elif opcao == 3:
        numero1 = float(input("Digite o primeiro numero: "))
        numero2 = float(input("Digite o segundo numero: "))
        print(f"O resultado atualmente é {multiplicacao(numero1, numero2)}")
    elif opcao == 4:
        numero1 = float(input("Digite o primeiro numero: "))
        numero2 = float(input("Digite o segundo numero: "))
        print(f"O resultado atualmente é {divisao(numero1, numero2)}")
    elif opcao == 5:
        print("01-Seno", "02-Cosseno", "03-Tangente", sep="\n")
        opcao_trigonometria = int(input("Escolha uma opção: "))
        numero1 = float(input("Digite um numero no angulo radiano: "))
        print(f"{trigonometricas(numero1, opcao_trigonometria)}")
    elif opcao == 6:
        numero1 = float(input("Digite o primeiro numero: "))
        numero2 = float(input("Digite o segundo numero: "))
        print(f"O resultado atualmente é {exponenciacao(numero1, numero2)}")
    elif opcao == 7:
        numero1 = float(input("Digite o primeiro numero: "))
        numero2 = float(input("Digite o segundo numero: "))
        print(f"O resultado atualmente é {logaritmos(numero1, numero2)}")
    else:
        print("Nenhuma opcao valita - Tente novamente")


menu()
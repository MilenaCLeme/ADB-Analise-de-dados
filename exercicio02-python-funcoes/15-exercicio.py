"""

15. Simulador de Lançamento de Dados
   - Crie uma função que simule o lançamento de um dado (ou múltiplos dados) um número específico de vezes e exiba a frequência de cada face.

"""

import random

def numero_aleatorio(min, max):
    return random.randint(min, max)

print("15. Simulador de Lançamento de Dados")

numero_dados = int(input("Digite o numero de dados (1 ou 2): "))
numero_lancamento = int(input("Digite quantas vez vai lançar o dado: "))

def lancamento_de_dados(dados, lancamento):
    if dados == 2:
        list_dois = []
        for i in range(lancamento):
            list_dois.append(f"Rodada {i+1} = O dado 1: {numero_aleatorio(1, 6)}. O dado 2: {numero_aleatorio(1, 6)}")
        return '\n'.join(list_dois)
    else:
        list_um = []
        for i in range(lancamento):
            list_um.append(f"Rodada {i+1} = O dado: {numero_aleatorio(1, 6)}.")
        return '\n'.join(list_um)
    

print(lancamento_de_dados(numero_dados, numero_lancamento))
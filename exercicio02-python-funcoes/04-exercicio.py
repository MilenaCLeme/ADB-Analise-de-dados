"""

4. Gerador de Senhas Seguras
   - Desenvolva uma função que gere uma senha segura com um comprimento especificado. A senha deve conter letras maiúsculas e minúsculas, números e símbolos especiais.

"""

import string
import random

print("4. Gerador de Senhas Seguras")

def numero_aleatorio(min, max):
    return random.randint(min, max)

def gerador_de_senha_segura(comprimento):
    alfabeto = list(string.ascii_letters)
    valor_senha = []
    for i in range(comprimento):
        numero = numero_aleatorio(i, len(alfabeto))
        valor_senha.append(alfabeto[numero])
    valor_senha.append('@')
    valor_senha.append(f"{numero_aleatorio(1, 1000)}")
    return ''.join(valor_senha) 

comprimento = int(input("Digite o número inteiro do comprimento da sua senha: "))

print(f"Sua senha gerada aleatoriamente é: {gerador_de_senha_segura(comprimento)}")

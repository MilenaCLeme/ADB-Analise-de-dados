'''
5.1. Peça ao usuário para digitar um e-mail e verifique se o e-mail contém o
caractere '@'. Imprima uma mensagem indicando se é um e-mail válido ou não.
'''

import re

email = input("Digite seu e-mail: ")

def valitador_email(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if re.fullmatch(regex, email):
        return "E-mail valido"
    else:
        return "E-mail não valido"

print("Seu ", valitador_email(email))

"""
Digite seu e-mail: milena@hotmail.com
Seu  E-mail valido

Digite seu e-mail: milenahotmail.com
Seu  E-mail não valido

Digite seu e-mail: milena@
Seu  E-mail não valido

"""

'''
5.2. Peça ao usuário para digitar uma frase e:
Converta a frase para maiúsculas.
Converta a frase para minúsculas.
Converta a primeira letra de cada palavra para maiúscula.
Verifique se a frase começa com uma determinada palavra (ex.: 'Olá').
'''

frase = input("Digite uma frase: ")

print(frase.upper()) # maiúsculo

print(frase.lower()) # minúsculo

print(frase.title()) # Converta a primeira letra de cada palavra para maiúscula.

contem = "Olá" in frase

print("Contem Olá na frase:", contem) # Verifique se a frase começa com uma determinada palavra (ex.: 'Olá').

"""

Digite seu e-mail: milena@hotmail.com
Seu  E-mail valido
Digite uma frase: Olá, eu amo meu pai, feliz dia dos Pais
OLÁ, EU AMO MEU PAI, FELIZ DIA DOS PAIS
olá, eu amo meu pai, feliz dia dos pais
Olá, Eu Amo Meu Pai, Feliz Dia Dos Pais
Contem Olá na frase: True

"""



"""


6. Validador de CPF
   - Crie uma função que valide um CPF (Cadastro de Pessoas Físicas) de acordo com as regras brasileiras, verificando se o CPF é válido ou não.


"""

import string

print("6. Validador de CPF")

def validador_de_CPF(cpf):
    # Remover os caracteres não numéricos (pontos e hífen)
    numeros = cpf.translate(str.maketrans('', '', string.punctuation))

    #Verificar se o CPF tem 11 dígitos e se não repedi o número.
    if len(numeros) != 11 or numeros == numeros[0] * 11:
        return f"O CPF número {cpf} é inválido"

    soma1 = sum(int(numeros[i]) * (10 - i) for i in range(9))
    digito_1 = (soma1 * 10 % 11) % 10

    soma2 = sum(int(numeros[i]) * (11 - i) for i in range(10))
    digito_2 = (soma2 * 10 % 11) % 10

    if numeros[-2:] == f"{digito_1}{digito_2}":
        return f"O CPF número {cpf} é válido"
    else:
        return f"O CPF número {cpf} é inválido"
    
    
cpf = input("Digite seu CPF: ")

print(validador_de_CPF(cpf))
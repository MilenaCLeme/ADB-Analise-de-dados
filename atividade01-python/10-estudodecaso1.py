'''
Contexto:
Uma empresa precisa registrar informações sobre seus clientes e calcular o IMC
(Índice de Massa Corporal) de cada um deles. As informações devem ser
armazenadas em um dicionário e exibidas ao final.
'''


'''
Requisitos:
Peça ao usuário para inserir os seguintes dados de um cliente:
Nome
Idade
Peso (em kg)
Altura (em metros)
E-mail
Armazene essas informações em um dicionário.
Calcule o IMC do cliente (IMC = Peso / (Altura * Altura)) e adicione esse valor ao dicionário.
Exiba todas as informações do cliente, incluindo o IMC arredondado para duas casas decimais.

'''

print("Por gentileza inserir os dados solicitados a seguir")

dicionario = {}

nome = input("Nome: ")
idade = input("Idade: ")
peso = float(input("Peso (em Kg): "))
altura = float(input("Altura (em metros): "))
email = input("E-mail: ")

def imc(peso, altura):
    resultado = peso / (altura * altura)
    return round(resultado, 2)

dicionario["nome"] = nome
dicionario["idade"] = idade
dicionario["peso"] = peso
dicionario["altura"] = altura
dicionario["email"] = email
dicionario["imc"] = imc(peso, altura)

print(dicionario)

"""
Por gentileza inserir os dados solicitados a seguir
Nome: Milena
Idade: 30
Peso (em Kg): 77
Altura (em metros): 1.52
E-mail: milenaleme4@hotmail.com
{'nome': 'Milena', 'idade': '30', 'peso': 77.0, 'altura': 1.52, 'email': 'milenaleme4@hotmail.com', 'imc': 33.33}

"""
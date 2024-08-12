
'''
3.1. Peça ao usuário para digitar seu nome e armazene em uma variável. Imprima
uma mensagem de boas-vindas usando o nome fornecido.
'''

nome = input("Digite seu nome: ")

print("Boas-vindas, ",nome)

"""

Digite seu nome: Milena
Boas-vindas,  Milena

"""

'''
3.2. Peça ao usuário para digitar sua idade, peso e altura. Calcule o IMC e
imprima o resultado arredondado para três casas decimais.
'''

idade = int( input("Digite seu idade: ") )
peso = float( input("Digite seu peso (kilos): ") )
altura = float( input("Digite sua altura (metros): ") )

def imc(peso, altura):
    resultado = peso / (altura * altura)
    return round(resultado, 3)

print("Seu IMC é ", imc(peso, altura)," e você tem", idade, "anos.")


"""

Digite seu nome: Milena
Boas-vindas,  Milena
Digite seu idade: 30
Digite seu peso (kilos): 66
Digite sua altura (metros): 1.52
Seu IMC é  28.566 30


"""
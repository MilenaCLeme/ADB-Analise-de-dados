# Condicionais
'''
9.1. Peça ao usuário para digitar sua idade e verifique se ele é menor de idade,
 adulto ou idoso. Imprima uma mensagem correspondente.
'''

idade = int(input("Digite sua idade: "))

if idade < 18:
    print("Menor de idade")
elif idade < 65:
    print("Adulto")
else:
    print("Idoso")


# Condicionais
'''
9.2. Peça ao usuário para digitar uma nota (0 a 100) e imprima se ele foi
aprovado (nota >= 60) ou reprovado.
'''

nota = int(input("Digite sua nota (0 a 100): "))

if nota >= 60:
    print("Aprovado")
else:
    print("Reprovado")

# Loop For
'''
9.3. Crie uma lista com os nomes de cinco cidades. Use um loop for para imprimir
cada nome de cidade.
'''

lista_de_cidade = ["São Paulo", "Uberlãndia", "Pato de Minas", "São Caetano do Sul", "Lima"]

for i in range(len(lista_de_cidade)):
    print(lista_de_cidade[i])

# Loop For
'''
9.4. Crie uma lista com os números de 1 a 10. Use um loop for para imprimir o
quadrado de cada número.
'''

lista_de_numero = [1,2,3,4,5,6,7,8,9,10]

for i in range(len(lista_de_numero)):
    print(lista_de_numero[i] ** lista_de_numero[i])
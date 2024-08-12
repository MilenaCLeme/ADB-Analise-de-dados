"""


2. Conversor de Unidades
   - Crie uma função que converta entre diferentes unidades de medida (por exemplo, metros para quilômetros, Celsius para Fahrenheit, etc.). A função deve receber a unidade original e a unidade desejada como parâmetros.


"""

print("2. Conversor de Unidades")

def metro_para_km(metro):
    return metro / 1000

def temperatura_celsuis_fahrenheit(celsius):
    f = (9/5 * celsius) + 32
    return f

def temperatura_fahrenheit_celsuis(fahrenheit):
    c = (fahrenheit - 32) * 5/9
    return c

def km_para_metro(km):
    return km * 1000


def conversor():
    print("Escolha um número para realizar a operação","01 - metros para quilômetros " , "02 - quilômetros para metro", 
        "03- Celsius para Fahrenheit", "04-Fahrenheit para Celsius", sep=".\n")
    opcao = int(input("Digite sua escolha: "))
    numero = float(input("Digite o número para conversão: "))

    if opcao == 1:
        print(f"A conversão do numero {numero} que está em metros, para quilometros ficou {metro_para_km(numero)} ")
    elif opcao == 2:
        print(f"A conversão do numero {numero} que está em quilometros, para metros ficou {km_para_metro(numero)} ")
    elif opcao == 3:
        print(f"A conversão do numero {numero} que está em Celsius, para Fahrenheit ficou {temperatura_celsuis_fahrenheit(numero)} ")
    elif opcao == 4:
        print(f"A conversão do numero {numero} que está em Fahrenheit, para Celsius ficou {temperatura_fahrenheit_celsuis(numero)} ")
    else:
        print("Opção errada!")


conversor()
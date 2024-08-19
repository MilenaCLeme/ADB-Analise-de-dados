"""
20. Conversão de Temperatura
    - **Descrição:** Desenvolva um programa que converta temperaturas de Celsius para Fahrenheit e vice-versa. Use loops para permitir múltiplas conversões até que o usuário decida parar.
"""

def temperatura_celsuis_fahrenheit(celsius):
    return (9/5 * celsius) + 32

def temperatura_fahrenheit_celsuis(fahrenheit):
    return (fahrenheit - 32) * 5/9

def conversao_temperadura():
    while True:
        print("Escolha um número para realizar a operação", "01- Celsius para Fahrenheit", "02-Fahrenheit para Celsius","03-Sair" , sep=".\n")
        opcao = int(input("Digite sua escolha: "))
        
        if opcao == 1 or opcao == 2:
            numero = int(input("Digite número para converter: "))
            
            print(temperatura_celsuis_fahrenheit(numero) if opcao == 1 else temperatura_fahrenheit_celsuis(numero))
        elif opcao == 3:
            print("Tchau! até mais")
            break
        else:
            print('Opcão errada digite novamente')
            

conversao_temperadura()
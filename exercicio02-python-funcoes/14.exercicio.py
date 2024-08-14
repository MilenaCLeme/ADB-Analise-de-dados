"""

14. Conversor de Data
   - Desenvolva uma função que converta datas entre diferentes formatos (por exemplo, de "DD/MM/YYYY" para "YYYY-MM-DD") e que valide se a data inserida é válida.

"""

import datetime

# modelo 1 -  "DD/MM/YYYY" para "YYYY-MM-DD"
def converter_data_modelo_1(data_str):
    x = data_str.split('/')
    return f"{x[2]}-{x[1]}-{x[0]}"

def validar_data(data_str):
    formato = "%d/%m/%Y"
    try:
        data_valida = datetime.strptime(data_str, formato)
        return "válida"
    except ValueError:
        return "inválida"

def menu():
    print("Escolha um número para realizar a operação","01 - converta datas (de DD/MM/YYYY para YYYY-MM-DD) " , "02 - validar data do formado de DD/MM/YYYY",  sep=".\n")
    opcao = int(input("Digite sua escolha: "))

    if opcao == 1:
        data_converter = str(input("Digite a data para converter: "))
        print(f"Era assim {data_converter} é foi para {converter_data_modelo_1(data_converter)}")
    elif opcao == 2:
        data =  str(input("Digite a data para validar (DD/MM/YYYY): "))
        print(f"A data {data} é {validar_data(data)} ")
    else:
        print("Opção errada!")
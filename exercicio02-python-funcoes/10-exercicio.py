"""
10. Simulação de Dados de Temperatura
   - Escreva uma função que simule a coleta de dados de temperatura de diferentes cidades ao longo de uma semana e, em seguida, calcule a média, a temperatura mais alta e mais baixa.

"""

print("10. Simulação de Dados de Temperatura")

def calcule_media_list(list):
    x = 0
    for i in range(len(list)):
        x += list[i]
    return x / len(list)

def calule_temperadura_mais_alta(list):
    x = 0
    for i in range(len(list)):
        if x < list[i]:
            x = list[i]
    return x

def calcule_temperadura_mais_baixa(list):
    x = 0
    for i in range(len(list)):
        if x == 0 or x > list[i]:
            x = list[i]
    return x

def menu():
    list = {
        "São Paulo": [18, 25, 25, 30, 25],
        "Rio de Janeiro": [26, 21, 18, 28, 32]   
    }

    print(f"São Paulo e suas informações: ", f"A média foi {calcule_media_list(list['São Paulo'])}", f"A temperatura mais alta é {calule_temperadura_mais_alta(list['São Paulo'])}", f"a temperatura mais baixa é {calcule_temperadura_mais_baixa(list['São Paulo'])}", sep="\n")
    print(f"Rio de Janeiro e suas informações: ", f"A média foi {calcule_media_list(list['Rio de Janeiro'])}", f"A temperatura mais alta é {calule_temperadura_mais_alta(list['Rio de Janeiro'])}", f"a temperatura mais baixa é {calcule_temperadura_mais_baixa(list['Rio de Janeiro'])}", sep="\n")


menu()
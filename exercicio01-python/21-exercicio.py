"""
21. Média de Notas
    - **Descrição:** Crie um programa que calcule a média de uma série de notas fornecidas pelo usuário. O programa deve parar quando o usuário digitar um valor negativo.
"""

notas = []

def calcular_media():
    nota = 0
    for x in range(notas):
        nota += notas[x]
    
    return nota / len(notas)

def medias_calculo_menu():
    while True:
        numero = int(input("Digite uma nota: "))
        
        if numero > 0:
            notas.append(numero)
            
            print(f"Até o momento temos {len(notas)} notas, a media esta em: {calcular_media()}")
        else:
            print("O programa parar em digitar algo negativo!")
            break
            

medias_calculo_menu()


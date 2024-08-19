"""
28. Tabuada de 1 a 10
    - **Descrição:** Crie um programa que exiba a tabuada de 1 a 10 usando dois loops `for`: um para o número base e outro para o multiplicador.
"""

def tabuada():
    for x in range(1, 11, 1):
        for y in range(1, 11, 1):
            print(f"{x} * {y} = {x*y}")
        
        print("-----------------------")
            
tabuada()
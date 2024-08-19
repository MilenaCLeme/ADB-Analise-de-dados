"""
18. Tabuada de um Número
   - **Descrição:** Crie um programa que exiba a tabuada (de 1 a 10) de um número fornecido pelo usuário usando um loop `for`.
"""

def tabuada(n):
    for x in range(1, 11, 1):
        print(f"{x} * {n} = {x*n}")
        

tabuada(6)
        
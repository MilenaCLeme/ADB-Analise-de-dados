"""
22. Números Divisíveis por 3 e 5
    - **Descrição:** Crie um programa que liste todos os números entre 1 e 100 que são divisíveis por 3 e por 5 usando um loop `for` e condicionais.
"""

def numero_divisiveis_por_3_5_1a100():
    for x in range(1, 100, 1):
        if x % 3 == 0 or x % 5 == 0:
            print(f"{x}")

numero_divisiveis_por_3_5_1a100()
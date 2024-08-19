"""
11. Contador de Números Ímpares
   - **Descrição:** Crie um programa que conte e imprima todos os números ímpares entre 1 e 100 usando um loop `for`.    
"""

def contador_numeros_impares_1a100():
    for x in range(1, 100, 1):
        if x % 2 != 0:
            print(x)
            
contador_numeros_impares_1a100()

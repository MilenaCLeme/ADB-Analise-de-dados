"""
25. Múltiplos de um Número
    - **Descrição:** Crie um programa que encontre todos os múltiplos de um número fornecido pelo usuário até um valor máximo também fornecido pelo usuário.
"""

def multiplo_de_um_numero(n, m):
    for x in range(m):
        if x % n == 0:
            print(f"{x}")
        
multiplo_de_um_numero(8, 82)
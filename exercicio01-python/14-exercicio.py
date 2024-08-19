"""
14. Fatorial de um Número
   - **Descrição:** Calcule o fatorial de um número fornecido pelo usuário usando um loop `for`. O fatorial de um número `n` é o produto de todos os números de 1 até `n`.
"""

def fatorial(n):
    soma = 1
    
    for x in range(n, 1, -1):
        soma *= x
    
    return soma

print(fatorial(5))


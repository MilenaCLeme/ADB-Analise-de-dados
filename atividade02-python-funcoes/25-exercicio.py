"""
25. **Função para Filtrar Números Pares**:
    - Crie uma função chamada `filtrarPares` que receba um array de números como argumento e retorne um novo array contendo apenas os números pares.
"""

def filtrarPares(lst):
    return list(filter(lambda x: x % 2 == 0, lst))

print(filtrarPares([5,2,6,8,7,4,9,3])) #[2, 6, 8, 4]
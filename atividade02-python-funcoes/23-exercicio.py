"""
23. **Função para Encontrar o Maior Número em um Array**:
    - Crie uma função chamada `maiorNumero` que receba um array de números como argumento e retorne o maior número do array.
"""

def maiorNumero(lst):
    return  f"{sorted(lst)[::-1][0]}"

print(maiorNumero([5,2,3,1,8,9]))
print(maiorNumero([100,25,9,82,542,18]))
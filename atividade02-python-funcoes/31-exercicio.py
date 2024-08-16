"""
31. **Função para Remover Duplicatas de um Array**:
    - Crie uma função chamada `removerDuplicatas` que receba um array como argumento e retorne um novo array sem duplicatas.
"""

def removerDuplicatas(lst):
    return list(set(lst))

print(removerDuplicatas([5,6,5,9,9,66,9,8]))

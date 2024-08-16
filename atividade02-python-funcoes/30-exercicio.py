"""
30. **Função para Reduzir um Array**:
    - Crie uma função chamada `reduzirArray` que receba um array de números e uma função de redução (callback) como argumentos e retorne o valor reduzido.
"""

def reducao(lst):
    return list(map(lambda x: x - 1, lst))

def reduzirArray(lst, callback):
    return callback(lst)

print(reduzirArray([1,5,68,67,4], reducao))
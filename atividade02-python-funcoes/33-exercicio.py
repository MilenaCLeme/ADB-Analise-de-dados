"""
33. **Função para Mapear um Array**:
    - Crie uma função chamada `mapearArray` que receba um array e uma função de mapeamento (callback) como argumentos e retorne um novo array com os resultados da função de mapeamento aplicada a cada elemento.

"""

def mapeamento(lst):
    return list(map(lambda x: x + 10, lst))

def mapearArray(lst, callback):
    return callback(lst)

print(mapearArray([8,6,1,2,3], mapeamento))
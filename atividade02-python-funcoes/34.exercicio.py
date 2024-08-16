"""
34. **Função de Ordenação Personalizada**:
    - Crie uma função chamada `ordenarPersonalizado` que receba um array de objetos e uma função de comparação (callback) como argumentos e retorne o array ordenado.
"""
def decresente(lst):
    return sorted(lst)[::-1]

def cresente(lst):
    return sorted(lst)

def ordenarPersonalizado(lst, callback):
    return callback(lst)


print(ordenarPersonalizado([1,2,35,8,6,2], cresente))
print(ordenarPersonalizado([1,2,35,8,6,2], decresente))
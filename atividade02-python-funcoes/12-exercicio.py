"""
12. **Função de Ordem Superior**:
    - Crie uma função chamada `operacao` que receba dois números e uma função como argumentos. A função deve aplicar a função fornecida aos dois números e retornar o resultado.

"""


def multiplicacao(a,b):
    return a * b

def operacao(x, y, func):
    return func(x, y)

print(operacao(5, 7, multiplicacao))
print(operacao(18, 6, multiplicacao))
print(operacao(7, 98, multiplicacao))

"""

35
108
686

"""
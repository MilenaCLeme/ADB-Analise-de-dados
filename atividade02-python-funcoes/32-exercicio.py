"""
32. **Função de Composição**:
    - Crie uma função chamada `compor` que receba duas funções como argumentos e retorne uma nova função que é a composição das duas.
"""

def nome():
    return "Milena"

def saudacao(nome):
    return f"Esse é meu nome: {nome}"

def compor(fun1, func2):
    return fun1(func2())

print(compor(saudacao, nome))
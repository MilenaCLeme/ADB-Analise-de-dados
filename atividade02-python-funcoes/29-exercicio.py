"""
29. **Função de Curry**:
    - Crie uma função chamada `currySoma` que usa currying para somar três números. A função deve ser chamada assim: `currySoma(a)(b)(c)`.
"""

def nome(exibir):
    return f"{exibir}"

def nome2(x , fun):
    return fun(x)

print(nome2('Paulo', nome))



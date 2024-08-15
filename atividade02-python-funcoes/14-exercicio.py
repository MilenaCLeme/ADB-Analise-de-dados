"""
14. **Função Recursiva**:
    - Crie uma função chamada `contagemRegressiva` que receba um número como argumento e exiba uma contagem regressiva a partir desse número até 0, usando recursão.
"""

def contagemRegressiva(numero):
    return f"{numero}, {contagemRegressiva(numero - 1)}"

print(contagemRegressiva(8))
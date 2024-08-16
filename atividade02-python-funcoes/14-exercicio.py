"""
14. **Função Recursiva**:
    - Crie uma função chamada `contagemRegressiva` que receba um número como argumento e exiba uma contagem regressiva a partir desse número até 0, usando recursão.
"""

def contagemRegressiva(n):
    return f"{n}, " + contagemRegressiva(n - 1) if n > 0 else '0'

print(contagemRegressiva(5))
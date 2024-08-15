"""
15. **Função para Calcular Fibonacci**:
    - Crie uma função chamada `fibonacci` que receba um número `n` como argumento e retorne o `n`-ésimo número da sequência de Fibonacci.
"""

def fibonacci(n):
    return fibonacci(n-1) + fibonacci(n - 2) if n > 1 else 1

print(fibonacci(10)) # 89

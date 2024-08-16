"""

6. **Função de Fatorial**:
   - Crie uma função chamada `fatorial` que receba um número como argumento e retorne o fatorial desse número.

"""

def fatorial(n):
    return n * fatorial(n-1) if n > 1 else 1

print(fatorial(5))
print(fatorial(10))
print(fatorial(6))

"""
120
3628800
720

"""
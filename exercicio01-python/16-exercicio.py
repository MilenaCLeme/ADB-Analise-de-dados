"""
16. Sequência de Fibonacci
   - **Descrição:** Gere a sequência de Fibonacci até um número máximo fornecido pelo usuário usando um loop `while`. A sequência começa com 0 e 1, e cada número subsequente é a soma dos dois anteriores.
"""

def fibonacci(n):
    soma = 0
    contador = 0
    while contador < n:
        contador += 1
        soma += (n-1) + (n-2)
    return soma    
    

print(fibonacci(5))




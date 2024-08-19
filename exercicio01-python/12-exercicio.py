"""
12. Soma de Números até um Limite
   - **Descrição:** Desenvolva um programa que receba um número inteiro positivo e use um loop `while` para calcular a soma de todos os números de 1 até o número fornecido.
"""

def soma_numero(n):
   contador = 1
   soma = 0
   while contador <= n:
      soma += contador
      contador += 1
   
   return soma

print(soma_numero(5))
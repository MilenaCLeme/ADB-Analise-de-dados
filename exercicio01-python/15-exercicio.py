""" 
15. Verificação de Primalidade
   - **Descrição:** Crie um programa que verifique se um número é primo. Use um loop `for` e condicionais para determinar se o número tem apenas dois divisores: 1 e ele mesmo.
"""

def ePrimo(x):
   n = 0
   if x == 1 or x == 2:
      return True
   
   for i in range(x, 0, -1):
      if x % i == 0:
         n += 1

   if n > 2:
      return False

   return True

print(ePrimo(10))


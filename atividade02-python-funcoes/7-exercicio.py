"""

7. **Função para Verificar Número Primo**:
   - Crie uma função chamada `ePrimo` que receba um número como argumento e retorne `true` se o número for primo e `false` caso contrário.

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
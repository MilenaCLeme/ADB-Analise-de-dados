"""
3. Verificação de Número Par, Ímpar e Positivo/Negativo
   **Problema:** Crie um programa que receba um número inteiro e informe se ele é par ou ímpar e, adicionalmente, se é positivo, negativo ou zero. Inclua uma mensagem especial para números que sejam múltiplos de 10.

"""

print("3. Verificação de Número Par, Ímpar e Positivo/Negativo")

numero = int(input("Digite um número: "))

def verificacao_de_numeros(numero=0):
   texto = ''
   if numero == 0:
      texto += ' é zero.'
   elif numero > 0:
      texto += ' é positivo.'
   else:
      texto += ' é negativo.'
   
   if numero % 2 == 0:
      texto += 'Ele é par.'
   else:
      texto += 'Ele é impar.'

   if numero % 10 == 0:
      texto += 'Ele também é multiplo de 10! Incrivel esse número.'
   else:
      texto += 'Ele não é multiplo de 10.'
   
   print(f" O número {numero}{texto}")

verificacao_de_numeros(numero)
   

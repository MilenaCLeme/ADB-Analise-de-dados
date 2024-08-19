"""
7. Conversão e Comparação de Temperatura
   **Problema:** Crie um programa que receba uma temperatura em graus Celsius e a converta para Fahrenheit. Em seguida, verifique se a temperatura em Fahrenheit é inferior a 32°F (fria), entre 32°F e 68°F (amena), ou superior a 68°F (quente). Mostre a classificação junto com a temperatura convertida.
"""

converta_celsius_para_fahrenheit = lambda x: round((9/5 * x) + 32, 2)

def verificacao_celsius(c):
   converter = converta_celsius_para_fahrenheit(c)
   return 'quente' if converter > 68 else ('amena'if 68 > converter > 32 else 'fria')


print(verificacao_celsius(21))
print(verificacao_celsius(-1))
print(verificacao_celsius(15))

"""
quente
fria
amena   
"""
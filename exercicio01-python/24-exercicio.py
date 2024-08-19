"""
24. Verificar Palíndromo
    - **Descrição:** Desenvolva um programa que verifique se uma palavra é um palíndromo (ou seja, se pode ser lida da mesma forma de trás para frente). Use um loop `for` e condicionais.
"""

import re

def palindromo(texto: str):
    converter = re.sub('[^a-zA-Z0-9]', '', texto.upper())
    novo = ''
    for x in range(len(converter), 0, -1):
        novo += converter[x-1]
    
    if converter == novo:
        print(" palavra é um palíndromo ")
    else:
        print(" palavra não é um palíndromo ")


palindromo("arara")    
"""

3. Verificador de Palíndromo
   - Escreva uma função que verifique se uma determinada palavra ou frase é um palíndromo (lê-se da mesma forma de frente para trás). A função deve ignorar espaços e pontuações.


"""


"""

Outra forma - estudar 


import re (veirificar como funciona o re)


def palindromo():
  frase = input("Digite uma frase: ").strip().upper()
  frase_sem_espaco_caractere = re.sub('[^a-zA-Z0-9]', '', frase) --- localizado aqui 
  frase_inversa = frase_sem_espaco_caractere[::-1]
  
  if (frase_sem_espaco_caractere == frase_inversa ):
   print("Esta palavra é um palindromo")
  else:
   print("Esta palavra não é um palindromo")

print(palindromo())


"""

import unicodedata
import string

print("3. Verificador de Palíndromo")

def remover_acento_limpar_texto(frase):
    texto_sem_espacos = frase.replace(" ", "")
    texto_sem_pontuacao = texto_sem_espacos.translate(str.maketrans('', '', string.punctuation))
    texto_normalizado = unicodedata.normalize('NFD', texto_sem_pontuacao)
    return ''.join(c for c in texto_normalizado if not unicodedata.combining(c))

def palindromo():
    frase = str(input("Digite uma frase: ")).upper()
    texto_remover = remover_acento_limpar_texto(frase)
    inverso = texto_remover[::-1]
    print(texto_remover, inverso)
    if texto_remover == inverso:
        print("Temos um palindromo")
    else:
        print("A frase digitada não é um palindromo!")

palindromo()


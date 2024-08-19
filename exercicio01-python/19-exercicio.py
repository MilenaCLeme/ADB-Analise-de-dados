"""
19. Contador de Letras em Palavras
   - **Descrição:** Dada uma lista de palavras, conte quantas letras `a` existem em todas as palavras usando um loop `for` e condicionais.
"""

def caracter(text: str):
    soma = 0
    for x in text:
        if x.upper() == 'a'.upper():
            soma += 1
        
    return soma

print(caracter('EuAmoVoceMuitoeMuitaaaa'))

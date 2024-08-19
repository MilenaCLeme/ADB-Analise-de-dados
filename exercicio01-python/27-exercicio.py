"""
27. Contar Palavras em uma Frase
    - **Descrição:** Crie um programa que conte o número de palavras em uma frase fornecida pelo usuário. Use um loop `for` para iterar sobre as palavras da frase.
"""

def conter_palavras_em_uma_frase(frase: str):
    lst = frase.split(' ')
    soma = 0
    for x in range(len(lst)):
        soma += 1
    return soma

print(conter_palavras_em_uma_frase('Eu Amo Muito Tudo Isso'))
    
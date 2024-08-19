"""
17. Contar Caracteres em uma String
   - **Descrição:** Conte quantas vezes um caractere específico aparece em uma string fornecida pelo usuário usando um loop `for`.
"""

def caracter(c: str, text: str):
    soma = 0
    for x in text:
        if x.upper() == c.upper():
            soma += 1
        
    return soma

print(caracter('e', 'EuAmoVoce'))

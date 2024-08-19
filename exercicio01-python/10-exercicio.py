"""
10. Verificação de Senha Segura com Requisitos Adicionais
   **Problema:** Desenvolva um programa que receba uma senha e verifique se ela é segura. Uma senha é considerada segura se tiver pelo menos 8 caracteres, incluir pelo menos uma letra maiúscula, uma letra minúscula, um número e um caractere especial (como !, @, #). Informe se a senha é segura ou não e liste quais requisitos estão faltando.
"""

import re

def verificacao_de_senha_segura(text: str):
    requisitos = ''
    if len(text) < 8:
        requisitos += ' Menos que 8 caracteres.'
    
    if not (re.search('[A-Z]', text)):
        requisitos += ' Precisa conter pelo menos uma letra maiúscula.'
    
    if not (re.search('[a-z]', text)):
        requisitos += ' Precisa conter pelo menos uma letra minuscula.'
    
    if not (re.search('[0-9]', text)):
        requisitos += ' Precisa conter pelo menos uma número.'
    
    if not (re.search('[^a-zA-Z0-9\s]', text)):
        requisitos += ' Precisa conter pelo menos uma caractere especiais.'
    
    if len(requisitos) > 0:
        return f"A senha não é segura. Segue Requisitos:{requisitos}"
    
    return f"A senha é segura"
    

print(verificacao_de_senha_segura('Euamo'))
print(verificacao_de_senha_segura('EuAmoVoce@123'))

"""
A senha não é segura. Segue Requisitos: Menos que 8 caracteres. Precisa conter pelo menos uma número. Precisa conter pelo menos uma caractere especiais.
A senha é segura    
"""
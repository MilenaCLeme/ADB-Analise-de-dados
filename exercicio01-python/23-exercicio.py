"""
23. Inverter uma String
    - **Descrição:** Crie um programa que inverta uma string fornecida pelo usuário sem usar funções embutidas, utilizando um loop `for`.
"""

def inverter_string(text):
    novo = ''
    for x in range(len(text),0,-1):
       novo += text[x-1]
    
    return novo

print(inverter_string('Euqueroentender')) 
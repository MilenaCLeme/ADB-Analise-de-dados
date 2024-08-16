"""
28. **Função para Verificar Substring**:
    - Crie uma função chamada `contemSubstring` que receba duas strings como argumentos e retorne `true` se a primeira string contiver a segunda string, e `false` caso contrário.
"""

def contemSubtring(text1: str, text2: str) -> bool:
    return text1.upper() in text2.upper()

print(contemSubtring('Ola', 'Oii.. Ola.. Quero saber mais'))
print(contemSubtring('oi', 'eu quero saber se você mand um OI'))
print(contemSubtring('sei', 'eu quero saber se você mand um OI'))

"""
True
True
False
"""
"""

22. **Função para Verificar Palíndromo**:
    - Crie uma função chamada `ePalindromo` que receba uma string como argumento e retorne `true` se a string for um palíndromo e `false` caso contrário.

"""

import re

def ePalindromo(frase: str) -> bool:
    inverter = re.sub('[^a-zA-Z0-9]', '', frase.upper())
    return inverter == inverter[::-1] 

print(ePalindromo('Roma me tem amor')) #True
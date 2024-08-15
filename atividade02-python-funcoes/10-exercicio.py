"""

10. **Função para Contar Caracteres**:
    - Crie uma função chamada `contarCaracteres` que receba uma string e um caractere como argumentos e retorne o número de vezes que o caractere aparece na string.

"""

def contarCaracters(frase: str, caractere: str) -> int:
    return len(list(filter(lambda x: x == caractere.upper(), list(frase.upper()))))

print(contarCaracters('arara', 'a'))
print(contarCaracters('Você é demais!!!', '!'))

"""

3
3

"""
"""

21. **Função para Contar Vogais**:
    - Crie uma função chamada `contarVogais` que receba uma string como argumento e retorne o número de vogais na string.

"""

def contarVogais(texto):
    return len(list(filter(lambda x: x == 'A' or x == 'E' or x == 'I' or x == 'O' or x == 'U', list(texto.upper()))))

print(contarVogais('Amor'))
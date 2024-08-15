"""

13. **Função de Retorno**:
    - Crie uma função chamada `criarSaudacao` que receba uma saudação como argumento e retorne uma nova função. A função retornada deve receber um nome como argumento e exibir a saudação seguida pelo nome.

"""

def criarSaudacao(saudacao):
    def exibir_saudacao(nome):
        return f"{saudacao}, {nome}"
    return exibir_saudacao

saudar = criarSaudacao('Olá')

print(saudar('Milena'))
print(saudar('Neto'))

"""
Olá, Milena
Olá, Neto

"""
'''
8.1. Crie um dicionário com informações de um cliente
(nome, idade, peso, altura). Imprima o valor associado à chave 'nome'.
'''

cliente = {
    "nome": "Milena",
    "idade": 30,
    "peso": 77.0,
    "altura": 1.52
}

print(cliente["nome"]) # Milena

'''
8.2. Adicione uma nova chave 'email' ao dicionário do exercício anterior e
imprima o dicionário atualizado.
'''

cliente["email"] = "milenalemeh@gmail.com"
print(cliente) # {'nome': 'Milena', 'idade': 30, 'peso': 77.0, 'altura': 1.52, 'email': 'milenalemeh@gmail.com'}

'''
8.3. Remova a chave 'peso' do dicionário e verifique se a chave 'endereço' está
no dicionário. Imprima os resultados.
'''

cliente.pop("peso")

print(cliente)
print(cliente.get("endereço"))

"""

Milena
{'nome': 'Milena', 'idade': 30, 'peso': 77.0, 'altura': 1.52, 'email': 'milenalemeh@gmail.com'}
{'nome': 'Milena', 'idade': 30, 'altura': 1.52, 'email': 'milenalemeh@gmail.com'}
None

"""
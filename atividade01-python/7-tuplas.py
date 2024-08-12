'''
7.1 Crie uma tupla com as informações de um cliente (nome, idade, peso, altura).
Imprima todas as informações.
'''
informacao_cliente = ("Milena", 30, 77.0, 1.52)
print(informacao_cliente) 

"""

('Milena', 30, 77.0, 1.52)

"""

'''
7.2. Crie uma nova tupla concatenando a tupla do exercício anterior com o e-mail
do cliente. Imprima a nova tupla.
'''

nova_tupla = informacao_cliente + ("milenalemeh@hotmail.com", )

print(nova_tupla)

"""

('Milena', 30, 77.0, 1.52)
('Milena', 30, 77.0, 1.52, 'milenalemeh@hotmail.com')

"""
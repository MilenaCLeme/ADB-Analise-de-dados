'''
Contexto
Uma empresa deseja realizar uma pesquisa de opinião com cinco participantes
sobre um novo produto. As respostas devem ser armazenadas e analisadas para
verificar a satisfação dos clientes.
'''

'''
Requisitos
Peça ao usuário para inserir o nome e a opinião (satisfeito/insatisfeito) de
cinco participantes.
Armazene os nomes e as opiniões em um dicionário.
Conte o número de participantes satisfeitos e insatisfeitos.
Exiba a lista de participantes satisfeitos e insatisfeitos, bem como o número
total de cada categoria.
'''

lista = []

def satisfacao_insatisfacao():
    satisfacao = 0
    insatisfacao = 0
    for i in range(len(lista)):
        opiniao = lista[i]["opiniao"]
        if opiniao == 0:
            insatisfacao += 1
        else:
            satisfacao += 1
    
    print("O numero total de clientes", len(lista), ". O numero de clientes satisfeitos foi", satisfacao, "O numero de clientes insatisfeitos foi", insatisfacao)


def exibir_lista():
    for i in range(len(lista)):
        nome_do_cliente = lista[i]["nome"]
        nota_do_satisfaca = lista[i]["opiniao"]

        if nota_do_satisfaca == 0:
            print("Nome do cliente:", nome_do_cliente, ".Este cliente está insatisfeito")
        else:
            print("Nome do cliente:", nome_do_cliente, ".Este cliente está satisfeito" )


def inserir_nome_nota_lista(nome, nota):
    if (len(lista) < 5):
        lista.append({"nome": nome, "opiniao": nota})
        return "Inserido com sucesso"
    else:
        return "Limite Maximo de registro"

def menu():
    print("---Menu---")
    print("1 - Registro Nome do Cliente e Satisfação do produto (maximo 5)")
    print("2 - Exibir a lista de participantes")
    print("3 - Exibir o numero total de satisfeitos e insatisfeitos")
    print("4 - exit")
    verificacao()

def verificacao():
    numero = int(input("Digite numero do menu: "))

    print("---------------------------------------")

    if numero == 1:
        nome = input("Digite o nome do Cliente: ")
        nota = int(input("Digite o numero 1 para satisfeito ou 0 para insatisfeitos: "))
        print(inserir_nome_nota_lista(nome, nota))
        print("---------------------------------------")
        menu()
    
    elif numero == 2:
        exibir_lista()
        print("---------------------------------------")
        menu()

    elif numero == 3:
        satisfacao_insatisfacao()
        print("---------------------------------------")
        menu()
    
    else:
        print("Ate o proxima")


menu()

"""

---Menu---
1 - Registro Nome do Cliente e Satisfação do produto (maximo 5)
2 - Exibir a lista de participantes
3 - Exibir o numero total de satisfeitos e insatisfeitos
4 - exit
Digite numero do menu: 1
---------------------------------------
Digite o nome do Cliente: Milena
Digite o numero 1 para satisfeito ou 0 para insatisfeitos: 1
Inserido com sucesso
---------------------------------------
---Menu---
1 - Registro Nome do Cliente e Satisfação do produto (maximo 5)
2 - Exibir a lista de participantes
3 - Exibir o numero total de satisfeitos e insatisfeitos
4 - exit
Digite numero do menu: 1
---------------------------------------
Digite o nome do Cliente: Neto
Digite o numero 1 para satisfeito ou 0 para insatisfeitos: 1
Inserido com sucesso
---------------------------------------
---Menu---
1 - Registro Nome do Cliente e Satisfação do produto (maximo 5)
2 - Exibir a lista de participantes
3 - Exibir o numero total de satisfeitos e insatisfeitos
4 - exit
Digite numero do menu: 1
---------------------------------------
Digite o nome do Cliente: Andre
Digite o numero 1 para satisfeito ou 0 para insatisfeitos: 0
Inserido com sucesso
---------------------------------------
---Menu---
1 - Registro Nome do Cliente e Satisfação do produto (maximo 5)
2 - Exibir a lista de participantes
3 - Exibir o numero total de satisfeitos e insatisfeitos
4 - exit
Digite numero do menu: 1
---------------------------------------
Digite o nome do Cliente: José
Digite o numero 1 para satisfeito ou 0 para insatisfeitos: 0
Inserido com sucesso
---------------------------------------
---Menu---
1 - Registro Nome do Cliente e Satisfação do produto (maximo 5)
2 - Exibir a lista de participantes
3 - Exibir o numero total de satisfeitos e insatisfeitos
4 - exit
Digite numero do menu: 1
---------------------------------------
Digite o nome do Cliente: Milena 2
Digite o numero 1 para satisfeito ou 0 para insatisfeitos: 1
Inserido com sucesso
---------------------------------------
---Menu---
1 - Registro Nome do Cliente e Satisfação do produto (maximo 5)
2 - Exibir a lista de participantes
3 - Exibir o numero total de satisfeitos e insatisfeitos
4 - exit
Digite numero do menu: 1
---------------------------------------
Digite o nome do Cliente: Claudio
Digite o numero 1 para satisfeito ou 0 para insatisfeitos: 1
Limite Maximo de registro
---------------------------------------
---Menu---
1 - Registro Nome do Cliente e Satisfação do produto (maximo 5)
2 - Exibir a lista de participantes
3 - Exibir o numero total de satisfeitos e insatisfeitos
4 - exit
Digite numero do menu: 2
---------------------------------------
Nome do cliente: Milena .Este cliente está satisfeito
Nome do cliente: Neto .Este cliente está satisfeito
Nome do cliente: Andre .Este cliente está insatisfeito
Nome do cliente: José .Este cliente está insatisfeito
Nome do cliente: Milena 2 .Este cliente está satisfeito
---------------------------------------
---Menu---
1 - Registro Nome do Cliente e Satisfação do produto (maximo 5)
2 - Exibir a lista de participantes
3 - Exibir o numero total de satisfeitos e insatisfeitos
4 - exit
Digite numero do menu: 3
---------------------------------------
O numero total de clientes 5 . O numero de clientes satisfeitos foi 3 O numero de clientes insatisfeitos foi 2
---------------------------------------
---Menu---
1 - Registro Nome do Cliente e Satisfação do produto (maximo 5)
2 - Exibir a lista de participantes
3 - Exibir o numero total de satisfeitos e insatisfeitos
4 - exit
Digite numero do menu: 4
---------------------------------------
Ate o proxima


"""
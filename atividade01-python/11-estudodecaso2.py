'''
Contexto:
Uma escola precisa analisar as notas de seus alunos e determinar se cada aluno
foi aprovado ou reprovado. As notas serão armazenadas em uma lista e a análise
deve ser realizada em um loop.
'''

'''
Requisitos:
Peça ao usuário para inserir o nome e a nota de cinco alunos.
Armazene os nomes e as notas em listas separadas.
Para cada aluno, verifique se a nota é maior ou igual a 60. Se sim, o aluno está
aprovado; caso contrário, está reprovado.
Exiba uma mensagem para cada aluno informando seu nome, nota e se foi aprovado
ou reprovado.
'''

lista = []

def mensagem_aprovados():
    for i in range(len(lista)):
        nome_do_aluno = lista[i][0]
        nota_do_aluno = lista[i][1]

        if int(nota_do_aluno) >= 60:
            print("O(a) aluno(a)", nome_do_aluno, "foi aprovado, com a nota de", nota_do_aluno)
        else:
            print("O(a) aluno(a)", nome_do_aluno, "foi reprovado, com a nota de", nota_do_aluno)

def inserir_nome_nota_lista(nome, nota):
    if (len(lista) < 5):
        lista.append([nome, nota])
        return "Inserido com sucesso"
    else:
        return "Limite Maximo de registro"

def menu():
    print("---Menu---")
    print("1 - Registro Aluno e nota (maximo 5)")
    print("2 - Verificação de aprovação dos alunos registrados")
    print("3 - exit")
    verificacao()

def verificacao():
    numero = int(input("Digite numero do menu: "))

    print("---------------------------------------")

    if numero == 1:
        nome = input("Digite o nome do aluno: ")
        nota = input("Digite a nota do aluno: ")
        print(inserir_nome_nota_lista(nome, nota))
        print("---------------------------------------")
        menu()
    
    elif numero == 2:
        mensagem_aprovados()
        print("---------------------------------------")
        menu()
    
    else:
        print("Ate o proxima")


menu()

"""

---Menu---
1 - Registro Aluno e nota (maximo 5)
2 - Verificação de aprovação dos alunos registrados
3 - exit
Digite numero do menu: 1
---------------------------------------
Digite o nome do aluno: Milena
Digite a nota do aluno: 60
Inserido com sucesso
---------------------------------------
---Menu---
1 - Registro Aluno e nota (maximo 5)
2 - Verificação de aprovação dos alunos registrados
3 - exit
Digite numero do menu: 1
---------------------------------------
Digite o nome do aluno: Sei la
Digite a nota do aluno: 40
Inserido com sucesso
---------------------------------------
---Menu---
1 - Registro Aluno e nota (maximo 5)
2 - Verificação de aprovação dos alunos registrados
3 - exit
Digite numero do menu: 1
---------------------------------------
Digite o nome do aluno: Neto
Digite a nota do aluno: 100
Inserido com sucesso
---------------------------------------
---Menu---
1 - Registro Aluno e nota (maximo 5)
2 - Verificação de aprovação dos alunos registrados
3 - exit
Digite numero do menu: 1
---------------------------------------
Digite o nome do aluno: Pedro
Digite a nota do aluno: 60
Inserido com sucesso
---------------------------------------
---Menu---
1 - Registro Aluno e nota (maximo 5)
2 - Verificação de aprovação dos alunos registrados
3 - exit
Digite numero do menu: 1
---------------------------------------
Digite o nome do aluno: Mari
Digite a nota do aluno: 100
Inserido com sucesso
---------------------------------------
---Menu---
1 - Registro Aluno e nota (maximo 5)
2 - Verificação de aprovação dos alunos registrados
3 - exit
Digite numero do menu: 1
---------------------------------------
Digite o nome do aluno: Milena
Digite a nota do aluno: 90
Limite Maximo de registro
---------------------------------------
---Menu---
1 - Registro Aluno e nota (maximo 5)
2 - Verificação de aprovação dos alunos registrados
3 - exit
Digite numero do menu: 2
---------------------------------------
O(a) aluno(a) Milena foi aprovado, com a nota de 60
O(a) aluno(a) Sei la foi reprovado, com a nota de 40
O(a) aluno(a) Neto foi aprovado, com a nota de 100
O(a) aluno(a) Pedro foi aprovado, com a nota de 60
O(a) aluno(a) Mari foi aprovado, com a nota de 100
---------------------------------------
---Menu---
1 - Registro Aluno e nota (maximo 5)
2 - Verificação de aprovação dos alunos registrados
3 - exit
Digite numero do menu: 3
---------------------------------------
Ate o proxima


"""
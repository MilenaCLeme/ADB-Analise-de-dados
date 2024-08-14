"""

9. Sistema de Votação
   - Crie um sistema de votação simples em que os usuários podem votar em diferentes opções. A função deve calcular e exibir o vencedor com base nos votos.

"""

print("9. Sistema de Votação", "-------------------------------------", sep="\n")

dicionario = {
    "neto": 0,
    "amanda": 0,
    "nome": 0,
}

def votacao():
    print("---VOTAÇÃO---", "01-Neto Russo", "02-Amanda Cris", "03-Seu nome")
    votacao = int(input("Digite seu voto: "))
    if votacao == 1:
        dicionario["neto"] = dicionario["neto"] + 1
    elif votacao == 2:
        dicionario["amanda"] = dicionario["amanda"] + 1
    elif votacao == 3:
        dicionario["nome"] = dicionario["nome"] + 1
    else:
        return "Não houve votação"
    
    return "Votação realizada com sucesso!"

def contagem():
    ganhador = ''
    if dicionario["neto"] > dicionario['amanda'] and dicionario["neto"] > dicionario['nome']:
        ganhador = "Neto Russo"
    elif dicionario["amanda"] > dicionario['neto'] and dicionario["amanda"] > dicionario['nome']:
        ganhador = "Neto Russo"
    elif dicionario["nome"] > dicionario["neto"] and dicionario["nome"] > dicionario["amanda"]:
        ganhador = "Seu Nome"
    else:
        ganhador = "Embate!"

    return f"O valor do Neto Russo é {dicionario['neto']}. O valor de Amanda Cris é {dicionario['amanda']}. O valor de Seu nome é {dicionario['nome']}, \n O ganhador foi {ganhador}"


def menu():
    print("---MENU---", "01-Realizar Votação", "02-Contagem dos votos", "03-Exit", sep="\n")
    numero = int(input("Digite o numero do menu: "))
    
    if numero == 1:
        votacao()
        print("----------------------------")
        menu()
    elif numero == 2:
        print(contagem())
        print("----------------------------")
        menu()
    elif numero == 3:
        print("Até a próxima!!")
    else:
        print("Error! tente novamente!", "-------------------------", sep="\n")
        menu()

    
menu()

"""

9. Sistema de Votação
-------------------------------------
---MENU---
01-Realizar Votação
02-Contagem dos votos
03-Exit
Digite o numero do menu: 1
---VOTAÇÃO--- 01-Neto Russo 02-Amanda Cris 03-Seu nome
Digite seu voto: 1
----------------------------
---MENU---
01-Realizar Votação
02-Contagem dos votos
03-Exit
Digite o numero do menu: 1
---VOTAÇÃO--- 01-Neto Russo 02-Amanda Cris 03-Seu nome
Digite seu voto: 1
----------------------------
---MENU---
01-Realizar Votação
02-Contagem dos votos
03-Exit
Digite o numero do menu: 1
---VOTAÇÃO--- 01-Neto Russo 02-Amanda Cris 03-Seu nome
Digite seu voto: 2
----------------------------
---MENU---
01-Realizar Votação
02-Contagem dos votos
03-Exit
Digite o numero do menu: 1
---VOTAÇÃO--- 01-Neto Russo 02-Amanda Cris 03-Seu nome
Digite seu voto: 3
----------------------------
---MENU---
01-Realizar Votação
02-Contagem dos votos
03-Exit
Digite o numero do menu: 1
---VOTAÇÃO--- 01-Neto Russo 02-Amanda Cris 03-Seu nome
Digite seu voto: 1
----------------------------
---MENU---
01-Realizar Votação
02-Contagem dos votos
03-Exit
Digite o numero do menu: 1
---VOTAÇÃO--- 01-Neto Russo 02-Amanda Cris 03-Seu nome
Digite seu voto: 1
----------------------------
---MENU---
01-Realizar Votação
02-Contagem dos votos
03-Exit
Digite o numero do menu: 2
O valor do Neto Russo é 4. O valor de Amanda Cris é 1. O valor de Seu nome é 1, 
 O ganhador foi Neto Russo
----------------------------
---MENU---
01-Realizar Votação
02-Contagem dos votos
03-Exit
Digite o numero do menu: 8
Error! tente novamente!
-------------------------
---MENU---
01-Realizar Votação
02-Contagem dos votos
03-Exit
Digite o numero do menu: 3
Até a próxima!!

"""
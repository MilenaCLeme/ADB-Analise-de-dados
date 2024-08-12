"""

2. Classificação de Idade com Mensagens Personalizadas
   **Problema:** Desenvolva um programa que receba a idade de uma pessoa e determine sua categoria: "Criança" (0-12 anos), "Adolescente" (13-17 anos), "Adulto" (18-64 anos) ou "Idoso" (65 anos ou mais). Exiba uma mensagem personalizada para cada faixa etária, como "Você é uma criança cheia de energia!" ou "Você tem muita sabedoria como idoso!".

"""

print("2. Classificação de Idade com Mensagens Personalizadas")

idade = int(input("Digite a sua idade: "))

def mensagem_personaliza_por_idade(valor=0):
    if 0 < valor < 13:
        print(f"Sua idade é {valor} anos. Sua mensagem no dia: Você é uma criança cheia de energia!")
    elif 12 < valor < 18:
        print(f"Sua idade é {valor} anos. Sua mensagem no dia: Você é uma adolescente maravilhoso")
    elif 17 < valor < 65:
        print(f"Sua idade é {valor} anos. Sua mensagem no dia: Você é uma adulto incrivel!")
    else:
        print(f"Sua idade é {valor} anos. Sua mensagem no dia: Você tem muita sabedoria como idoso!")

mensagem_personaliza_por_idade(idade)

"""
2. Classificação de Idade com Mensagens Personalizadas
Digite a sua idade: 10
Sua idade é 10 anos. Sua mensagem no dia: Você é uma criança cheia de energia!

2. Classificação de Idade com Mensagens Personalizadas
Digite a sua idade: 15
Sua idade é 15 anos. Sua mensagem no dia: Você é uma adolescente maravilhoso

2. Classificação de Idade com Mensagens Personalizadas
Digite a sua idade: 25
Sua idade é 25 anos. Sua mensagem no dia: Você é uma adulto incrivel!

2. Classificação de Idade com Mensagens Personalizadas
Digite a sua idade: 65
Sua idade é 65 anos. Sua mensagem no dia: Você tem muita sabedoria como idoso!
"""
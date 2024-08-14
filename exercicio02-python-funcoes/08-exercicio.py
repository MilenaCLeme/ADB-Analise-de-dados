"""

8. Análise de Sentimento
   - Desenvolva uma função que analise uma frase ou texto e determine se o sentimento é positivo, negativo ou neutro, usando uma abordagem simples baseada em palavras-chave.

"""

print("8. Análise de Sentimento")

list_positivo = [
    "ótimo",
    "excelente",
    "maravilhoso",
    "feliz",
    "incrível",
    "sucesso",
    "bom",
    "fantástico",
    "alegre",
    "satisfatório",
    "perfeito",
    "positivo",
    "agradável",
    "brilhante",
    "encantador",
    "excepcional",
    "promissor",
    "admirável",
    "estimulante",
    "magnífico",
    "amo",
    "amor"
]

list_negativo = [
    "ruim",
    "horrível",
    "péssimo",
    "triste",
    "decepcionante",
    "desastroso",
    "insucesso",
    "terrível",
    "desagradável",
    "frustrante",
    "negativo",
    "lamentável",
    "desanimador",
    "desesperador",
    "horrendo",
    "medíocre",
    "inaceitável",
    "deprimente",
    "destrutivo",
    "tóxico"
]

def analise_frase(text=""):
    frase_positiva = 0
    frase_negativa = 0

    for i in range(len(list_positivo)):
        contem = list_positivo[i] in text
        if contem:
            frase_positiva += 1


    for j in range(len(list_negativo)):
        contem = list_negativo[j] in text
        if contem:
            frase_negativa += 1

    if frase_positiva > 0:
        return "O sentimento é positivo"
    elif frase_negativa > 0:
        return "O sentimento é negativo"
    else:
        return "O sentimento é neutro"
    

texto = str(input("Digite uma frase: "))

print(analise_frase(texto))

"""

8. Análise de Sentimento
Digite uma frase: eu me amo muito 
O sentimento é positivo

"""
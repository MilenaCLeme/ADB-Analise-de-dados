"""

12. Analisador de Texto
   - Crie uma função que receba um texto e retorne o número de palavras, frases, e caracteres, além de calcular a frequência de cada palavra no texto.

"""

print("12. Analisador de Texto")

frase = str(input("Digite uma frase: "))

def numero_de_caracteres(texto):
    return len(texto)

def numero_de_palavras(texto):
    list_palavras = texto.split()
    return len(list_palavras)

def numero_de_frases(texto):
    list_frases = texto.split('.')
    return len(list_frases)

def calcular_frequência_de_cada_palavra(texto):
    list_texto = texto.split()
    list_total = []
    for i in range(len(list_texto)):
        total = 0
        for j in range(len(list_texto)):
            contem = False
            for l in list_total:
                if list_texto[i] in l:
                    contem = True
            if list_texto[i] == list_texto[j] and contem == False:
                total += 1
        list_total.append(f"{list_texto[i]}: {total}")
    
    return ' '.join(list_total)

def escrutura_para_realizar(frases="Amo tudo isso"):
    print(f"A frases inserida é: {frases}", f"O número de palavras é: {numero_de_palavras(frases)}", f"O número de frases é: {numero_de_frases(frases)}", f"O número de caracteres é: {numero_de_caracteres(frases)}", sep="\n")
    print(f"Segue a frequência de cada palavra no texto:", f"{calcular_frequência_de_cada_palavra(frases)}")

escrutura_para_realizar(frase)

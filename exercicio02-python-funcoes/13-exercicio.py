"""

13. Cálculo de Juros Compostos
   - Escreva uma função que calcule o valor futuro de um investimento com base nos juros compostos. A função deve permitir a personalização do principal, taxa de juros, e número de períodos.

"""

print("13. Cálculo de Juros Compostos")

valor = float(input("Digite seu investimento: "))
taxa = float(input("Digite sua taxa de juros: "))
periodo = int(input("Digite o periodo para pagamento: "))

def calculo_de_juros_compostos(valor, taxa, periodo):
    list = []
    valores = []

    for i in range(periodo):
        if len(list) > 0:
            list.append(f"{i+1} parcela: R$ {round(valores[i-1]*(1+taxa), 2)}.")
            valores.append(valores[i-1]*(1+taxa))
        else:
            list.append(f"{i+1} parcela: R$ {round(valor*(1+taxa), 2)}.")
            valores.append(valor*(1+taxa))
    
    return '\n'.join(list)

print(calculo_de_juros_compostos(valor, taxa, periodo))
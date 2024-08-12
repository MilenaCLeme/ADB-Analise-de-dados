"""
1. Cálculo de Despesa com Desconto Progressivo
   **Problema:** Crie um programa que receba o custo de três produtos e calcule o valor total. Se o total exceder R$ 500, aplique um desconto progressivo: 10% se o total for entre R$ 500 e R$ 1.000, e 15% se for acima de R$ 1.000. Mostre o valor final após o desconto

"""

print("1. Cálculo de Despesa com Desconto Progressivo")
valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))
valor3 = float(input("Digite o terceiro valor: "))

def calculo_de_despesa_com_desconto_progressivo(valor_1, valor_2, valor_3):
    x = valor_1 + valor_2 + valor_3
    j = 0

    if x > 1000:
        j = x * 0.15
        print("Valor com desconto de 15% - R$", (x - j))
    elif 500 < x < 1000:
        j = x * 0.10
        print("Valor com desconto de 10% - R$", (x - j))
    else:
        print("Valor total é  R$", x)

calculo_de_despesa_com_desconto_progressivo(valor1, valor2, valor3)
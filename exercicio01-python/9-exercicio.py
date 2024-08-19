"""
9. Calculadora de Desconto com Condição de Pagamento
   **Problema:** Crie um programa que receba o valor de uma compra e determine o desconto a ser aplicado. Aplique 20% de desconto para compras acima de R$ 1.500, 10% para compras entre R$ 800 e R$ 1.500, e 5% para compras abaixo de R$ 800. Se o pagamento for à vista, aplique um desconto adicional de 5% sobre o valor final com desconto.    
"""

def calculadora_de_desconto_com_condicaao_de_pagamento(v):
    valor = v
    if v > 1500:
        valor -= valor * 0.20
    elif 1500 > v > 800:
        valor -= valor * 0.10
    else:
        valor -= valor * 0.05
        
    return valor

print(calculadora_de_desconto_com_condicaao_de_pagamento(5000))
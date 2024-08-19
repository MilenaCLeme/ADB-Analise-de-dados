"""
8. Comparação de Três Números com Verificação de Ordenação
   **Problema:** Desenvolva um programa que receba três números inteiros e determine qual é o maior e o menor. Além disso, verifique e informe se os números estão em ordem crescente, decrescente ou se não estão ordenados.    
"""

def verificarNumero(a,b,c):
    lst = [a, b, c]
    list_ordenada = sorted(lst)
    menor = list_ordenada[0]
    maior = list_ordenada[::-1][0]
    verificao_ordenacao = 'são crescente' if a < b < c else ('são decresente' if a > b > c else 'não são ordenados')
    
    return f"Os números {a}, {b} e {c}, podemos veririfcar que {verificao_ordenacao} e o maior é {maior} e o menor é {menor} "  

print(verificarNumero(10,20,30))
print(verificarNumero(20,50,60))
print(verificarNumero(100,22,90))
print(verificarNumero(80,60,30))

"""
Os números 10, 20 e 30, podemos veririfcar que são crescente e o maior é 30 e o menor é 10 
Os números 20, 50 e 60, podemos veririfcar que são crescente e o maior é 60 e o menor é 20 
Os números 100, 22 e 90, podemos veririfcar que não são ordenados e o maior é 100 e o menor é 22 
Os números 80, 60 e 30, podemos veririfcar que são decresente e o maior é 80 e o menor é 30    
    
"""
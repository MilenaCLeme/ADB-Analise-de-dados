"""
30. Somar Números em uma Lista
    - **Descrição:** Crie uma lista de números e calcule a soma de todos os números positivos usando um loop `for`.
"""

def somar_numero_em_uma_lista(lst):
    soma = 0
    
    for x in range(len(lst)):
        if lst[x] > 0:
            soma += lst[x]

    print(soma)
        
        
somar_numero_em_uma_lista([2,-5,3,6,8,9])
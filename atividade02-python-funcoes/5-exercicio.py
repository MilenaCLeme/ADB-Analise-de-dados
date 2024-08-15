"""
5. **Função de Divisão**:
   - Crie uma função chamada `divisao` que receba dois números como argumentos e retorne a divisão do primeiro pelo segundo.

"""

def divisao(a,b):
    return a / b if b != 0 else "Erro: Divisão por zero."

print(divisao(2,5)) 
print(divisao(10,50))
print(divisao(8,0))
print(divisao(5,9))

"""
0.4
0.2
Erro: Divisão por zero.
0.5555555555555556
"""
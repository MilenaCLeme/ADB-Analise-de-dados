"""
29. Verificar Paridade de Números
    - **Descrição:** Dado um número máximo fornecido pelo usuário, crie um programa que exiba todos os números de 1 até o máximo e informe se cada um é par ou ímpar.
"""

def paridade_de_numeros(m):
    for x in range(m):
        print(f"Esse numero {x} é {'par' if x % 2 == 0 else 'impar'}")

paridade_de_numeros(10)
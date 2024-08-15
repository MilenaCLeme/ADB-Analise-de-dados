"""


4. Cálculo de Média com Condição de Recuperação
   **Problema:** Desenvolva um programa que receba as notas de quatro provas e calcule a média. Se a média for menor que 5, informe que o aluno está reprovado. Se estiver entre 5 e 7, informe que o aluno está em recuperação, e se for maior ou igual a 7, informe que o aluno está aprovado.

"""

print("Cálculo de Média com Condição de Recuperação")

def calculo_de_media(nota_1, nota_2, nota_3, nota_4):
    media = ((nota_1 + nota_2 + nota_3 + nota_4) / 4)
    if media >= 7:
       print("Você está aprovado")
    elif 5 < media < 7:
        print("Você está de recuperação")
    else:
        print("Você está de recuperação")

nota1= int(input("Digite sua nota de 01 a 10: "))
nota2= int(input("Digite sua nota de 01 a 10: "))
nota3= int(input("Digite sua nota de 01 a 10: "))
nota4= int(input("Digite sua nota de 01 a 10: "))

calculo_de_media(nota1, nota2, nota3, nota4)

"""

Cálculo de Média com Condição de Recuperação
Digite sua nota de 01 a 10:5
Digite sua nota de 01 a 10:0
Digite sua nota de 01 a 10:5
Digite sua nota de 01 a 10:0
2.5
Você está de recuperação

Cálculo de Média com Condição de Recuperação
Digite sua nota de 01 a 10: 5
Digite sua nota de 01 a 10: 10
Digite sua nota de 01 a 10: 8
Digite sua nota de 01 a 10: 9
Você está aprovado

Cálculo de Média com Condição de Recuperação
Digite sua nota de 01 a 10: 5
Digite sua nota de 01 a 10: 9
Digite sua nota de 01 a 10: 6
Digite sua nota de 01 a 10: 4
Você está de recuperação

"""
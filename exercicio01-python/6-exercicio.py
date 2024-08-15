"""

6. Verificação de Ano Bissexto com Mensagens
   **Problema:** Desenvolva um programa que receba um ano e determine se ele é bissexto. Se for, informe que "O ano é bissexto e possui 366 dias." Caso contrário, informe que "O ano não é bissexto e possui 365 dias."

"""

ano_bissexto = lambda ano: ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)


def mensagem_ano_bissexto_e_nao(func, ano):
    if func(ano):
        return "O ano é bissexto e possui 366 dias." 
    else:    
        return "O ano não é bissexto e possui 365 dias."
    
ano = int(input("Digite um ano (YYYY): "))

print(mensagem_ano_bissexto_e_nao(ano_bissexto, ano))
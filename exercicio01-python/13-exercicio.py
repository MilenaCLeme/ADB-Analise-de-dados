"""

13. Número de Tentativas para Senha
   - **Descrição:** Crie um programa que limite o número de tentativas para digitar a senha correta. O usuário deve ter no máximo 3 tentativas. Use `while` e `if`.    
"""

def numero_tentativas_para_senha(senha_esperada):
    contador = 0
    
    while contador < 3:
        senha = input('Digite sua senha: ')
        
        contador += 1
        if senha_esperada == senha:
            print("Login autorizado")
            break
    
    if contador == 3:
        print('Limite maximo de 3 tentativas')
    
numero_tentativas_para_senha('Euamo')
    
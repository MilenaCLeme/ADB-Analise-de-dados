"""

1. **Função de Saudação**:
   - Crie uma função chamada `saudacao` que receba um nome como argumento e exiba uma mensagem de saudação no console.


"""

def saudacao(nome="Visitante"):
    return f"Olá, {nome}!"

# saudacao_mensagem

def saudacao_mensagem(nome="Visitante", mensagem="Bora codar"):
    return f"{mensagem}, {nome}"


print(saudacao())
print(saudacao_mensagem())
print(saudacao("Neto Russo"))
print(saudacao_mensagem("Neto Russo", "Amo você"))

"""
Olá, Visitante!
Bora codar, Visitante

Olá, Neto Russo!
Amo você, Neto Russo

"""
"""


7. Jogo da Velha
   - Escreva funções para implementar o jogo da velha, incluindo a verificação de vitória, empate, e a atualização do tabuleiro com cada jogada.


"""

def imprimir_tela(a='   ',b='   ',c='   ',d='   ',e='   ',f='   ',g='   ',h='   ',i='   '):
   print(f"    1   2   3 ")
   print(f"1  {a}|{b}|{c}")
   print(f"2  {d}|{e}|{f}")
   print(f"3  {g}|{h}|{i}")

def start_game():
   imprimir_tela()
   escolher_posicao()

list_posicao = {
   "a": '   ',
   "b": '   ',
   "c": '   ',
   "d": '   ',
   "e": '   ',
   "f": '   ',
   "g": '   ',
   "h": '   ',
   "i": '   ',
}

posicao = ['0']

def verificacao_vitoria():
   vitorias = [
      ['a', 'b', 'c'],
      ['d', 'e', 'f'],
      ['g', 'h', 'i'],
      ['a', 'd', 'g'],
      ['b', 'e', 'h'],
      ['c', 'f', 'i'],
      ['a', 'e', 'i'],
      ['c', 'e', 'g'],
   ]

   for linha in vitorias:
        if list_posicao[linha[0]] == list_posicao[linha[1]] == list_posicao[linha[2]] != '   ':
            return f"Vitoria do {list_posicao[linha[0]]}"
    
   if all(value != '   ' for value in list_posicao.values()):
        return "Empate"
    
   return False

def escolher_posicao():
   print("Analisando o jogo na Velha , escolha sua posição")
   primeira = int(input("Escolha sua primeira posição: "))
   segunda = int(input("Escolha sua segunda posição: "))

   if primeira == 1 and segunda == 1 and list_posicao["a"] == '   ':
      list_posicao['a'] = f" {posicao[len(posicao) - 1]} "
      imprimir_tela(list_posicao['a'], list_posicao['b'], list_posicao['c'], list_posicao['d'], list_posicao['e'], list_posicao['f'], list_posicao['g'], list_posicao['h'], list_posicao['i'])
      formado = 'X' if posicao[len(posicao) - 1] == '0' else '0'
      posicao.append(formado)
      vitoria = verificacao_vitoria()
      print(vitoria)
      if vitoria == False:
         escolher_posicao()
   elif primeira == 2 and segunda == 1 and list_posicao['b'] == '   ':
      list_posicao['b'] = f" {posicao[len(posicao) - 1]} "
      imprimir_tela(list_posicao['a'], list_posicao['b'], list_posicao['c'], list_posicao['d'], list_posicao['e'], list_posicao['f'], list_posicao['g'], list_posicao['h'], list_posicao['i'])
      formado = 'X' if posicao[len(posicao) - 1] == '0' else '0'
      posicao.append(formado)
      vitoria = verificacao_vitoria()
      print(vitoria)
      if vitoria == False:
         escolher_posicao()
   elif primeira == 3 and segunda == 1 and list_posicao['c'] == '   ':
      list_posicao['c'] = f" {posicao[len(posicao) - 1]} "
      imprimir_tela(list_posicao['a'], list_posicao['b'], list_posicao['c'], list_posicao['d'], list_posicao['e'], list_posicao['f'], list_posicao['g'], list_posicao['h'], list_posicao['i'])
      formado = 'X' if posicao[len(posicao) - 1] == '0' else '0'
      posicao.append(formado)
      vitoria = verificacao_vitoria()
      print(vitoria)
      if vitoria == False:
         escolher_posicao()
   elif primeira == 1 and segunda == 2 and list_posicao['d'] == '   ':
      list_posicao['d'] = f" {posicao[len(posicao) - 1]} "
      imprimir_tela(list_posicao['a'], list_posicao['b'], list_posicao['c'], list_posicao['d'], list_posicao['e'], list_posicao['f'], list_posicao['g'], list_posicao['h'], list_posicao['i'])
      formado = 'X' if posicao[len(posicao) - 1] == '0' else '0'
      posicao.append(formado)
      vitoria = verificacao_vitoria()
      print(vitoria)
      if vitoria == False:
         escolher_posicao()
   elif primeira == 2 and segunda == 2 and list_posicao['e'] == '   ':
      list_posicao['e'] = f" {posicao[len(posicao) - 1]} "
      imprimir_tela(list_posicao['a'], list_posicao['b'], list_posicao['c'], list_posicao['d'], list_posicao['e'], list_posicao['f'], list_posicao['g'], list_posicao['h'], list_posicao['i'])
      formado = 'X' if posicao[len(posicao) - 1] == '0' else '0'
      posicao.append(formado)
      vitoria = verificacao_vitoria()
      print(vitoria)
      if vitoria == False:
         escolher_posicao()
   elif primeira == 3 and segunda == 2 and list_posicao['f'] == '   ':
      list_posicao['f'] = f" {posicao[len(posicao) - 1]} "
      imprimir_tela(list_posicao['a'], list_posicao['b'], list_posicao['c'], list_posicao['d'], list_posicao['e'], list_posicao['f'], list_posicao['g'], list_posicao['h'], list_posicao['i'])
      formado = 'X' if posicao[len(posicao) - 1] == '0' else '0'
      posicao.append(formado)
      vitoria = verificacao_vitoria()
      print(vitoria)
      if vitoria == False:
         escolher_posicao()
   elif primeira == 1 and segunda == 3 and list_posicao['g'] == '   ':
      list_posicao['g'] = f" {posicao[len(posicao) - 1]} "
      imprimir_tela(list_posicao['a'], list_posicao['b'], list_posicao['c'], list_posicao['d'], list_posicao['e'], list_posicao['f'], list_posicao['g'], list_posicao['h'], list_posicao['i'])
      formado = 'X' if posicao[len(posicao) - 1] == '0' else '0'
      posicao.append(formado)
      vitoria = verificacao_vitoria()
      print(vitoria)
      if vitoria == False:
         escolher_posicao()
   elif primeira == 2 and segunda == 3 and list_posicao['h'] == '   ':
      list_posicao['h'] = f" {posicao[len(posicao) - 1]} "
      imprimir_tela(list_posicao['a'], list_posicao['b'], list_posicao['c'], list_posicao['d'], list_posicao['e'], list_posicao['f'], list_posicao['g'], list_posicao['h'], list_posicao['i'])
      formado = 'X' if posicao[len(posicao) - 1] == '0' else '0'
      posicao.append(formado)
      vitoria = verificacao_vitoria()
      print(vitoria)
      if vitoria == False:
         escolher_posicao()
   elif primeira == 3 and segunda == 3 and list_posicao['i'] == '   ':
      list_posicao['i'] = f" {posicao[len(posicao) - 1]} "
      imprimir_tela(list_posicao['a'], list_posicao['b'], list_posicao['c'], list_posicao['d'], list_posicao['e'], list_posicao['f'], list_posicao['g'], list_posicao['h'], list_posicao['i'])
      formado = 'X' if posicao[len(posicao) - 1] == '0' else '0'
      posicao.append(formado)
      vitoria = verificacao_vitoria()
      print(vitoria)
      if vitoria == False:
         escolher_posicao()
   
start_game()
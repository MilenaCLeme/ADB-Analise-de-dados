"""
1 - Crie um DataFrame com as colunas nome, idade, altura, peso e sexo usando listas.
"""

import pandas as pd

lst = [['Milena', 30, 1.52, 77, 'F'], ['Neto', 35, 1.98, 130, 'M'], ['Nair', 50, 1.49, 49, 'F'], ['Amora', 4, 1.00, 30, 'F'], ['Romeu', 5, 1.00, 10, 'M']]

data = pd.DataFrame(lst, columns=['Nome', 'Idade', 'Altura', 'Peso', 'Sexo'])

"""
2 - Exiba o DataFrame criado.
"""

# print(data)

"""
3 - Selecione e exiba a coluna "idade" do DataFrame.
"""

idade = data['Idade']

# print(idade)

"""
4 - Selecione e exiba a linha com índice 2 do DataFrame.
"""

linha_2 = data.iloc[2]

# print(linha_2)

"""
5 - Selecione e exiba a linha com rótulo 2 do DataFrame.
"""

rotulo_2 = data.loc[2]

#print(rotulo_2)

"""
6 - Selecione e exiba o valor da célula na linha de rótulo 3, coluna "altura".
"""

linha_3_valor_altura = data.iloc[3]['Altura']

#print(linha_3_valor_altura)

"""
7 - Renomeie as colunas "sexo" para "genero" e "peso" para "massa".
"""

data.rename(columns={"Sexo": "Genero", "Peso": "Massa"}, inplace=True)

#print(data)

"""
8 - Selecione e exiba as colunas "nome" e "altura" do DataFrame.
"""

colunas_selecionado_nome_e_altura = data[['Nome', 'Idade']]

#print(colunas_selecionado_nome_e_altura)

"""
9 - Filtre e exiba todas as linhas onde a idade é maior que 40.
"""

linha_filtra = data[data['Idade'] > 40]

#print(linha_filtra)

"""
10 - Adicione uma nova coluna chamada "IMC" ao DataFrame, calculando o Índice de Massa Corporal.
"""

data['IMC'] = round(((data['Massa'] / data['Altura']) / data['Altura']), 2)

#print(data)

"""
11 - Ordene o DataFrame pela coluna "altura" em ordem crescente.
"""

ordem_crescente_altura = data.sort_values(by='Altura')

#print(ordem_crescente_altura)

"""
12 - Filtre e exiba todas as linhas onde a altura é  maior que 1.65.
"""

linha_filtra_altura = data[data['Altura'] > 1.65]

#print(linha_filtra_altura)

"""
13 - Modifique a altura de alguém para 1.91 e exiba o DataFrame.
"""

data.loc[data['Nome'] == 'Romeu', 'Altura'] = 1.91

#print(data)

"""
14 - Crie uma coluna com valores de CPF para cada linha
"""

data['CPF'] = '111.111.111-11'

#print(data)

"""
15 - Exclua a coluna CPF do DataFrame.
"""

data = data.drop(columns='CPF')

#print(data)

"""
16 - Resete o índice do DataFrame e exiba o resultado.
"""

novo_index = data.set_index('Nome', inplace=True)

resetado = data.reset_index()

"""
17 - Exiba as linhas do DataFrame onde a altura é maior que 1.70.
"""

linha_filtro_altura_maior = data[data['Altura'] > 1.70]

#print(linha_filtro_altura_maior)

"""
18 - Selecione e exiba as colunas "nome" e "genero".
"""

novo = data[['Nome', 'Genero']]

"""
19 - Calcule e exiba a soma das idades.
"""

soma_das_idades = data['Idade'].sum()

#print(soma_das_idades)

"""
20 - Salve o DataFrame em um arquivo CSV.
"""

data.to_csv('exercicio03-python-panda/data.csv')



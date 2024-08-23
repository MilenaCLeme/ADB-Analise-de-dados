import pandas as pd

dados = pd.read_csv('./atividade03-python-panda/dados.csv')

# Visualizar as primeiras linhas
#print(dados.head())

# 1. Quais são os funcionários mais jovens?

mais_jovem = dados[dados['Idade'] == dados['Idade'].min()]

mais_jovem.to_csv('atividade03-python-panda/Funcionarios/funcionariosmaisjovem.csv')

# 2. Quais são os funcionários mais velhos?

mais_velho = dados[dados['Idade'] == dados['Idade'].max()]

mais_velho.to_csv('atividade03-python-panda/Funcionarios/funcionariosmaisvelho.csv')

# 3 . Quais são os funcionários com mais anos trabalhados na empresa?

funcionario_mais_ano_de_trabalho = dados[dados['Total de anos trabalhados na empresa'] == dados['Total de anos trabalhados na empresa'].max()]

funcionario_mais_ano_de_trabalho.to_csv('atividade03-python-panda/Funcionarios/funcionariosmaisantigosdaempresa.csv')

# 4. Ordenar por idade

ordenar_idade = dados.sort_values(by='Idade', ascending=True)

ordenar_idade.to_csv('atividade03-python-panda/Funcionarios/ordenarporidade.csv')

# 5. Quais são os funcionários com o maior salário mensal?

salarios_maior = dados[dados['Salário Mensal'] == dados['Salário Mensal'].max()]

salarios_maior.to_csv('atividade03-python-panda/Funcionarios/salariosmaior.csv')

# 6. Soma de todas as colunas de Salário, Renda mensal e Salário por hora

total = dados.drop(columns=['Demissão', 'Viagem de negócios', 'Departamento', 'Área de Formação', 'Gênero', 'Cargo', 'Estado civil', 'Maior de idade', 'Faz hora extra'])

total = total.sum(axis=0)

colunas = ['Salário por hora', 'Salário Mensal', 'Renda mensal']

selecionados = total[colunas]

selecionados.to_csv('atividade03-python-panda/Salários/valorestotalderendasalarios.csv')

# 7. Qual é a lista dos 5 funcionários mais velhos com salário mensal acima de R$4000?

salario_acima_4000 = dados[dados['Salário Mensal'] > 4000]

funcionario_mais_velho = salario_acima_4000.sort_values(by='Idade', ascending=False)

funcionario_mais_velho.to_csv('atividade03-python-panda/Funcionarios/funcionariomaisvelhocomsalarioacimade4000.csv')

# 8 . Qual é o salário mensal médio dos funcionários que estão insatisfeitos com o trabalho (nível de satisfação 'Baixa') e têm mais de 5 anos de empresa?

salario_mensal_insatisfeitos_cinco_anos = dados[(dados['Nível de Satisfação com o ambiente de trabalho'] == 1) & (dados['Total de anos trabalhados na empresa'] > 5)]

salario_mensal_insatisfeitos_cinco_anos = salario_mensal_insatisfeitos_cinco_anos[['Idade', 'Nível de Satisfação com o ambiente de trabalho', 'Total de anos trabalhados na empresa', 'Salário Mensal']]

salario_mensal_insatisfeitos_cinco_anos['media'] = round(salario_mensal_insatisfeitos_cinco_anos['Salário Mensal'].mean())

salario_mensal_insatisfeitos_cinco_anos.to_csv('atividade03-python-panda/Salários/salariomensalinsatisfeitoscincoanos.csv')

# Agrupamento por Departamento
# 9. Qual é a média de idade dos funcionários em cada departamento?

mean_year_dp = dados.groupby('Departamento').agg(
    media_idade=('Idade', 'mean')
)

mean_year_dp.to_csv('atividade03-python-panda/Departamentos/mediadeidadepordepartamento.csv')

# 10. Qual o salário mensal médio e a satisfação com o trabalho em cada departamento?

def satisfacao(x):
    if x == 1:
        return 'Baixa'
    elif x == 2:
        return 'Média'
    elif x == 3:
        return 'Alta'
    elif x == 4:
        return 'Muito Alta'
    else:
        return 'Não identificada'

dados['Nível de Satisfação com o ambiente de trabalho'] = dados['Nível de Satisfação com o ambiente de trabalho'].apply(satisfacao)

mean_salario_dp_satisfacao = dados.groupby(['Departamento', 'Nível de Satisfação com o ambiente de trabalho']).agg(
    media_salario=('Salário Mensal', 'mean'),
    quantidade=('Salário Mensal', 'size') 
)

mean_salario_dp_satisfacao.to_csv('atividade03-python-panda/Departamentos/salariomedioporniveldesatisfacaopordepartamento.csv')

# 11. Qual é o percentual de funcionários que fazem hora extra em cada departamento?
hora_extra_quantidade = dados.groupby(['Departamento', 'Faz hora extra']).size().reset_index(name='Quantidade')

contagem_total_dp = dados.groupby(['Departamento']).size().reset_index(name='Total')

resultado = pd.merge(hora_extra_quantidade, contagem_total_dp, on='Departamento')

def percentual(x):
    return f"{round((x['Quantidade'] / x['Total']) * 100)}%"

resultado['Percentual'] = resultado.apply(percentual, axis=1)

resultado = resultado.drop(columns=['Total'])

resultado.to_csv('atividade03-python-panda/Departamentos/percentualdefuncionariosquefazemhoraextra.csv')

# 12. Quantos funcionários de cada departamento têm maior de idade?

quantidade_funcionario_maior_idade = dados.groupby(['Departamento', 'Maior de idade']).size().reset_index(name='Quantidade')

quantidade_funcionario_maior_idade.to_csv('atividade03-python-panda/Departamentos/quantidadefuncionariomaioridade.csv')

# Agrupamento por Escolaridade:

# 13. Qual é a média salarial por nível de escolaridade?

def escolaridade(x):
    if x == 1:
        return 'Abaixo da faculdade'
    elif x == 2:
        return 'Faculdade'
    elif x == 3:
        return 'Bacharelado'
    elif x == 4:
        return 'Mestre'
    elif x == 5:
        return 'Doutor'
    else:
        return 'Não informato'

dados['Escolaridade'] = dados['Escolaridade'].apply(escolaridade)

mean_salario_por_nivel = dados.groupby(['Escolaridade']).agg(
    media_salario=('Salário Mensal', 'mean')
)

mean_salario_por_nivel.to_csv('atividade03-python-panda/Funcionarios/escolaridade/mediasalarialpornivelescolaridade.csv')

# 14. Qual é a média de satisfação com o trabalho para cada nível de escolaridade?

def satisfacao_para_numero(x):
    if x == 'Baixa':
        return 1
    elif x == 'Média':
        return 2
    elif x == 'Alta':
        return 3
    elif x == 'Muito Alta':
        return 4
    else:
        return 0
    
dados['Nível de Satisfação com o ambiente de trabalho'] = dados['Nível de Satisfação com o ambiente de trabalho'].apply(satisfacao_para_numero)

mean_satisfacao_por_escolaridade = dados.groupby(['Escolaridade']).agg(
    total_satisfacao=('Nível de Satisfação com o ambiente de trabalho', 'sum'),
    quantidade=('Escolaridade', 'size')
)

mean_satisfacao_por_escolaridade['mean_satisfacao'] = mean_satisfacao_por_escolaridade['total_satisfacao'] / mean_satisfacao_por_escolaridade['quantidade']

mean_satisfacao_por_escolaridade.to_csv('atividade03-python-panda/Funcionarios/escolaridade/mediasatisfacaoporescolaridade.csv')

#15. Quantos funcionários com diferentes níveis de escolaridade pediram demissão?

demissao_quantidade = dados.groupby(['Escolaridade', 'Demissão']).agg(
    quantidade=('Demissão', 'size')
)

demissao_quantidade.to_csv('atividade03-python-panda/Funcionarios/escolaridade/funcionariocomdiferentesniveisdeescolaridadepediramdemissao.csv')

# Agrupamento por Gênero

# 16. Qual é a renda mensal média por gênero?

renda_mensal_genero = dados.groupby(['Gênero']).agg(
    mean_renda_mensal=('Renda mensal','mean')
)

renda_mensal_genero['mean_renda_mensal'] = round(renda_mensal_genero['mean_renda_mensal'], 2)

renda_mensal_genero.to_csv('atividade03-python-panda/Funcionarios/genero/rendamensalmediaporgenero.csv')

# 17. Quantos funcionários de cada gênero fazem hora extra?

funcionario_cada_genero_fazem_hora_extra = dados.groupby(['Gênero', 'Faz hora extra']).agg(
    quantidade=('Faz hora extra', 'size')
)

funcionario_cada_genero_fazem_hora_extra.to_csv('atividade03-python-panda/Funcionarios/genero/horaextraseparadosporgeneros.csv')

# Agrupamento por Idade:

# 18. Qual é a média salarial para diferentes faixas etárias (Ex: < 30 anos, 30-40 anos, > 40 anos)?

bins=[0, 30, 40, 100]
labels=['< 30 anos', '30-40 anos', '> 40 anos']

faixa_etaria = dados

faixa_etaria['Faixa Etária'] = pd.cut(dados['Idade'], bins=bins, labels=labels, right=False)

novo = faixa_etaria.groupby(['Faixa Etária'], observed=True).agg(
    salario_mean=('Salário Mensal', 'mean'),
    quantidade_funcionarios=('Salário Mensal', 'size')
)

novo['salario_mean'] = round(novo['salario_mean'], 2)

novo.to_csv('atividade03-python-panda/Funcionarios/idade/mediasalarialpordiferentesestarias.csv')

#19. Como varia a satisfação nas relações de trabalho entre diferentes faixas etárias?

satisfacao_faixa_etaria = faixa_etaria.groupby(['Faixa Etária', 'Nível de Satisfação com o ambiente de trabalho'], observed=False).size().reset_index(name='Quantidade')

satisfacao_faixa_etaria = satisfacao_faixa_etaria.rename(columns={'Nível de Satisfação com o ambiente de trabalho': 'Satisfação pelo trabalho'})

satisfacao_faixa_etaria['Satisfação pelo trabalho'] = satisfacao_faixa_etaria['Satisfação pelo trabalho'].apply(satisfacao)

satisfacao_faixa_etaria.to_csv('atividade03-python-panda/Satisfacao/satisfacaoporidade.csv')


# 20. Qual é a média de satisfação com o trabalho para diferentes grupos de anos trabalhados na empresa (Ex: < 5 anos, 5-10 anos, > 10 anos)?

bins=[0, 5, 10, 100]
labels=['< 5 anos', '5-15 anos', '> 10 anos']

faixa_anos_trabalhados = dados

faixa_anos_trabalhados['Faixa Anos Trabalhados'] = pd.cut(dados['Total de anos trabalhados na empresa'], bins=bins, labels=labels, right=False)

faixa_anos_trabalhados['Nível de Satisfação com o ambiente de trabalho'] = faixa_anos_trabalhados['Nível de Satisfação com o ambiente de trabalho'].apply(satisfacao)

satisfacao_faixa_anos_trabalhados = faixa_anos_trabalhados.groupby(['Faixa Anos Trabalhados', 'Nível de Satisfação com o ambiente de trabalho'], observed=True).agg(
    total_funcionario=('Nível de Satisfação com o ambiente de trabalho', 'size')
)

satisfacao_faixa_anos_trabalhados.to_csv('atividade03-python-panda/Satisfacao/mediadesatisfacaoporanodaempresa.csv')



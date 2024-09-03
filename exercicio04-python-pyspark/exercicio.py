"""
Olá Pessoal,

Boa Tarde,

A atividade de hoje é sobre uma base de dados que já utilizamos em projetos anteriores com outras ferramentas e tecnologias.
A base encontra-se já disponível anteriormente sobre funcionários, e a atividade é a seguinte:

1 - Baixe a base em sua máquina no formato .csv;
2 - Abra um novo colab e crie uma nova seção PySpark;
3 - Suba a base da máquina para seu ambiente Pyspark no Colab;
4 - Elabore Análises com filtros e agrupamentos aprendidos em PySpark na aula de ontem;
5 - Cada filtro ou agrupamento que você realizar deve estar acompanhado (no bloco de código do respectivo colab) de um comentário sobre qual  pergunta essas dados filtrados ou agrupados tentam responder sobre essa base;
6 - Cada filtro ou agrupamento deverá ser salvo em um objeto PySpark e depois convertido em um objeto Pandas, ao longo
do dia você deverá realizar no mínimo 20 tabelas resultantes dessas análises;
7 - Após isso, as tabelas pandas deverão ser enviadas diretamente do colab para arquivos csv.
8 - O formato de entrega é o próprio link, ou arquivo ypynb do colab

Bom trabalho,

Abraços
"""


# 1 - Baixe a base em sua máquina no formato .csv; Ok (Tabela Dados)

# 2 - Abra um novo colab e crie uma nova seção PySpark;
from pyspark.sql import SparkSession
from pyspark.sql import functions as F 
import pandas as pd


spark = SparkSession.builder.appName('Introducao').getOrCreate()

#print(spark)

# 3 - Suba a base da máquina para seu ambiente Pyspark no Colab;

dados = spark.read.csv('exercicio04-python-pyspark/dados.csv', header=True, inferSchema=True)

#dados.show()

# 4 - Elabore Análises com filtros e agrupamentos aprendidos em PySpark na aula de ontem;

# Filtros 

dados_filtered_idade = dados.filter(dados['Idade'] == 30)

dados_where_idade = dados.where(dados['Idade'] > 30)

# Agrupamentos count , sum , avg 

dados_grupos_departamentos = dados.groupBy('Departamento').agg(
    F.count("*").alias("total_departamentos"),
    F.avg("Salário Mensal").alias("avg Salário"),
    F.max("Salário Mensal").alias("avg Salário")
)

# dados_grupos_departamentos.show()

# Ordenação

ordenar_por_salario = dados.orderBy("Salário Mensal", ascending=False)

# Select

teste_coluna_idade = dados.filter(dados['Idade'] > 30).select('ID Funcionário', 'Idade', 'Gênero')


# 5 - Cada filtro ou agrupamento que você realizar deve estar acompanhado (no bloco de código do respectivo colab) de um comentário sobre qual  pergunta essas dados filtrados ou agrupados tentam responder sobre essa base;

# Quantos funcionários em cada departamento têm mais de 5 anos de experiência?

quantidade_funcionarios_com_mais_de_5_anos = dados.filter(dados['Total de anos trabalhados na empresa'] > 5)

groupo_de_quantidade_f_por_5_anos = quantidade_funcionarios_com_mais_de_5_anos.groupBy('Departamento').agg(
    F.count('*').alias('total_departamento')
)


#6 - Cada filtro ou agrupamento deverá ser salvo em um objeto PySpark e depois convertido em um objeto Pandas, ao longo do dia você deverá realizar no mínimo 20 tabelas resultantes dessas análises;


# 1 - Quantos funcionários acima de 30 anos ?

filter_acima_30 = dados.filter(dados['Idade'] > 30)

converter_pandas1 = filter_acima_30.toPandas()

#converter_pandas1.to_csv('exercicio04-python-pyspark/tabelas/filteracima30.csv')

# 2 - Quantos funcionários com mais de 5 km  de distancia de casa ?

filtered_distancia_de_5km = dados.filter(dados['Distância de Casa'] > 5)

converter_pandas = filtered_distancia_de_5km.toPandas()

#converter_pandas.to_csv('exercicio04-python-pyspark/tabelas/filterdistanciade5km.csv')

# 3 -  Agrupar por Departamento e calcular salário médio

agrupar_po_dp = dados.groupBy('Departamento').agg(
    F.avg('Salário Mensal'),
    F.max('Salário Mensal'),
    F.min('Salário Mensal')
)

converter_pandas3 = agrupar_po_dp.toPandas()

#converter_pandas3.to_csv('exercicio04-python-pyspark/tabelas/agrupardepartamento.csv')

# 4 - Qual é a média de Nível de Satisfação com o ambiente de trabalho por faixa etária?

media_nivel_satisfacao = dados.withColumn('Faixa Etária', F.when(F.col('Idade') <= 30, 'Jovem Adulto').when((F.col('Idade') > 30) & (F.col('Idade') < 50), 'Adulto').otherwise('Sênior'))

media_satisfacao = media_nivel_satisfacao.groupBy('Faixa Etária').agg(
    F.avg('Nível de Satisfação com o ambiente de trabalho').alias('Média de Nível De Satisfação com o ambiente de trabalho')
)

media_satisfacao_converter = media_satisfacao.toPandas()

#media_satisfacao_converter.to_csv('exercicio04-python-pyspark/tabelas/mediasatisfacao.csv')

# 5 -  Qual é a média do Nível de envolvimento com o trabalho por faixa de Distância de Casa?

faixa_de_distancia_de_casa = dados.withColumn('Faixa de Distância de Casa', F.when(F.col('Distância de Casa') < 5, 'Distancia Curta até 5 Km').when((F.col('Distância de Casa') > 5) & (F.col('Distância de Casa') < 20), 'Distancia Média entre 6 a 20 Km').otherwise('Distancia Longa acima de 20 Km'))

media_de_envolvimento_com_trabalho = faixa_de_distancia_de_casa.groupBy('Faixa de Distância de Casa').agg(
    F.avg('Nível de envolvimento com o trabalho').alias('Média Do Nível de envolvimento com o trabalho')
)

media_de_envolvimento_com_trabalho_converter = media_de_envolvimento_com_trabalho.toPandas()

#media_de_envolvimento_com_trabalho_converter.to_csv('exercicio04-python-pyspark/tabelas/mediadeenvolvimentocomtrabalho.csv')

# 6. Filtrar funcionários que foram demitidos e que fizeram viagens de negócios

filtrar_demissao_viagem = dados.filter((dados['Demissão'] == 'Sim') & (dados['Viagem de negócios'] == 'Sim'))

converter_pandas4 = filtrar_demissao_viagem.toPandas()

#converter_pandas4.to_csv('exercicio04-python-pyspark/tabelas/viagemdemissao.csv')

# 7. Agrupar por Gênero e calcular a média do salário por hora

agrupar_genero = dados.groupBy('Gênero').agg(
    F.avg('Salário por hora'),
    F.stddev('Salário por hora'),
    F.median('Salário por hora'),
    F.max('Salário por hora'),
    F.min('Salário por hora')
)

converter_pandas5 = agrupar_genero.toPandas()

#converter_pandas5.to_csv('exercicio04-python-pyspark/tabelas/agrupargenero.csv')

# 8 . Filtrar por Jornada padrão de trabalho e Maior de idade

jornada_idade_maior_idade = dados.filter((dados['Jornada padrão de trabalho'] == 'Sim') & (dados['Maior de idade'] == 'Sim'))

converter_pandas6 = jornada_idade_maior_idade.toPandas()

#converter_pandas6.to_csv('exercicio04-python-pyspark/tabelas/jornadaidademaior.csv')

# 9. Agrupar por Estado civil e calcular o total de anos trabalhados na empresa

agrupar_estado_civil = dados.groupBy('Estado civil').agg({'Total de anos trabalhados na empresa': 'sum'})

converter_pandas7 = agrupar_estado_civil.toPandas()

#converter_pandas7.to_csv('exercicio04-python-pyspark/tabelas/agruparestadocivil.csv')

# 10. Filtrar por Satisfação com o trabalho maior que 4 e Estado civil igual a "Solteiro"

filtrar_stisfacao = dados.filter((dados['Satisfação com o trabalho'] > 4) & (dados['Estado civil'] == 'Solteiro'))

converter_pandas8 = filtrar_stisfacao.toPandas()

#converter_pandas8.to_csv('exercicio04-python-pyspark/tabelas/filtrar_satisfacao.csv')

# 11 - Agrupar por Área de Formação e calcular o número de contratos de trabalho na empresa

agrupar_area_de_formacao = dados.groupBy('Área de Formação').agg(
    F.sum('Número de contratos de trabalho na empresa'),
)

converter_pandas9 = agrupar_area_de_formacao.toPandas()

#converter_pandas9.to_csv('exercicio04-python-pyspark/tabelas/converteragruparcivil.csv')

# 12 - Filtrar por Faz hora extra e percentual de aumento de salário maior que 10%

filtrar_hora_extra_aumento = dados.filter((dados['Faz hora extra'] == 'Sim') & (dados['percentual de aumento de salário'] > 10))

converter_pandas10 = filtrar_hora_extra_aumento.toPandas()

#converter_pandas10.to_csv('exercicio04-python-pyspark/tabelas/converteragruparcivil.csv')

# 13 - Agrupar por Cargo e calcular o score de performance médio

agrupar_cargo_performance = dados.groupBy('Cargo').agg(F.mean('score de performance')).alias('media_score_performance')

converter_pandas11 = agrupar_cargo_performance.toPandas()

#converter_pandas11.to_csv('exercicio04-python-pyspark/tabelas/agruparcargoperfomance.csv')

# 14 - Agrupar por Gênero e Estado civil e calcular a Renda mensal média

agruparestados = dados.groupBy(['Gênero', 'Estado civil']).agg(F.mean('Renda mensal')).alias('media_renda_mensal')

converter_pandas12 = agruparestados.toPandas()

#converter_pandas12.to_csv('exercicio04-python-pyspark/tabelas/agruparestados.csv')

# 15 - Filtrar por Equilíbrio vida trabalho menor que 3

filtrar_baixo_esquilibrio = dados.filter(dados['Equilíbrio vida trabalho'] < 3)

converter_pandas13 = filtrar_baixo_esquilibrio.toPandas()

#converter_pandas13.to_csv('exercicio04-python-pyspark/tabelas/filtrarbaixoesquilibro.csv')

# 16 - Agrupar por Departamento e calcular a média de Anos trabalhados na função atual

agrupar_departamento_funcao = dados.groupBy('Departamento').agg({'Anos trabalhados na função atual': 'mean'})

converter_pandas14 = agrupar_departamento_funcao.toPandas()

#converter_pandas14.to_csv('exercicio04-python-pyspark/tabelas/agrupardepartamentofuncao.csv')

# 17 - Filtrar por Renda mensal maior que 8000 

filtro_renda_alta = dados.filter(dados["Renda mensal"] > 8000)

converter_pandas14 = filtro_renda_alta.toPandas()

#converter_pandas14.to_csv('exercicio04-python-pyspark/tabelas/filtrorendaalta.csv')

# 18 - Agrupar por Nível hierárquico e calcular o Total de anos trabalhados

agrupamento_nivel_anos = dados.groupBy("Nível hierárquico").agg({"Total de anos trabalhados": "sum"})

converter_pandas15 = agrupamento_nivel_anos.toPandas()

#converter_pandas15.to_csv('exercicio04-python-pyspark/tabelas/agrupamentonivelanos.csv')

# 19 - Filtrar por quantidade de empresas que já trabalhou maior que 3

filtro_varias_empresas = dados.filter(dados["qtde de empresas que já trabalhou"] > 3)

converter_pandas16 = filtro_varias_empresas.toPandas()

#converter_pandas16.to_csv('exercicio04-python-pyspark/tabelas/filtro_varias_empresas.csv')

# 20 - Qual é a proporção de funcionários que estão Satisfeitos com o trabalho entre aqueles que Fazem hora extra e os que não fazem?

# - Satisfação com o trabalho - Faz hora extra

satisfacao_percentual_com_horas_extra = dados.groupBy(['Faz hora extra', 'Satisfação com o trabalho']).agg(
    F.sum(F.when(F.col('Faz hora extra') == 'Sim', 1).otherwise(0)).alias('Quantidade Faz Hora Extra'),
    F.sum(F.when(F.col('Faz hora extra') == 'Não', 1).otherwise(0)).alias('Quantidade Não Faz Hora Extra'),
    F.count('Satisfação com o trabalho').alias('Quantidade de pessoas')
)

satisfacao_percentual_com_horas_extra_coluna = satisfacao_percentual_com_horas_extra.withColumn('Satisfação com o trabalho', F.when((F.col('Satisfação com o trabalho') == 1) | (F.col('Satisfação com o trabalho') == 2), 'Baixa Satisfação').otherwise('Alta Satisfação'))

satisfacao_percentual_com_horas_extra_novo_grupo = satisfacao_percentual_com_horas_extra_coluna.groupBy(['Faz hora extra','Satisfação com o trabalho']).agg(
    F.sum('Quantidade Faz Hora Extra').alias('Total Faz Hora Extra'),
    F.sum('Quantidade Não Faz Hora Extra').alias('Total Não Faz Hora Extra'),
)

converter_pandas17 = satisfacao_percentual_com_horas_extra_novo_grupo.toPandas()

converter_pandas17.to_csv('exercicio04-python-pyspark/tabelas/satisfacaocomhorasexta.csv')

# 7 - Após isso, as tabelas pandas deverão ser enviadas diretamente do colab para arquivos csv.

# ok


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

# 1 - Quantos funcionários com mais de 5 km  de distancia de casa ?

filtered_distancia_de_5km = dados.filter(dados['Distância de Casa'] > 5)

converter_pandas = filtered_distancia_de_5km.toPandas()

# converter_pandas.to_csv('exercicio04-python-pyspark/tabelas/filterdistanciade5km.csv')

# 2 - Qual é a média de Nível de Satisfação com o ambiente de trabalho por faixa etária?

media_nivel_satisfacao = dados.withColumn('Faixa Etária', F.when(F.col('Idade') <= 30, 'Jovem Adulto').when((F.col('Idade') > 30) & (F.col('Idade') < 50), 'Adulto').otherwise('Sênior'))

media_satisfacao = media_nivel_satisfacao.groupBy('Faixa Etária').agg(
    F.avg('Nível de Satisfação com o ambiente de trabalho').alias('Média de Nível De Satisfação com o ambiente de trabalho')
)

media_satisfacao_converter = media_satisfacao.toPandas()

# media_satisfacao_converter.to_csv('exercicio04-python-pyspark/tabelas/mediasatisfacao.csv')

# 3 -  Qual é a média do Nível de envolvimento com o trabalho por faixa de Distância de Casa?

faixa_de_distancia_de_casa = dados.withColumn('Faixa de Distância de Casa', F.when(F.col('Distância de Casa') < 5, 'Distancia Curta até 5 Km').when((F.col('Distância de Casa') > 5) & (F.col('Distância de Casa') < 20), 'Distancia Média entre 6 a 20 Km').otherwise('Distancia Longa acima de 20 Km'))

media_de_envolvimento_com_trabalho = faixa_de_distancia_de_casa.groupBy('Faixa de Distância de Casa').agg(
    F.avg('Nível de envolvimento com o trabalho').alias('Média Do Nível de envolvimento com o trabalho')
)

media_de_envolvimento_com_trabalho_converter = media_de_envolvimento_com_trabalho.toPandas()

# media_de_envolvimento_com_trabalho_converter.to_csv('exercicio04-python-pyspark/tabelas/mediadeenvolvimentocomtrabalho.csv')

# 4 - Qual é a proporção de funcionários que estão Satisfeitos com o trabalho entre aqueles que Fazem hora extra e os que não fazem?

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

satisfacao_percentual_com_horas_extra_novo_grupo.show()



# 7 - Após isso, as tabelas pandas deverão ser enviadas diretamente do colab para arquivos csv.



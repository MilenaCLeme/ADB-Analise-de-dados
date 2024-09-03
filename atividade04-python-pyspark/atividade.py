from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.types import StringType
from pyspark.sql.types import FloatType
from pyspark.sql.types import IntegerType
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.regression import LinearRegression
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.evaluation import BinaryClassificationEvaluator
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns
import re
import pandas as pd
from scipy import stats

spark = SparkSession.builder.appName('Atividade').config("spark.jars.packages", "com.crealytics:spark-excel_2.12:0.13.5").getOrCreate()

dados = spark.read.format("com.crealytics.spark.excel").option("inferSchema", "True").option("header", "True").option("sheetName", "Sheet1").load('atividade04-python-pyspark/base_suja.xlsx')

dados_new = dados.dropna(how="all")

"""
1. Análise de Consistência de Dados: Identificar e corrigir inconsistências nos valores de &quot;Área&quot; e
&quot;Status de Emprego&quot; (e.g., diferenças de maiúsculas/minúsculas).

"""
columns = ['Área', 'Status de Emprego']

for column in columns:
    dados_new = dados_new.withColumn(column, F.lower(F.col(column)))
    
# dados_new.show()

"""

2. Limpeza de Dados Faltantes: Detectar e tratar os valores ausentes na coluna &quot;Idade&quot; e &quot;Área&quot;.

"""

dados_new = dados_new.fillna({
    "Idade": 28,
    "Área": "desconhecido",
    "Salário": 0,
    "Data de Contratação": '00/00/0000'
})

def corrigir_por_letra(valor):
    if valor.startswith('f'):
        return 'financeiro'
    elif valor.startswith('r'):
        return 'rh'
    elif valor.startswith('m'):
        return 'marketing'
    else:
        return 'desconhecido'

corrigir_area = F.udf(corrigir_por_letra, StringType())

dados_new = dados_new.withColumn('Área', corrigir_area(F.col('Área')))

# dados_new.show()

def verificar_formato_dato(valor):
    formatos = ['%d/%m/%Y', '%d-%m-%Y', '%Y/%m/%d', '%d.%m.%Y']
    for formato in formatos:
        try:
            datetime.strptime(valor, formato)
            return formato
        except:
            continue
    
    return None
    

def transformar_data(data):
    formato_data = verificar_formato_dato(data)
    
    if formato_data is not None:
        nova_data = datetime.strptime(data, formato_data)
        return f"{nova_data.day:02d}/{nova_data.month:02d}/{nova_data.year}"
    else:
        return ''

corrigir_data = F.udf(transformar_data, StringType())

dados_new = dados_new.withColumn('Data de Contratação', corrigir_data(F.col('Data de Contratação')))

def remover_letras_converter_float(valor):
    if valor is not None:
        valor_limpo = re.sub(r'[a-zA-Z$]', '', valor)
        try:
            return float(valor_limpo)
        except:
            return None
    
    return None


corrigir_salario = F.udf(remover_letras_converter_float, FloatType())

dados_new = dados_new.withColumn('Salário', corrigir_salario(F.col('Salário')))

#dados_new.show()

"""
3. Distribuição de Idade: Analisar a distribuição da idade dos funcionários por departamento.
"""

distribuicao_de_idade_por_pd = dados_new.groupBy("Área").agg(
    F.avg("Idade").alias('Média'),
    F.stddev("Idade").alias('Descio Padrão'),
    F.min('Idade').alias('Mínimo'),
    F.max('Idade').alias('Máximo'),
)

# distribuicao_de_idade_por_pd.show()

"""
4. Salário por Departamento: Calcular a média, mediana e desvio padrão dos salários por
departamento.
"""

salario_por_dp = dados_new.groupBy('Área').agg(
    F.avg("Salário").alias('Média'),
    F.stddev("Salário").alias("Descio Padrão"),
    F.median("Salário").alias("Mediana"),
)

#salario_por_dp.show()

"""
5. Análise de Outliers: Identificar salários que estão fora do padrão (outliers) para cada
departamento.
"""

mean = dados_new.select(F.mean('Salário')).collect()[0][0]

desviopadrao = dados_new.select(F.stddev('Salário')).collect()[0][0]

nova_tabela = dados_new.withColumn('z-code', F.round((F.col('Salário') -  mean) / desviopadrao))

outliers = nova_tabela.filter(F.abs(F.col('z-code')) >= 3)

#outliers.show()

"""
6. Correlação Idade-Salário: Analisar a correlação entre idade e salário dos funcionários.

"""

correlation = dados_new.stat.corr('Idade', 'Salário')

# print(f'Correlação entre Idade e Salário: {correlation}')


"""
7. Tempo de Casa: Calcular o tempo de contratação dos funcionários e categorizá-los em grupos
(e.g., 1-3 anos, 4-6 anos, etc.).
"""

def tempo_de_casa(valor):
    ano = datetime.now().year
    try:
        data = datetime.strptime(valor, '%d/%m/%Y')
        return int(ano) - int(data.year)
    except ValueError as e:
        print(f"Erro ao converter a data: {e}")
        return None



inserir_informacao = F.udf(tempo_de_casa, IntegerType())

nova_tabela = dados_new.withColumn('Tempo de casa', inserir_informacao(F.col('Data de Contratação')))

def categorizar_em_grupo(numero):
    if numero is None:
        return 'nenhuma informação'
    elif numero < 4:
        return '1-3 anos'
    elif 3 < numero < 7:
        return '4-6 anos'
    else:
        return 'acima de 6 anos'

inserir_categoria = F.udf(categorizar_em_grupo, StringType())

nova_tabela = nova_tabela.withColumn('Catrgorizar Tempo De Casa', inserir_categoria(F.col('Tempo de casa')))

#nova_tabela.show()

"""
8. Análise de Rotatividade: Identificar padrões entre os funcionários que estão ativos versus os que
não estão.
"""
nova_tabela_rotatividade = dados_new.groupBy(['Status de Emprego', 'Área']).agg(
    F.count('*').alias('funcionario')
)

#nova_tabela_rotatividade.show()

"""
9. Análise de Desempenho por Data de Contratação: Verificar se existe uma correlação entre o ano
de contratação e o nível de salário.
"""

def ano(valor):
    try:
        data = datetime.strptime(valor, '%d/%m/%Y')
        return int(data.year)
    except ValueError as e:
        print(f"Erro ao converter a data: {e}")
        return None
    

inserir_ano_tabela = F.udf(ano, IntegerType())

tabela_ano_de_contratacao = dados_new.withColumn('Ano de contratação', inserir_ano_tabela(F.col('Data de Contratação')))

def nivel_salario(valor):
    if valor < 5000:
        return 'Abaixo de R$ 5.000,00'
    elif 5000 < valor > 6000:
        return 'Salário entre de R$ 5.000,00 e R$ 6.000,00'
    else:
        return 'Acima de R$ 6.000,00'
    
inserir_nivel_salario = F.udf(nivel_salario, StringType())

tabela_ano_de_contratacao = tabela_ano_de_contratacao.withColumn('Nível Salário', inserir_nivel_salario(F.col('Salário')))

tabela_ano_de_contratacao = tabela_ano_de_contratacao.groupBy(['Ano de contratação', 'Nível Salário']).agg(
    F.count('*').alias('Funcionario')
)

#tabela_ano_de_contratacao.show()

"""
10. Histograma de Salário: Criar um histograma de salários para visualizar a distribuição geral.
"""

salario = dados_new.select(F.col('Salário'))

salario = salario.withColumn('ID', F.monotonically_increasing_id())

pdf = salario.toPandas()

plt.figure(figsize=(10, 6))
plt.hist(pdf['Salário'], bins=10, edgecolor='black')
plt.title('Distribuição dos Salários')
plt.xlabel('Salário')
plt.ylabel('Número de Funcionários')
plt.grid(True)
#plt.show()

"""
11. Análise de Frequência: Quantificar a frequência dos nomes dos funcionários para identificar
nomes comuns.
"""

frequencia_nomes = dados_new.groupBy('Nome').agg(
    F.count('Nome').alias('Frequência')
)

#frequencia_nomes.show()

"""
12. Agrupamento de Departamentos: Analisar o impacto do departamento na variação salarial e na
distribuição de idade.
"""

agrupar_departamento = dados_new.groupBy(['Área']).agg(
    F.avg('Salário').alias('Media por Salário'),
    F.sum('Salário').alias('Total de salário por departamento'),
    F.avg('Idade').alias('Media por Idade'),
)

#agrupar_departamento.show()

"""
13. Normalização de Dados: Normalizar o salário e idade para comparações entre diferentes
departamentos.
"""

media_salario = dados_new.select(F.mean(F.col('Salário'))).first()[0]
desvio_padrao_salario = dados_new.select(F.stddev(F.col('Salário'))).first()[0]

media_idade = dados_new.select(F.mean(F.col('Idade'))).first()[0]
desvio_padrao_idade = dados_new.select(F.stddev(F.col('Idade'))).first()[0]

normalizando_dados = dados_new.withColumn('Salário_normalizado', ((F.col('Salário') - media_salario) / desvio_padrao_salario)).withColumn('Idade_normalizado', ((F.col('Idade') - media_idade) / desvio_padrao_idade))

#normalizando_dados.show()

"""
14. Proporção de Gêneros: Analisar a proporção de gêneros entre os funcionários, caso houvesse
uma coluna de gênero.
"""
# não tem genero
"""
15. Correção de Formato de Data: Uniformizar o formato das datas de contratação.
"""

data_padronizada = dados_new.orderBy(F.col('Nome').desc())

#data_padronizada.show()

"""
16. Impacto de Status no Salário: Comparar salários médios entre funcionários ativos e não ativos.
"""

comparar_salario = dados_new.groupBy('Status de Emprego').agg(
    F.avg('Salário').alias('Média')
)

#comparar_salario.show()

"""
17. Data de Contratação e Demografia: Relacionar a data de contratação com a idade dos
funcionários na época da contratação.
"""

tabela_ano_de_contratacao_nova = dados_new.withColumn('Ano de contratação', inserir_ano_tabela(F.col('Data de Contratação')))

tabela_ano_de_contratacao_nova = tabela_ano_de_contratacao_nova.withColumn('idade dos funcionários na época da contratação', (
   (F.col('Idade') - (int(datetime.now().year) - F.col('Ano de contratação')))
))

#tabela_ano_de_contratacao_nova.show()

"""
18. Distribuição de Status de Emprego: Analisar a distribuição do status de emprego (ativo vs. não
ativo).
"""

analisando_status = dados_new.groupBy('Status de Emprego').agg(
    F.count('*').alias('total de funcionarios')
)

#analisando_status.show()

"""
19. Criação de Coluna de Idade de Contratação: Criar uma coluna que calcule a idade do
funcionário na época da contratação e analisar os dados.
"""

# tabela_ano_de_contratacao_nova.show()

"""
20. Análise de Promoções: Analisar possíveis promoções dentro da empresa ao comparar datas de
contratação e aumentos salariais, se houvesse uma coluna histórica de salários.
"""

# sem historico de salario

"""
21. Análise de Desempenho Temporal: Verificar se o tempo de casa influencia o salário ou a
permanência no emprego.
"""

tabela_ano_de_contratacao_nova = dados_new.withColumn('Ano de contratação', inserir_ano_tabela(F.col('Data de Contratação')))

tabela_ano_de_contratacao_nova = tabela_ano_de_contratacao_nova.groupBy(['Ano de contratação', 'Salário', 'Status de Emprego']).agg(
    F.count('*')
)

# tabela_ano_de_contratacao_nova.show()

"""
22. Filtragem por Data de Contratação: Identificar funcionários contratados em períodos específicos
(e.g., antes de 2019, entre 2019-2020).
"""


tabela_ano_de_contratacao_3 = dados_new.withColumn('Ano de contratação', inserir_ano_tabela(F.col('Data de Contratação')))

filtragem_antes_de_2019 = tabela_ano_de_contratacao_3.filter(F.col('Ano de contratação') < 2019)

# filtragem_antes_de_2019.show()

filtragem_entre_2019_e_2020 = tabela_ano_de_contratacao_3.filter((F.col('Ano de contratação') >= 2019) & (F.col('Ano de contratação') <= 2020))

#filtragem_entre_2019_e_2020.show()
 
"""
23. Análise de Status de Emprego e Tempo de Casa: Verificar a relação entre tempo de casa e
status de emprego (ativo vs. não ativo).
"""

nova_tabela_2 = dados_new.withColumn('Tempo de casa', inserir_informacao(F.col('Data de Contratação')))

nova_tabela_2 = nova_tabela_2.groupBy(['Tempo de casa', 'Status de Emprego']).agg(
    F.count('*').alias('Total de funcionarios')
)

#nova_tabela_2.show()

"""
24. Identificação de Funcionários Veteranos: Encontrar os funcionários com maior tempo de casa e
analisar seu impacto na empresa.
"""

nova_tabela_3 = dados_new.withColumn('Tempo de casa', inserir_informacao(F.col('Data de Contratação')))

max_tempo_de_casa = nova_tabela_3.agg(F.max('Tempo de casa')).collect()[0][0]

tempo_de_casa = nova_tabela_3.filter((F.col('Tempo de casa')) == max_tempo_de_casa)

#tempo_de_casa.show()

"""
25. Análise de Tendências de Contratação: Identificar padrões de contratação ao longo do tempo,
como sazonalidade.
"""

def mes(valor):
    try:
        data = datetime.strptime(valor, '%d/%m/%Y')
        return int(data.month)
    except ValueError as e:
        print(f"Erro ao converter a data: {e}")
        return None
    

inserir_month_tabela = F.udf(mes, IntegerType())
    
contratacoes_por_mes = dados_new.withColumn('Ano', inserir_ano_tabela(F.col('Data de Contratação')))
contratacoes_por_mes = contratacoes_por_mes.withColumn('Mês', inserir_month_tabela(F.col('Data de Contratação')))

contratacoes_por_mes = contratacoes_por_mes.groupBy('Ano', 'Mês').count().orderBy('Ano', 'Mês')

df_pandas = contratacoes_por_mes.toPandas()

plt.figure(figsize=(12, 6))
plt.plot(df_pandas['Ano'].astype(str) + '-' + df_pandas['Mês'].astype(str), df_pandas['count'], marker='o')
plt.xticks(rotation=45)
plt.xlabel('Ano-Mês')
plt.ylabel('Número de Contratações')
plt.title('Tendência de Contratações ao Longo do Tempo')
plt.grid(True)
#plt.show()

"""
26. Salário Máximo e Mínimo por Departamento: Determinar os salários mais altos e mais baixos
dentro de cada departamento.
"""

salarios_max_altos_e_baixo = dados_new.groupBy('Área').agg(
    F.max('Salário').alias('Maior Salário'),
    F.min('Salário').alias('Menor Salário')
)

# salarios_max_altos_e_baixo.show()

"""
27. Classificação de Funcionários por Salário: Criar rankings de funcionários por salário dentro de
cada departamento.
"""

departamento_nome_salario = dados_new.groupBy(['Área', 'Nome', 'Salário']).agg(
    F.count('*')
).orderBy(['Área', 'Salário'])

#departamento_nome_salario.show()

"""
28. Projeção de Aposentadoria: Estimar o número de funcionários que podem se aposentar em
breve com base na idade.
"""

idade_minima_aposentadoria = 65

aposentadoria = dados_new.filter(F.col('Idade') >= idade_minima_aposentadoria)

#aposentadoria.show()

"""
29.Segmentação de Funcionários por Faixa Salarial: Agrupar funcionários em faixas salariais (e.g.,
2000-3000, 3001-4000) e analisar a distribuição.
"""

def faixa_salario(valor):
    if valor < 3001:
        return '0 - 3000'
    elif 3000 < valor < 4001:
        return '3001 - 4000'
    else:
        return 'maior 4000'
    
inserir_faixa_salarial = F.udf(faixa_salario, StringType())

nova_tabela_4 = dados_new.withColumn('Faixa_Salarial', inserir_faixa_salarial(F.col('Salário')))

nova_tabela_4 = nova_tabela_4.groupBy('Faixa_Salarial').agg(
    F.avg('Salário'),
    F.stddev('Salário'),
    F.max('Salário'),
    F.min('Salário'),
)

# nova_tabela_4.show()

"""
30. Análise de Equidade Salarial: Verificar se há desigualdade salarial dentro de departamentos
específicos.
"""

media_salarial_departamento = dados_new.groupBy('Área').agg(
    F.mean('Salário').alias('Média Salarial')
)

dados_com_media = dados_new.join(media_salarial_departamento, on='Área', how='inner')

media_salarial_analise = dados_com_media.withColumn('Diferença para Média', F.col('Salário') - F.col('Média Salarial'))

#media_salarial_analise.show()

"""
31. Comparação de Salários por Período de Contratação: Comparar os salários de funcionários
contratados em diferentes anos para identificar tendências de aumento salarial.
"""

nova_tabela_5 = dados_new.withColumn('Ano', inserir_ano_tabela(F.col('Data de Contratação')))

nova_tabela_5 = nova_tabela_5.groupBy('Ano').agg(
    F.avg('Salário'),
    F.mean('Salário'),
    F.stddev('Salário'),
    F.min('Salário'),
    F.max('Salário')
)

#nova_tabela_5.show()

"""
32. Criação de Coluna de Faixa Etária: Agrupar os funcionários em faixas etárias (e.g., 20-30 anos,
31-40 anos) e analisar diferenças entre elas.
"""

def faixa_etaria(valor):
    if 18 < valor < 21:
        return '18 - 20 anos'
    elif 20 < valor < 31:
        return '20 - 30 anos'
    elif 30 < valor < 41:
        return '30 - 40 anos'
    else: 
        return 'acima de 40 anos'

inserir_faixa_anos = F.udf(faixa_etaria, StringType())


nova_tabela_5 = dados_new.withColumn('Faixa Idade', inserir_faixa_anos(F.col('Idade')))

nova_tabela_5 = nova_tabela_5.groupBy('Faixa Idade').agg(
    F.avg('Salário'),
    F.mean('Salário'),
    F.stddev('Salário'),
    F.min('Salário'),
    F.max('Salário')
)

#nova_tabela_5.show()

"""
33. Relação Entre Área e Tempo de Contratação: Identificar se alguns departamentos tendem a
manter seus funcionários por mais tempo do que outros.
"""

ano = datetime.now().year


tabela_ano_tempo = dados_new.withColumn('Ano de contratação', inserir_ano_tabela(F.col('Data de Contratação')))

tabela_ano_tempo = tabela_ano_tempo.withColumn('Tempo de Contratação', ((ano) - (F.col('Ano de contratação'))))

tabela_ano_tempo = tabela_ano_tempo.groupBy(['Área','Tempo de Contratação']).agg(
    F.avg('Tempo de Contratação'),
    F.mean('Tempo de Contratação'),
    F.stddev('Tempo de Contratação'),
    F.min('Tempo de Contratação'),
    F.max('Tempo de Contratação')
)

#tabela_ano_tempo.show()

"""
34. Previsão de Turnover: Usar dados históricos para prever quais funcionários têm maior
probabilidade de deixar a empresa.
"""

db_dd = dados_new.withColumn("Status de Emprego", F.col("Status de Emprego").lower().alias("Status de Emprego"))
db_dd = dados_new.withColumn("Status de Emprego", F.lower(F.col("Status de Emprego")))

db_dd = db_dd.withColumn("Data de Contratação", F.col("Data de Contratação").cast("date"))
db_dd = db_dd.withColumn("Tempo de Serviço", F.datediff(F.current_date(), F.col("Data de Contratação")))

train_data, test_data = db_dd.randomSplit([0.8, 0.2], seed=42)

assembler = VectorAssembler(inputCols=["Idade", "Salário", "Tempo de Serviço"], outputCol="features")
train_data = assembler.transform(train_data)
test_data = assembler.transform(test_data)

lr = LogisticRegression(featuresCol="features", labelCol="Alvo")
lr_model = lr.fit(train_data)

predictions = lr_model.transform(test_data)

evaluator = BinaryClassificationEvaluator(labelCol="Alvo", metricName="areaUnderROC")
roc_auc = evaluator.evaluate(predictions)
print(f"Área sob a Curva ROC: {roc_auc}")

"""
35. Análise de Homogeneidade Salarial: Verificar a homogeneidade dos salários dentro de cada
departamento.
"""

tabela_de_homogenidade = dados_new.groupBy(['Área', 'Salário']).agg(
    F.count('*')
)

#tabela_de_homogenidade.show()

"""
36. Detecção de Funcionários Com Anomalias: Identificar funcionários com salários e idades que
destoam significativamente dos outros no mesmo departamento.
"""



"""
37. Comparação de Salários por Região: Se houvesse uma coluna de localização, comparar os
salários entre diferentes regiões.
"""

# Não tem localização

"""
38. Criação de Métricas Personalizadas: Desenvolver novas métricas como &quot;salário ajustado pela
idade&quot; ou &quot;tempo de casa ajustado pela idade&quot;.
"""

"""
39. Análise de Recrutamento Recente: Focar na análise dos funcionários contratados nos últimos
12 meses para ver tendências.
"""

ano_atual = datetime.now().year

tabela_ano_contratacao = dados_new.withColumn('Ano de contratação', inserir_ano_tabela(F.col('Data de Contratação')))

tabela_ano_contratacao = tabela_ano_contratacao.filter(F.col('Ano de contratação') == ano_atual)

#tabela_ano_contratacao.show()

"""
40. Distribuição de Funcionários por Departamento: Quantificar o número de funcionários por
departamento e comparar com a média salarial.
"""

distribuicao_de_funcionario_por_departamento = dados_new.groupBy(['Área']).agg(
    F.count('*').alias('número de funcionários por departamento'),
    F.avg('Salário').alias('média salarial')
)

#distribuicao_de_funcionario_por_departamento.show()

"""
41. Análise de Rotatividade por Departamento: Verificar se há departamentos com alta rotatividade
de funcionários.
"""

funcionario_com_rotatividade = dados_new.groupBy(['Status de Emprego', 'Área']).agg(
    F.count('*').alias('Número de funcionarios')
).orderBy('Área')

#funcionario_com_rotatividade.show()

"""
42. Comparação de Salários por Gênero: Se houvesse uma coluna de gênero, comparar os
salários médios entre homens e mulheres.
"""

"""
43. Correlação Entre Status de Emprego e Desempenho Salarial: Avaliar se há diferença
significativa de salários entre diferentes status de emprego.    
"""

estatisticas_salarial = dados_new.groupBy('Status de Emprego').agg(
    F.mean('Salário').alias('Média Salarial'),
    F.stddev('Salário').alias('Desvio Padrão'),
    F.count('Salário').alias('Número de Funcionários')
)

#estatisticas_salarial.show()

"""
44. Análise de Impacto de Promoções: Se houvesse dados de promoções, analisar o impacto das
promoções no salário ao longo do tempo.
"""

# Não tem historico de promoção

"""
45. Projeção de Custos Salariais: Calcular o custo projetado para a empresa em termos de salários
nos próximos anos.
"""

estatistica_salario = dados_new.groupBy('Status de Emprego').agg(
    F.sum('Salário')
)

#estatistica_salario.show()

"""
46. Análise de Desempenho por Escolaridade: Se houvesse uma coluna de escolaridade, analisar
o impacto da escolaridade no salário.
"""

# Se houvesse uma coluna de escolaridade (Não tem coluna)

"""
47. Comparação Entre Funcionários com Benefícios: Se houvesse dados de benefícios, comparar
o salário entre funcionários que recebem ou não benefícios.
"""

# Se houvesse dados de benefícios (Não tem Beneficio)

"""
48. Análise de Desempenho por Formação Acadêmica: Se houvesse uma coluna de formação,
analisar como diferentes formações afetam o salário e tempo de casa.
"""

# Não tem coluna

"""
49. Previsão de Salários Futuros: Usar regressão linear ou outros modelos para prever o
crescimento salarial futuro.
"""
data_atual = datetime.now()

db = dados_new.withColumn('Data de Contratação', F.to_date(F.col('Data de Contratação'), 'dd/MM/yyyy'))
db = db.withColumn('Ano de Contratação', F.year(F.col('Data de Contratação')))
db = db.withColumn('Ano Atual', 2024)
db = db.withColumn('Anos de Experiencia', (data_atual - F.col('Ano de Contratação')))

assembler = VectorAssembler(inputCols=['Anos de Experiência'], outputCol='features')
dados = assembler.transform(dados)

lr = LinearRegression(featuresCol='features', labelCol='Salário')
modelo = lr.fit(dados)

resumo = modelo.summary
"""
print(f'Coeficiente: {resumo.coefficients}')
print(f'Intercepto: {resumo.intercept}')
print(f'R²: {resumo.r2}')
"""


"""
50. Identificação de Padrões de Promoção Interna: Analisar os padrões de promoção dentro da
empresa ao longo dos anos.
"""




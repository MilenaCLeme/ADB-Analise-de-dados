from google.cloud import storage

client = storage.Client()

bucket_name = 'aula-soulcode-python-milena'
bucket = client.bucket(bucket_name)

destination_blob_path = 'dados_brutos/agentes-economicos-regulares.csv'

blob = bucket.blob(destination_blob_path)
blob.upload_from_filename('/content/agentes-economicos-regulares.csv')

from google.cloud import storage
import pandas as pd
import io
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from datetime import datetime
from pyspark.sql.types import IntegerType
from pyspark.sql.types import DoubleType
import numpy as np

client = storage.Client()

bucket_name = 'aula-soulcode-python-milena'
file_name = 'dados_brutos/agentes-economicos-regulares.csv'

bucket = client.bucket(bucket_name)
blob = bucket.blob(file_name)

data = blob.download_as_bytes()

spark = SparkSession.builder.appName('Atividade').getOrCreate()

df = pd.read_csv(io.BytesIO(data), on_bad_lines='skip')

destination_blob_path = 'dados_tratados/'


df['DATA_REGISTRO'] = pd.to_datetime(df['DATA_REGISTRO'], errors='coerce', format='%d/%m/%Y')
df['DATA_CONSTITUICAO'] = pd.to_datetime(df['DATA_CONSTITUICAO'], errors='coerce', format='%d/%m/%Y')

df_pyspark = spark.createDataFrame(df)
# Agrupamentos por UF (Unidade Federativa):

# 1 - Quantas empresas estão registradas em cada estado (UF)?

df_agrupamentos_uf = df.groupby('UF').agg(
    quantidade_por_regiao=('UF', 'size'),
).sort_values('UF')

df_agrupamentos_uf.to_csv('agrupamentoUF.cvs')

#print(df_agrupamentos_uf)

# Filtragem por DATA_REGISTRO:

# 2 . Quais empresas foram registradas após 2020?

df_filter_data_registro = df[df['DATA_REGISTRO'].dt.year > 2020]

df_filter_data_registro.to_csv('filtrar2020.cvs')


#print(df_filter_data_registro)


# 3. Quais são os setores econômicos mais comuns (CLASSIFICACAO_AGENTE_ECONOMICO) em cada estado?

df_classificao_agrupamento = df.groupby(['CLASSIFICACAO_AGENTE_ECONOMICO', 'UF']).agg(
    quantidade_de_agentes=('CLASSIFICACAO_AGENTE_ECONOMICO', 'size')
)

df_classificao_agrupamento.to_csv('classificaoagrupamento.cvs')


#print(df_classificao_agrupamento)

#4 . pegar o agrupamento e fazer mais um somando e tirando a media

df_agrupamento_media_mediana = df_classificao_agrupamento.groupby(['CLASSIFICACAO_AGENTE_ECONOMICO']).agg(
    Soma_por_quantidade=('quantidade_de_agentes', 'sum'),
    media_por_quantidade=('quantidade_de_agentes', 'mean'),
    mediana_por_quantidade=('quantidade_de_agentes', 'median')
).reset_index()

#print(df_agrupamento_media_mediana)

df_agrupamento_media_mediana.to_csv('dfagrupamento.cvs')


# 5. Como o número de empresas classificadas como "Brasileiro independente" QUNATOS ANOS DE FUNCIONAMENTO?


df_limit1 = df_pyspark.select('CLASSIFICACAO_AGENTE_ECONOMICO').limit(1)

resultado = df_limit1.collect()

valor = resultado[0]['CLASSIFICACAO_AGENTE_ECONOMICO']

df_classificao_classificacao = df_pyspark.filter(F.col('CLASSIFICACAO_AGENTE_ECONOMICO') == valor)

df_classificao_classificacao = df_classificao_classificacao.withColumn('ANO_CONSTITUICAO', F.year(F.col('DATA_CONSTITUICAO')))

converter_pandas1 = df_classificao_classificacao.toPandas()

converter_pandas1.to_csv('dfclassificacao.cvs')

blob1 = bucket.blob(f"{destination_blob_path}agrupamentoUF.cvs")
blob1.upload_from_filename('/content/agrupamentoUF.cvs')

blob2 = bucket.blob(f"{destination_blob_path}filtrar2020.cvs")
blob2.upload_from_filename('/content/filtrar2020.cvs')

blob3 = bucket.blob(f"{destination_blob_path}classificaoagrupamento.cvs")
blob3.upload_from_filename('/content/classificaoagrupamento.cvs')

blob4 = bucket.blob(f"{destination_blob_path}dfagrupamento.cvs")
blob4.upload_from_filename('/content/dfagrupamento.cvs')

blob5 = bucket.blob(f"{destination_blob_path}dfclassificacao.cvs")
blob5.upload_from_filename('/content/dfclassificacao.cvs')
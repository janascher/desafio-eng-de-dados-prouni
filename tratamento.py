import pandas as pd 
from unidecode import unidecode

df = pd.read_csv("ProuniRelatorioDadosAbertos2020.csv", encoding="UTF-8", sep=";")

#Informções dos dados cru:
print(df.info())

print(df.shape)

print(df.nunique())

print(df.isnull().sum())

#Limpando dados:

colunas_para_apagar = ["CPF_BENEFICIARIO", "BENEFICIARIO_DEFICIENTE_FISICO", "NOME_TURNO_CURSO_BOLSA", "CODIGO_EMEC_IES_BOLSA"]
df = df.drop(colunas_para_apagar, axis=1)

df["MUNICIPIOS"] = df["MUNICIPIO"] + df["MUNICIPIO_BENEFICIARIO"]
df["MUNICIPIOS"] = df['MUNICIPIOS'].drop_duplicates()
df = df.dropna(subset=['NOME_CURSO_BOLSA', 'MUNICIPIOS'])
df.drop(['MUNICIPIO', 'MUNICIPIO_BENEFICIARIO'], axis=1, inplace=True)

print(df.isnull().sum())

df.to_csv('dados_prouni2020_tratados.csv', index=False,)

colunas_para_remover_acentos =  ['ANO_CONCESSAO_BOLSA','NOME_IES_BOLSA','CAMPUS','TIPO_BOLSA','MODALIDADE_ENSINO_BOLSA','NOME_CURSO_BOLSA','SEXO_BENEFICIARIO','RACA_BENEFICIARIO','DATA_NASCIMENTO','REGIAO_BENEFICIARIO','UF_BENEFICIARIO','MUNICIPIOS']
for coluna in colunas_para_remover_acentos:
    df[coluna] = df[coluna].apply(lambda x: unidecode(str(x)))
print(df)
df.dropna(inplace=True)
df.to_csv('dados_prouni2020_tratados.csv', index=False)


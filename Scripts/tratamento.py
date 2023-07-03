import pandas as pd

df = pd.read_csv("./Data/raw/ProuniRelatorioDadosAbertos2020.csv", encoding="UTF_8", sep=";")

#Informções dos dados cru:
# print(df.info())

# print(df.shape)

# print(df.nunique())

# print(df.isnull().sum())

#Limpando dados:
df = df.dropna(subset=['NOME_CURSO_BOLSA'])

colunas_para_apagar = ["CPF_BENEFICIARIO", "BENEFICIARIO_DEFICIENTE_FISICO", "NOME_TURNO_CURSO_BOLSA", "CODIGO_EMEC_IES_BOLSA"]
df = df.drop(colunas_para_apagar, axis=1)

df["MUNICIPIOS"] = df["MUNICIPIO"] + df["MUNICIPIO_BENEFICIARIO"]
df['MUNICIPIOS'] = df['MUNICIPIOS'].drop_duplicates()
df.drop(['MUNICIPIO', 'MUNICIPIO_BENEFICIARIO'], axis=1, inplace=True)
print(df.isnull().sum())

# df.to_csv('dados_prouni2020_tratados.csv', index=False)
df.to_csv('./Data/curated/dados_prouni2020_tratados.csv', index=False)


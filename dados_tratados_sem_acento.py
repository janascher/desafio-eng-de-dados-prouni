import pandas as pd
from unidecode import unidecode

df = pd.read_csv("dados_prouni2020_tratados.csv", sep=',', encoding="utf-8")

colunas_para_remover_acentos =  ['ANO_CONCESSAO_BOLSA','NOME_IES_BOLSA','CAMPUS','TIPO_BOLSA','MODALIDADE_ENSINO_BOLSA','NOME_CURSO_BOLSA','SEXO_BENEFICIARIO','RACA_BENEFICIARIO','DATA_NASCIMENTO','REGIAO_BENEFICIARIO','UF_BENEFICIARIO','MUNICIPIOS']
for coluna in colunas_para_remover_acentos:
    df[coluna] = df[coluna].apply(lambda x: unidecode(str(x)))
print(df)
df.to_csv('arquivo_tratado_sem_acentos.csv', index=False)


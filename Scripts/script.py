import psycopg2

# USE AS CONFIGURAÇÕSE A BAIXO PARA SE CONECTAR COM SERVIDOR ELEPHANTSQL 
# O ELEPHANTSQL SUPORTA APENAS 20MB DE DADOS GRATUITOS
# PARA USAR MAIS DE 20MB MUDE AS CONFIGURAÇOES ABAIXO PASSANDO OS DADOS DO SERVIDOR LOCAL INSTALADO NA SUA MAQUINA
# PARA GERAR AS TABELAS LOCALMENTE BASTA EXECUTAR O SCRIPT ABAIXO

# Configurações do banco de dados
db_host = 'stampy.db.elephantsql.com'
db_name = 'xzzjkleg'
db_user = 'xzzjkleg'
db_password = 'O1Nk6zWqMGePPghjALegO3Q-FBCvqx2V'

# Conexão com o banco de dados
conn = psycopg2.connect(host=db_host, database=db_name, user=db_user, password=db_password)
cursor = conn.cursor()

# Criação da tabela Regiões
cursor.execute('''
    CREATE TABLE Regioes (
        id SERIAL PRIMARY KEY,
        nome_regiao VARCHAR(255) NOT NULL
    )
''')

# Criação da tabela UF
cursor.execute('''
    CREATE TABLE UF (
        id SERIAL PRIMARY KEY,
        uf CHAR(2) NOT NULL
    )
''')

# Criação da tabela Municípios
cursor.execute('''
    CREATE TABLE Municipios (
        id SERIAL PRIMARY KEY,
        nome_municipio VARCHAR(255) NOT NULL,
        uf_id INTEGER REFERENCES UF(id)
    )
''')

# Criação da tabela Beneficiários
cursor.execute('''
    CREATE TABLE Beneficiarios (
        id SERIAL PRIMARY KEY,
        cpf VARCHAR(11) NOT NULL,
        sexo VARCHAR(10) NOT NULL,
        raca VARCHAR(50) NOT NULL,
        data_nascimento DATE NOT NULL,
        deficiente_fisico BOOLEAN NOT NULL,
        municipio_id INTEGER REFERENCES Municipios(id)
    )
''')

# Criação da tabela IES (Instituições de Ensino Superior)
cursor.execute('''
    CREATE TABLE IES (
        id SERIAL PRIMARY KEY,
        codigo_emec INTEGER NOT NULL,
        nome VARCHAR(255) NOT NULL,
        municipio_id INTEGER REFERENCES Municipios(id),
        regiao_id INTEGER REFERENCES Regioes(id)
    )
''')

# Criação da tabela Cursos
cursor.execute('''
    CREATE TABLE Cursos (
        id SERIAL PRIMARY KEY,
        nome_curso VARCHAR(255) NOT NULL,
        turno VARCHAR(255) NOT NULL
    )
''')

# Criação da tabela Bolsas
cursor.execute('''
    CREATE TABLE Bolsas (
        id SERIAL PRIMARY KEY,
        ano_concessao INTEGER NOT NULL,
        tipo_bolsa VARCHAR(255) NOT NULL,
        modalidade_ensino VARCHAR(255) NOT NULL,
        ies_id INTEGER REFERENCES IES(id),
        curso_id INTEGER REFERENCES Cursos(id),
        beneficiario_id INTEGER REFERENCES Beneficiarios(id)
    )
''')

# Criação de índices para melhorar o desempenho de consultas
cursor.execute('CREATE INDEX idx_beneficiarios_municipio ON Beneficiarios(municipio_id)')
cursor.execute('CREATE INDEX idx_ies_municipio ON IES(municipio_id)')
cursor.execute('CREATE INDEX idx_ies_regiao ON IES(regiao_id)')

# Commit e fechamento da conexão
conn.commit()
conn.close()

print("Banco de dados criado com sucesso.")

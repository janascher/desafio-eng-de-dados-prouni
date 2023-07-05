import psycopg2

# Configurações do banco de dados
db_host = 'postgres-db.csteolceunx7.us-east-1.rds.amazonaws.com'
db_name = 'postgres'
db_user = 'postgres'
db_password = 'ErJMgFrLGjnpBe9Xg6Bv'

# Conexão com o banco de dados
conn = psycopg2.connect(host=db_host, database=db_name, user=db_user, password=db_password)
cursor = conn.cursor()

# 2 - Quantidade de Beneficiários por Raça/Cor:
query = '''
    SELECT sexo, COUNT(*) AS quantidade
    FROM Beneficiarios
    GROUP BY sexo;
'''

cursor.execute(query)
sexo = cursor.fetchall()

# 3 - Quantidade de Beneficiários por Raça/Cor:
query = '''
    SELECT raca, COUNT(*) AS quantidade
    FROM Beneficiarios
    GROUP BY raca;
'''

cursor.execute(query)
raca = cursor.fetchall()

# 4 - Distribuição Percentual de Beneficiários por Raça/Cor:
query = '''
    SELECT raca, (COUNT(*) * 100.0 / (SELECT COUNT(*) FROM Beneficiarios)) AS percentual
    FROM Beneficiarios
    GROUP BY raca;
'''

cursor.execute(query)
dist = cursor.fetchall()

# 5 - Média de Idade dos Beneficiários por Sexo e Raça/Cor:
query = '''
    SELECT sexo, raca, AVG(EXTRACT(YEAR FROM AGE(NOW(), data_nascimento))) AS media_idade
    FROM Beneficiarios
    GROUP BY sexo, raca;
'''

cursor.execute(query)
raca_porcent = cursor.fetchall()

# 6 - Distribuição de Beneficiários por Tipo de Bolsa de Estudos, Sexo e Raça/Cor:
query = '''
    SELECT b.tipo_bolsa, b.sexo, b.raca, COUNT(*) AS quantidade
    FROM Beneficiarios AS b
    JOIN Bolsas AS bo ON b.id = bo.beneficiario_id
    GROUP BY b.tipo_bolsa, b.sexo, b.raca;
'''

cursor.execute(query)
media = cursor.fetchall()

# 7 - Distribuição de Beneficiários por Sexo e Raça/Cor - {institution}:
query = '''
    SELECT b.sexo, b.raca, COUNT(*) AS quantidade
    FROM Beneficiarios AS b
    JOIN Bolsas AS bo ON b.id = bo.beneficiario_id
    JOIN IES AS i ON bo.ies_id = i.id
    WHERE i.nome = '{institution}'
    GROUP BY b.sexo, b.raca;
'''

cursor.execute(query)
dist_ies = cursor.fetchall()

# 8 - Distribuição de Beneficiários por Região e UF (Sexo: {sexo}):
query = '''
    SELECT r.nome_regiao, u.uf, COUNT(*) AS quantidade
    FROM Beneficiarios AS b
    JOIN Municipios AS m ON b.municipio_id = m.id
    JOIN UF AS u ON m.uf_id = u.id
    JOIN Regioes AS r ON u.regiao_id = r.id
    WHERE b.sexo = '{sexo}'
    GROUP BY r.nome_regiao, u.uf;
'''

cursor.execute(query)
dist_uf = cursor.fetchall()

# 9 - Distribuição de Beneficiários por Região e UF (Raça/Cor: {raca}):
query = '''
    SELECT r.nome_regiao, u.uf, COUNT(*) AS quantidade
    FROM Beneficiarios AS b
    JOIN Municipios AS m ON b.municipio_id = m.id
    JOIN UF AS u ON m.uf_id = u.id
    JOIN Regioes AS r ON u.regiao_id = r.id
    WHERE b.raca = '{raca}'
    GROUP BY r.nome_regiao, u.uf;
'''

cursor.execute(query)
dist_regiao = cursor.fetchall()
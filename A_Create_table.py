import mysql.connector

# Conectar ao banco de dados

Usuario = 'root' #Padrão
senha = '' #Senha do Mysql << PREENCHER
servidor =  'localhost' # Padrão
base_de_dados = 'base1' #Nome do Schema criado

cnx = mysql.connector.connect(user=Usuario, password=senha, host=servidor, database=base_de_dados)
cursor = cnx.cursor()

# Criar tabela >>ACOES<< com os sequintes campos, id (Com incremento automatico por iniclusão), Stock, Data, Open, Close.
table = '''
CREATE TABLE IF NOT EXISTS acoes ( 
    id INT AUTO_INCREMENT PRIMARY KEY,
    Stock VARCHAR2(255),
    Data DATE NOT NULL,
    Open FLOAT,
    Close FLOAT
);
'''
cursor.execute(table)

# Incluir dados em branco para teste

query = "INSERT INTO acoes (Stock, Data, Open, Close) VALUES (%s, %s, %s, %s)"
values = []

for val in values:
    cursor.execute(query, val)

cnx.commit()

# Fechar conexão
cursor.close()
cnx.close()

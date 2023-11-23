import mysql.connector

# Conectar ao banco de dados

Usuario = 'root' #Padrão
senha = '' #Senha do Mysql << PREENCHER
servidor =  'localhost' # Padrão
base_de_dados = 'base1' #Nome do Schema criado

cnx = mysql.connector.connect(user=Usuario, password=senha, host=servidor, database=base_de_dados)
cursor = cnx.cursor()

# Incluir dados, Stock = VARCHAR2, Data = Data, Open = FLOAT e Close = FLOAT

#Atualizar dados na tabela
stock = 'ITSA4.SA'
data = '2023-08-01'
new_open = 999.5
new_close = 14.57

query = "INSERT INTO acoes (Open = %s, Close = %s WHERE Stock = %s AND Data = %s)"
values = (new_open, new_close, stock, data)
cursor.execute(query, values)

cnx.commit()
for val in values:
    cursor.execute(query, val)

cnx.commit()

# Fechar conexão
cursor.close()
cnx.close()

import mysql.connector

# Conectar ao banco de dados

Usuario = 'root' #Padrão
senha = '' #Senha do Mysql << PREENCHER
servidor =  'localhost' # Padrão
base_de_dados = 'base1' #Nome do Schema criado

cnx = mysql.connector.connect(user=Usuario, password=senha, host=servidor, database=base_de_dados)
cursor = cnx.cursor()

# Definição de variáveis
stock = "BBDC3.SA"
data = "2023-11-20"

# Consulta
query = "SELECT * FROM acoes WHERE Stock = %s AND Data = %s"
cursor.execute(query, (stock, data))
resultados = cursor.fetchall()
for resultado in resultados:
    print(resultado)

# Fechar conexão
cursor.close()
cnx.close()

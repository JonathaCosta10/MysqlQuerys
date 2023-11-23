import mysql.connector

# Conectar ao banco de dados

Usuario = 'root' #Padrão
senha = '' #Senha do Mysql << PREENCHER
servidor =  'localhost' # Padrão
base_de_dados = 'base1' #Nome do Schema criado

cnx = mysql.connector.connect(user=Usuario, password=senha, host=servidor, database=base_de_dados)
cursor = cnx.cursor()

id_to_delete = 2

#Excluir registro com o id = 2 
query = "DELETE FROM acoes WHERE id = %s"
cursor.execute(query, (id_to_delete,))

cnx.commit()

#Fechar conexão
cursor.close()
cnx.close()
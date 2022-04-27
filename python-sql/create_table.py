import mysql.connector

try:
    connection = mysql.connector.connect(host='localhost',database='yamadori',user='root',password='CUZINd3P4RD4L(@)')

    criar_tabela_SQL = """CREATE TABLE `tbl_teste` (
                            IdTeste int(11) NOT NULL,
                            Nome VARCHAR(70) NOT NULL,
                            Preco FLOAT NOT NULL,
                            Quantidade TINYINT NOT NULL,
                            PRIMARY KEY (IdTeste)) """
    
    cursor = connection.cursor()
    cursor.execute(criar_tabela_SQL)
    print('Tabela criada com sucesso!')
except mysql.connection.Error as erro:
    print('Falha ao criar tabela no MySQL: ()'.format(erro))
finally:
    if(connection.is_connected()):
        cursor.close()
        connection.close()
        print('Conexão ao MySQL finalizada.')

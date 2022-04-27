import mysql.connector

connection = mysql.connector.connect(host='localhost',database='yamadori',user='root',password='CUZINd3P4RD4L(@)')

if connection.is_connected():
    info = connection.get_server_info()
    print('conectado ao seerver MySQL versão',info)
    cursor = connection.cursor()
    cursor.execute('select database();')
    schema = cursor.fetchone()
    print('conectado ao schema: ',schema)

if connection.is_connected():
    cursor.close()
    connection.close()
    print('conexão ao server MySQL encerrada')
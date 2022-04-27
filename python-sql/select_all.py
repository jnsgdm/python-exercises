import mysql.connector 
from mysql.connector import Error

try: 
    connection = mysql.connector.connect(host='localhost',database='yamadori',user='root',password='CUZINd3P4RD4L(@)')

    select_all = "select * from tbl_teste"
    cursor = connection.cursor()
    cursor.execute(select_all)
    rows = cursor.fetchall() #retorna uma lista de tuplas com os dados 
    print('Total de registros: ',cursor.rowcount,'\n')
    print('=-'*10)

    for row in rows:
        print('ID: ', row[0])
        print('Nome: ', row[1])
        print('Preço: ', row[2])
        print('Estoque: ', row[3],'\n')
except Error as erro:
    print('Algo deu errado: ', erro)
finally:
    if(connection.is_connected()):
        cursor.close()
        connection.close()
        print('Conexão finalizada!')



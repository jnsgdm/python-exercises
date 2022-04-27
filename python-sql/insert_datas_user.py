import mysql.connector
from mysql.connector import Error

print('Informe os dados solicitados')
print('-='*10)

IdTeste = input('ID: ')
Nome = input('Nome: ')
Preco = input('Preço: ')
Quantidade = input('Quantidade em estoque: ')

datas = '('+IdTeste + ',\'' +Nome + '\',' + Preco + ',' + Quantidade+')'#marcador de escape, pois o nome deve estar entre ''

sql_comand = """INSERT INTO tbl_teste
                       (IdTeste,Nome,Preco,Quantidade)    
                      VALUES""" + datas

try: 
    connection = mysql.connector.connect(host='localhost',database='yamadori',user='root',password='CUZINd3P4RD4L(@)')

    insert_datas = sql_comand

    cursor = connection.cursor()
    cursor.execute(insert_datas) 
    connection.commit() #tornar a ação permanente
    print("registro inserido!")
except Error as erro:
    print('Algo deu errado: ',erro)
finally:
    if(connection.is_connected()):
        cursor.close()
        connection.close()
        print('Conexão ao DB finalizada!')
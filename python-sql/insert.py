import mysql.connector
from mysql.connector import Error

try: 
    connection = mysql.connector.connect(host='localhost',database='yamadori',user='root',password='CUZINd3P4RD4L(@)')

    insert_datas = """INSERT INTO tbl_teste
                       (IdTeste,Nome,Preco,Quantidade)    
                      VALUES 
                       (1,'smart watch',450.00,3),
                       (2,'monitor 240hz',2000.00,5)  
                    """

    cursor = connection.cursor()
    cursor.execute(insert_datas) 
    connection.commit() #tornar a ação permanente
    print(cursor.rowcount,"registros inseridos!")
except Error as erro:
    print('Algo deu errado: ',erro)
finally:
    if(connection.is_connected()):
        cursor.close()
        connection.close()
        print('Conexão ao DB finalizada!')
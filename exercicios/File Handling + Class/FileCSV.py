import csv

with open('teste1.csv',encoding='utf-8') as file:

    table = csv.reader(file,delimiter=',') #ler o file e delimitador

    for i in table:
        id_ = i[0]
        nome = i[1]
        msg = i[2]

        print(id_,nome,msg)

op = open('teste2.csv','w',newline='',encoding='utf=8')

w = csv.writer(op)

for i in range(10):
    w.writerow([i,i*2,i*3])


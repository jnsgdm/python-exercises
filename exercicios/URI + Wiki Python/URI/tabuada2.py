A = int(input())
B = int(input())

if A > B:
    print('Nenhuma tabuada no intervalo!')
else:
    x = range(A,B+1)
    for i in x:
        count = 1 
        while count <= 10:
            mult = i*count
            print(f'{i} x {count} = {mult}')
            count+=1
        print('----------')
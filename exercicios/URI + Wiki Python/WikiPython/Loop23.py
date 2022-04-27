#todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário.
#O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos.
n = int(input())
x = range(1,n+1)
ar = []

for i in x:
    divis = 0
    count = 1
    while count <= i:
        if i%count==0:
            divis+=1
        count+=1
        
    if divis==2:
        ar.append(i)

print(f'Números primos são: {ar}')
print(f'Total de divisões: {divis}')

#output
#10
#Números primos são: [2, 3, 5, 7]
#Total de divisões: 4
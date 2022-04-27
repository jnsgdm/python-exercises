# Iterando dentro de uma tupla
x = (1,2,3,5,8,13,21)

it = iter(x)
try:
    while True:
        i = next(it)
        print(i)

except StopIteration:
    print("final 1")
    pass

for i in x:
    print(i)
else:
    print("final 2")

x = (1,2,3,4)
interacao = iter(x) #percorre uma coleção de elementos em objeto,listas,conjunto,tuplass e dicionairios, porém de forma genérica 
next(interacao) #move-se para o próximo item da coleção de elementos
#SIM, o except foi executado

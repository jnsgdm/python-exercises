# Crie um função que receba como parâmetro uma matriz tridimensional de inteiros 
# e um número N e retorne a soma de todos os valores pares que estão na matriz e que são 
# maiores que N
# Crie também um programa que preencha a matriz com números aleatórios e chame a função criada

def rotornaSomaPares(matriz,N):
    countLines = len(matriz)
    countColumns = len(matriz[0])
    newAr = []

    for line in range(countLines): 
        for column in range(countColumns):
            if matriz[line][column] > N:
                if matriz[line][column] % 2 == 0:
                    newAr.append(matriz[line][column])    
    return sum(newAr)

matriz = []
x = list(range(3))
y = list(range(3,6))
z = list(range(6,9))
matriz.append(x)
matriz.append(y)
matriz.append(z)

print(rotornaSomaPares(matriz,4))
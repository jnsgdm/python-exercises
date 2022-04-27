#Crie um função que receba como parâmetro uma matriz de inteiros e um número N 
#e retorne uma lista com todos os valores da matriz e que são maiores que N


def retornaMaiores(matriz,N):
    countLines = len(matriz)
    countColumns = len(matriz[0])
    newAr = []

    for line in range(countLines): 
        for column in range(countColumns):
            if matriz[line][column] > N:
                newAr.append(matriz[line][column])    
    return newAr

notas = [[10,9,10],[8,9,10],[8,7,9]]

print(retornaMaiores(notas,8))
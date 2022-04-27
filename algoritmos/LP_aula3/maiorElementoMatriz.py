def retornaMaior(matriz):
    countLines = len(matriz)
    countColumns = len(matriz[0])
    firstElement = matriz[0][0]

    for line in range(countLines): 
        for column in range(countColumns):
            if matriz[line][column] > firstElement:
                firstElement = matriz[line][column] 
    return firstElement

notas = [[1,2,23],[4,82,6],[7,8,9]]

print(retornaMaior(notas))
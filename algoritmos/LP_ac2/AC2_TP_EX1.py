def indexMatriz(matriz,n):
    countLines = len(matriz)
    countColumns = len(matriz[0])
    ar = []

    for line in range(countLines): 
        for column in range(countColumns):
            if matriz[line][column] == n:
                indexMatriz = (line,column)
                ar.append(indexMatriz)
    return ar

n = int(input('n='))
print("Matriz")
myRA = [(2,1,0),(1,8,5),(2,2,1)]
print(myRA)
print("Lista retornanda")
print(indexMatriz(myRA,n))
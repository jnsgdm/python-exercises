#Crie um função que receba como parâmetro uma matriz de inteiros e um número N e 
#retorne a soma de todos os valores que estão na matriz e que são maiores que N

def somaMaiores(matriz,N):
    countLines = len(matriz)
    countColumns = len(matriz[0])
    newAr = []

    for line in range(countLines): 
        for column in range(countColumns):
            if matriz[line][column] > N:
                newAr.append(matriz[line][column])    
    return sum(newAr)

notas = [[10,9,10],[8,9,10],[8,7,9]]

print(somaMaiores(notas,8))
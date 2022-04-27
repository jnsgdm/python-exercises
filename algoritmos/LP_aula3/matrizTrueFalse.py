#Crie um função que receba como parâmetro uma matriz de inteiros e um número N e
#retorne a True se N existir na matriz e False se não existir

def somaDiagonal(matriz,N):
    countLines = len(matriz)
    countColumns = len(matriz[0])
    soma = 0

    for line in range(countLines): 
        for column in range(countColumns):
            if matriz[line][column] == N: #verifica em todoas as linhas e tds as colunas se existem o numero N passado
                return True     
    return False

notas = [[10,9,10],[8,9,10],[8,7,9]]

print(somaDiagonal(notas,9))
print(somaDiagonal(notas,3))
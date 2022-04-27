def somaDiagonal(matriz):
    countLines = len(matriz)
    countColumns = len(matriz[0])
    soma = 0

    for line in range(countLines): 
        for column in range(countColumns):
            if line+column==3:
                soma=soma+matriz[line][column]
    print(soma)

notas = [[10,9,10],[8,9,10],[8,7,9]]

somaDiagonal(notas)
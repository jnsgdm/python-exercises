#criando matriz
# ar = [[6,2,4],[7,-3,-1],[-1,5,2]]
# for linha in range(3):
#     for coluna in range(3):
#         print(f'[{ar[linha][coluna]}]',end='')
#     print()

def sumElements(matriz):
    countLines = len(matriz)
    countColumns = len(matriz[0])
    soma = 0

    for line in range(countLines): 
        for column in range(countColumns):
            soma=soma+matriz[line][column]
    print(soma)

notas = [[10,9,10],[8,9,10],[8,7,9]]

sumElements(notas)
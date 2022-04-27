
def procurar():
    vetor = [1,2,3,4,5]
    numero = int(input('Qual número deseja?'))
    vdd = False

    for i in range(4):
        if (vetor[i] == numero):
            print('Encontrado na posição: ', i)
            vdd = True 

    if (vdd!=True):
        print('Numero nao encontrado.')

#procurar()

def matriz():
    #ar = [[1,2,-4],
    #      [2,0,-1],
    #      [0,-3,4]]

    #deixar a matriz vazia com zero 
    ar = [[0,0,0],[0,0,0],[0,0,0]]

    #for 1 para alimentação de valores da matriz
    for linha in range(3): #linha == 3
        for coluna in range(3): #linha ==3
            ar[linha][coluna] = input('Digite um numero esolhido: ') #ar[x][y] = x * y 
            #isso calcula a dimensão de 2x2 que é como uma matriz funciona (linha x Scoluna)
            #nesse caso vai se repetir 9 vezes 

    #mostrando uma matriz da forma adequada
    print('~='*20)
    for linha in range(3):
        for coluna in range(3):
            print(f'[{ar[linha][coluna]}]',end='') #criando as colunas 
        print()#print vazio para quebrar a linha toda vez que uma coluna for formada 

matriz()

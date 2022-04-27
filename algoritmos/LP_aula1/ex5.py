def posicao(array,num):
    if num in array:
        print(array.index(num))
    else:
        print(-1)
        

ar = [0,87,7,10,2]

posicao(ar,7)

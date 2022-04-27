#Seu objetivo é criar um programa que receba como entrada dois números naturais, INÍCIO e FIM,
#  e exibe os números primos que existem no intervalo fechado [ INÍCIO..FIM ].
#  Ao final, o programa também deve exibir a quantidade de primos encontrados no intervalo.
start = int(input())
final = int(input())

if start <= final <= 5000:  
    ar = []
    for i in range(start,final+1):  
        count_div = 0 
        n = 1 
        while n <= i:
            if i%n==0:
                count_div+=1
            n+=1
        if count_div == 2:
            ar.append(i)
            print(i)

    count = len(ar)
    print(f'primos: {count}')
#Calcula o ano bissextos entre os anos
inicio = int(input())
fim = int(input())
i = 0
if 0 <= inicio <= fim <= 9999:
    x = range(inicio,fim+1)
    for ano in x:
        if ano%4==0 and ano%100!=0 or ano %4 ==0 and ano%400==0:
            print(ano)
            i+=1
    print(f'bissextos: {i}')

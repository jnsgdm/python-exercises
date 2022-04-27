n_work = float(input())
n_teste = float(input())
sub = 10
media = (n_work+n_teste)/2

if media >= 6:
    print('aprovado')
elif (n_work+sub)/2 >=6: #na sub pode tentar tirar 10 de novo 
    print('talvez com a sub')
elif media < 6:
    print('reprovado')

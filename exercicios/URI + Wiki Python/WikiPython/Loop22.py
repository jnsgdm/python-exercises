#cálculo dos números primos, caso o número não seja primo, por quais número ele é divisível.
n = int(input())
i = 1
divis = 0
ar = []
while i <= n:
    if n%i==0:
        divis+=1
        ar.append(i)
    i+=1
if divis==2:
    print(f'{n} é primo')
else:
    print(f'{n} n é primo')
    print(f'seus divisores são: {ar}')
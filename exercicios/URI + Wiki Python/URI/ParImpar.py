num = int(input())

if num >= 2:
    if num%2==0:
        before_par = num - 1 #proximo impar 
        after_par = num + 2 #proximo par 
        print(f'{before_par} {after_par}')
    else: 
        before_impar = num - 2
        after_impar = num + 1
        print(f'{before_impar} {after_impar}')
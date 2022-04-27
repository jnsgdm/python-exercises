#fatorial de um número 
n = int(input())
fat = 1
i = 0
print(f'!{n} = ',end='')#end para parar o print com um espaço na mesma linha 
while i < n:
    print(f'{n}',end='*')
    fat=n*fat 
    n = n-1  
print(f' = {fat}')

#output
#5
#!5 = 5*4*3*2*1* = 120
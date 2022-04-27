#estipular um valor e dentro do range dele calcular o quadrado dos numeros pares
N = int(input())
if N > 5 and N < 2000:
    for i in range(1,N+1): #para um numero antes 
        if i%2==0:
            x = i**2
            print(f'{i}^2 = {x}')

'''20'''
#output
'''2^2 = 4   
4^2 = 16  
6^2 = 36  
8^2 = 64  
10^2 = 100
12^2 = 144
14^2 = 196
16^2 = 256
18^2 = 324
20^2 = 400'''
#Sua tarefa é construir um programa que receba como entrada um número natural N (0 <= N <= 10) 
# e exibir a tabuada de N de 1 até 10.
x = int(input())
if x >= 0 and x <= 10:
    i = 1 
    while i <= 10:
        result=x*i
        print(f'{x} x {i} = {result}')
        i+=1


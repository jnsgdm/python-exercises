#criando um programa que receba como entrada um número inteiro N (1 <= N <= 26) e que 
# desenhe um triângulo com exatas N linhas, seguindo a mesma estratégia descrita no texto. 
# Note que o maior triângulo possível é aquele formado por vinte e seis linhas,
#  onde na primeira linha há apenas um caractere 'A' e na última há somente vinte e seis caracteres 'Z'.
x = int(input())

ar = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

i = 0
count = 0 

if x >= 1 and x <=26:
    while i < x:
        print(ar[count]*(i+1))#multplicando a variaveis, exemplo: ar[0] = A * (0+1) == A*1 == A, ar[1] = B *(1+1) == B*2 == BB
        i+=1
        count+=1


#Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
n = int(input())
i = 1
divis = 0
while i <= n:#loop que executa até chegar no valor do numero passado 
    if n%i==0:#verifica se o resto de suas divisões pelo contador é = 0
        divis+=1 #se for soma +1
    i+=1
if divis==2: #se suas contagens de divisões forem = 2
    print(f'{n} é primo') #são primos
else:
    print(f'{n} n é primo')
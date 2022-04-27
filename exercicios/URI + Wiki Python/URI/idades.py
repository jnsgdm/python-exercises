#Faça um algoritmo para ler um número indeterminado de dados, contendo cada um, a idade de um indivíduo.
#  O último dado, que não entrará nos cálculos, contém o valor de idade negativa. 
# Calcular e imprimir a idade média deste grupo de indivíduos.
sm = 0
i = 0
while True:
    n = int(input())
    if n >= 0:
        i+=1
        sm = n+sm
        media =sm/i
    else:
        break
print('%.2f'%(media))
import math
import cmath

funcsMath = dir(math)
funcsCmath = dir(cmath)
ar = []
num = 0
haveSameName = False

for i in funcsCmath:
    if funcsMath[num] == i:
        haveSameName = True
        ar.append(funcsMath[num])
    num+=1

if haveSameName == True:
    print('Os modulos Math e Cmath possuem funções iguais.')
    print('As funções iguais são:\n')
    print(ar)
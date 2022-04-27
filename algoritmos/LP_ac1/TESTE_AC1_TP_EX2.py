def completeNulls(ar):
    i = 0
    while i < len(ar):
        if ar[i]==0:
            ar[i] = 1
        if ar[i] < 0:
            ar[i] = 1
        i+=1
    print(f'Lista com os valores Nulos corrigidos:\n {ar}')

x = 1
ar = []
print('Adicione 20 valores na lista...')
while x <= 20: 
    values = int(input(f'Valor {x}: '))
    ar.append(values)
    x+=1

print(f'Lista com os valores digitados:\n {ar}')

completeNulls(ar)


#exemplo do outpu
# Adicione 20 valores na lista...
# Valor 1: 0
# Valor 2: 0
# Valor 3: -3
# Valor 4: -76
# Valor 5: 77
# Valor 6: 27
# Valor 7: -4
# Valor 8: 32
# Valor 9: 36
# Valor 10: 28
# Valor 11: 16
# Valor 12: 12
# Valor 13: 0
# Valor 14: 0
# Valor 15: -7 
# Valor 16: -18
# Valor 17: 0
# Valor 18: 0
# Valor 19: -9
# Valor 20: 8
# Lista com os valores digitados:
#  [0, 0, -3, -76, 77, 27, -4, 32, 36, 28, 16, 12, 0, 0, -7, -18, 0, 0, -9, 8]
# Lista com os valores Nulos corrigidos:
#  [1, 1, 1, 1, 77, 27, 1, 32, 36, 28, 16, 12, 1, 1, 1, 1, 1, 1, 1, 8]
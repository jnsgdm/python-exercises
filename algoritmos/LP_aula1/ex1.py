ar = []
i = 0

while i < 5:
    x = int(input('Passe um número: '))
    ar.append(x)
    i+=1

soma = sum(ar)

print(f'Os elementos da lista são: {ar}')
print(f'A soma dos elementos é: {soma}')

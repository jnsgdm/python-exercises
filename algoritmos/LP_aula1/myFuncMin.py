def minhaFuncMin(ar):
    i = 0
    mn = ar[0]

    while i < len(ar): 
        if ar[i] < mn:
            mn = ar[i]
        i+=1
    print(f'O menor numero é: {mn}')

ar = [5,6,92,1,3,5,7,0]

trueAr = sorted(ar)

commands = 0

while commands < 10:
    commands+=1

minhaFuncMin(trueAr)
print(f'Foram executados {commands} comandos')
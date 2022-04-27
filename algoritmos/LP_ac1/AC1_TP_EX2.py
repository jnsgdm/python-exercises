def completeNulls(ar):
    i = 0
    while i < len(ar):
        if ar[i]==0:
            ar[i] = 1
        if ar[i] < 0:
            ar[i] = 1
        i+=1
    print(f'Completando valores nulos:\n {ar}')

ar = [1,2,-3,0,0,0,0,32,81,-9,-7,0,17,77,0,-88,0,-16,20,-21]
completeNulls(ar)

#Exemplo do outpu
#Completando valores nulos:
# [1, 2, 1, 1, 1, 1, 1, 32, 81, 1, 1, 1, 17, 77, 1, 1, 1, 1, 20, 1]
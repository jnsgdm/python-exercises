def maxNegative(ar):
    i = 0
    arNeg = []
    while i < len(ar):
        if ar[i] < 0:
            arNeg.append(ar[i])
        i+=1

    maxNeg = arNeg[0] 
    for x in arNeg:
        if x > maxNeg:
            maxNeg = x

    print(f'O maior número negativo é: {maxNeg}')

ar = [10,9,-23,-4,50,-19,97,-17679,-98]

maxNegative(ar)

#exemplo do output
#O maior número negativo é: -4
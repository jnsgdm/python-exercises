def myFuncSum(ar):
    i = 0
    sm = 0
    while i < len(ar):
        sm+=ar[i]
        i+=1
    print(f'A soma dos valores é: {sm}')

def media(ar):
    i = 0
    sm = 0
    while i < len(ar):
        sm+=ar[i]
        i+=1
    media = sm/len(ar)
    print(f'A média dos valores é: {media}')

ar = list(range(1,101))
print(f'O vetor é: {ar}')
newAr = []
for i in ar:
    if i >= 10:
        print(f'As posições maiores e iguais a 10 na lista com seus valores são: {ar.index(i)} = {i} ')
        newAr.append(i)

myFuncSum(newAr)
media(newAr)

#exemplo do output

# O vetor é: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 
# 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
# As posições maiores e iguais a 10 na lista com seus valores são: 9 = 10 
# As posições maiores e iguais a 10 na lista com seus valores são: 10 = 11
# As posições maiores e iguais a 10 na lista com seus valores são: 11 = 12
# As posições maiores e iguais a 10 na lista com seus valores são: 12 = 13
# As posições maiores e iguais a 10 na lista com seus valores são: 13 = 14
# As posições maiores e iguais a 10 na lista com seus valores são: 14 = 15
# As posições maiores e iguais a 10 na lista com seus valores são: 15 = 16
# As posições maiores e iguais a 10 na lista com seus valores são: 16 = 17
# As posições maiores e iguais a 10 na lista com seus valores são: 17 = 18
# As posições maiores e iguais a 10 na lista com seus valores são: 18 = 19
# As posições maiores e iguais a 10 na lista com seus valores são: 19 = 20
# As posições maiores e iguais a 10 na lista com seus valores são: 20 = 21
# As posições maiores e iguais a 10 na lista com seus valores são: 21 = 22
# As posições maiores e iguais a 10 na lista com seus valores são: 22 = 23
# As posições maiores e iguais a 10 na lista com seus valores são: 23 = 24
# As posições maiores e iguais a 10 na lista com seus valores são: 24 = 25
# As posições maiores e iguais a 10 na lista com seus valores são: 25 = 26
# As posições maiores e iguais a 10 na lista com seus valores são: 26 = 27
# As posições maiores e iguais a 10 na lista com seus valores são: 27 = 28
# As posições maiores e iguais a 10 na lista com seus valores são: 28 = 29
# As posições maiores e iguais a 10 na lista com seus valores são: 29 = 30
# As posições maiores e iguais a 10 na lista com seus valores são: 30 = 31
# As posições maiores e iguais a 10 na lista com seus valores são: 31 = 32
# As posições maiores e iguais a 10 na lista com seus valores são: 32 = 33
# As posições maiores e iguais a 10 na lista com seus valores são: 33 = 34
# As posições maiores e iguais a 10 na lista com seus valores são: 34 = 35
# As posições maiores e iguais a 10 na lista com seus valores são: 35 = 36
# As posições maiores e iguais a 10 na lista com seus valores são: 36 = 37
# As posições maiores e iguais a 10 na lista com seus valores são: 37 = 38
# As posições maiores e iguais a 10 na lista com seus valores são: 38 = 39
# As posições maiores e iguais a 10 na lista com seus valores são: 39 = 40
# As posições maiores e iguais a 10 na lista com seus valores são: 40 = 41
# As posições maiores e iguais a 10 na lista com seus valores são: 41 = 42
# As posições maiores e iguais a 10 na lista com seus valores são: 42 = 43
# As posições maiores e iguais a 10 na lista com seus valores são: 43 = 44
# As posições maiores e iguais a 10 na lista com seus valores são: 44 = 45
# As posições maiores e iguais a 10 na lista com seus valores são: 45 = 46
# As posições maiores e iguais a 10 na lista com seus valores são: 46 = 47
# As posições maiores e iguais a 10 na lista com seus valores são: 47 = 48
# As posições maiores e iguais a 10 na lista com seus valores são: 48 = 49
# As posições maiores e iguais a 10 na lista com seus valores são: 49 = 50
# As posições maiores e iguais a 10 na lista com seus valores são: 50 = 51
# As posições maiores e iguais a 10 na lista com seus valores são: 51 = 52
# As posições maiores e iguais a 10 na lista com seus valores são: 52 = 53
# As posições maiores e iguais a 10 na lista com seus valores são: 53 = 54
# As posições maiores e iguais a 10 na lista com seus valores são: 54 = 55
# As posições maiores e iguais a 10 na lista com seus valores são: 55 = 56
# As posições maiores e iguais a 10 na lista com seus valores são: 56 = 57
# As posições maiores e iguais a 10 na lista com seus valores são: 57 = 58
# As posições maiores e iguais a 10 na lista com seus valores são: 58 = 59
# As posições maiores e iguais a 10 na lista com seus valores são: 59 = 60
# As posições maiores e iguais a 10 na lista com seus valores são: 60 = 61
# As posições maiores e iguais a 10 na lista com seus valores são: 61 = 62
# As posições maiores e iguais a 10 na lista com seus valores são: 62 = 63
# As posições maiores e iguais a 10 na lista com seus valores são: 63 = 64
# As posições maiores e iguais a 10 na lista com seus valores são: 64 = 65
# As posições maiores e iguais a 10 na lista com seus valores são: 65 = 66
# As posições maiores e iguais a 10 na lista com seus valores são: 66 = 67
# As posições maiores e iguais a 10 na lista com seus valores são: 67 = 68
# As posições maiores e iguais a 10 na lista com seus valores são: 68 = 69
# As posições maiores e iguais a 10 na lista com seus valores são: 69 = 70
# As posições maiores e iguais a 10 na lista com seus valores são: 70 = 71
# As posições maiores e iguais a 10 na lista com seus valores são: 71 = 72
# As posições maiores e iguais a 10 na lista com seus valores são: 72 = 73
# As posições maiores e iguais a 10 na lista com seus valores são: 73 = 74
# As posições maiores e iguais a 10 na lista com seus valores são: 74 = 75
# As posições maiores e iguais a 10 na lista com seus valores são: 75 = 76
# As posições maiores e iguais a 10 na lista com seus valores são: 76 = 77
# As posições maiores e iguais a 10 na lista com seus valores são: 77 = 78
# As posições maiores e iguais a 10 na lista com seus valores são: 78 = 79
# As posições maiores e iguais a 10 na lista com seus valores são: 79 = 80
# As posições maiores e iguais a 10 na lista com seus valores são: 80 = 81
# As posições maiores e iguais a 10 na lista com seus valores são: 81 = 82
# As posições maiores e iguais a 10 na lista com seus valores são: 82 = 83
# As posições maiores e iguais a 10 na lista com seus valores são: 83 = 84
# As posições maiores e iguais a 10 na lista com seus valores são: 84 = 85
# As posições maiores e iguais a 10 na lista com seus valores são: 85 = 86
# As posições maiores e iguais a 10 na lista com seus valores são: 86 = 87
# As posições maiores e iguais a 10 na lista com seus valores são: 87 = 88
# As posições maiores e iguais a 10 na lista com seus valores são: 88 = 89
# As posições maiores e iguais a 10 na lista com seus valores são: 89 = 90
# As posições maiores e iguais a 10 na lista com seus valores são: 90 = 91
# As posições maiores e iguais a 10 na lista com seus valores são: 91 = 92
# As posições maiores e iguais a 10 na lista com seus valores são: 92 = 93
# As posições maiores e iguais a 10 na lista com seus valores são: 93 = 94
# As posições maiores e iguais a 10 na lista com seus valores são: 94 = 95
# As posições maiores e iguais a 10 na lista com seus valores são: 95 = 96
# As posições maiores e iguais a 10 na lista com seus valores são: 96 = 97
# As posições maiores e iguais a 10 na lista com seus valores são: 97 = 98
# As posições maiores e iguais a 10 na lista com seus valores são: 98 = 99
# As posições maiores e iguais a 10 na lista com seus valores são: 99 = 100
# A soma dos valores é: 5005
# A média dos valores é: 55.0
A = { 7, 2, 5, 8, 4} 
B = {4, 2, 5, 10}
C = A | B
print(C)
#ou
D = [3, 9, 11]
E = [2, 6, 11]
F = []
for x in D:
    F.append(x)
i = 0
for y in E:
    if y != F[i]:
        F.append(y)
    i+=1
print(F) 


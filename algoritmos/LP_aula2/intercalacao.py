A = [1,2,3,4]
B = [5,6,7,8]
C = []

for x,y in zip(A,B):
    C.append(x)
    C.append(y)
print(C)
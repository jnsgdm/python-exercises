A = [7, 2, 5, 8, 4]
B = [7,8,9,0,1]
C = []
for x in A:
    if x in B:
        C.append(x)
print(C)
#ou
A = {1,2,3,4,5}
B = {2,5}
print(A&B)
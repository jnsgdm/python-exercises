ar = [1,2,7,10,4,89987432819,1999,0]

i = 0
mr = ar[0]

while i < len(ar):
    if ar[i] > mr:
        mr = ar[i]
    i+=1

print(mr)

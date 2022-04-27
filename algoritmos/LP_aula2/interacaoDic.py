x = {1:'a',2:'b',3:'c',5:'d',8:'e',13:'f',21:'g'}

it = iter(x)
try:
    while True:
        i = next(it)
        print(i, x[i])

except StopIteration:
    print("final 1")
    pass

for i in x:
    print(i, x[i])
else:
    print("final 2")

#SIM!
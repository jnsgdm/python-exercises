students = int(input())
og = []
fn = []

count = 0
while count < students:
    original = float(input())
    og.append(original)
    count+=1

count_2 = 0
final = 0
count_modify = 0 
while count_2 < students:
    second_notes = float(input())
    for i in range(len(og)):
        if second_notes == 10:
            final = og[i]+2
            if final >= 10:
                final = 10
            fn.append(final)    
        else:
            fn.append(og[i])
    count_2+=1

for x in range(len(og)):
    if fn[x] != og[x]:
        count_modify += 1

print(f'NOTAS ALTERADAS: {count_modify}')
for i in range(students):
    modify = ''
    if og[i] != fn[i]:
        modify = '*'
    else: 
        modify = '-'
    print(f'{modify}({i+1:03}) original: {og[i]:05.2f} | final: {fn[i]:05.2f}')

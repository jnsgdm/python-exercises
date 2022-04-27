ar  = []

while True:
    time_sec = int(input())
    if time_sec > 0:
        ar.append(time_sec)
    else:
        total = len(ar)
        sm = sum(ar)    
        media = sm/total
        print(f'MEDIA: {media:.2f}')
        if media == min(ar):
            print('')
        else:
            for i in ar:
                if i < media:
                    print(i)
        break
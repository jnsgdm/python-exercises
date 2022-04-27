#adicionar 100 itens a uma lista, mostar a o maior e a posição dele
ar = []
i = 0
while i < 100:
    n = int(input())
    ar.append(n)
    i+=1
mx = max(ar)
pstn = ar.index(mx)+1 #nao quero que comece com 0 
print(mx)
print(pstn)
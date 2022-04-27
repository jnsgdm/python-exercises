import time

#Teste de velocidade dos diversos modos de iniciar uma lista

tamanho = 20000000

#Teste 1: append
inicio = time.time()

l1 = []
for i in range(tamanho):
    l1.append(0)

final = time.time()

tempo = final - inicio
print("Duração= %.2f seg. (append)"%(tempo))

#Teste 2: tamanho * [0]
inicio = time.time()

l1 = tamanho * [0]

final = time.time()

tempo = final - inicio
print("Duração= %.2f seg. (tamanho * [0])"%(tempo))


#Teste 3: comprehension
inicio = time.time()

l1 = [0 for i in range(tamanho)]

final = time.time()

tempo = final - inicio
print("Duração= %.2f seg. (list comprehension)"%(tempo))

#output
# Duração= 13.37 seg. (append)
# Duração= 0.44 seg. (tamanho * [0])
# Duração= 4.88 seg. (list comprehension)
'''Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" 
O programa deve no final emitir uma classificação 
sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 
questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 
5 como "Assassino". Caso contrário, ele será classificado como "Inocente".'''

ar = [
    "Telefonou para a vítima?",
    "Esteve no local do crime?",
    "Mora perto da vítima?",
    "Devia para a vítima?",
    "Já trabalhou com a vítima?"
]

count = 0 
while True:
    for i in ar:
        print(i)
        res = input('sim ou nao: ')
        if res == 'sim':
            count+=1
        
    if count <= 1:
        print('inocente')
    elif count == 2:
        print('suspeito')
    elif count <= 4:
        print('cumplice')
    elif count == 5:
        print('assassino')
    break

#output
'''Telefonou para a vítima?
sim ou nao: sim
Esteve no local do crime?
sim ou nao: sim
Mora perto da vítima?
sim ou nao: sim
Devia para a vítima?
sim ou nao: sim     
Já trabalhou com a vítima?
sim ou nao: sim
assassino'''

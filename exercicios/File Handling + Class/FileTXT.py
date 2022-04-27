# como criaar e modificar arquivos 
values = [30,400,5000,678,128,90]
'''

'r' -> Usado apenas para ler algo 
'w' -> Usado apenas para escrever algo
'r+' -> Usado para ler e escrever algo 
'a' -> Usado para acrescentar algo 

'''
with open('valores.txt','w') as file: 
#especificando o nome do arquivo que deve ser aberto, ação q ele recebra e o nome dele no programa
#se esse arquivo nao existir ele sera criado    

    for value in values:#lendo tds os valores no array de dados 

        file.write(str(value)+'\n')#escrevendo os valores dentro do arquivo e quebrando uma linha 
        #os valores tem que ser no formato de string
        ### o 'w' sobresqueve os valores salvos, ou seja, apaga tudo e escreve algo e cima


with open('valores.txt','a') as file: 
    for value in values:
        file.write(str(value)+'\n')
    ### o 'a' acrescenta algo, ou seja, adiciona valores sem apagar os anteriores

with open('valores.txt','r') as file: 
    for value in values:
        print(value) #ira printar os valores do array
    ### o 'r' apenas le as informações, ou seja, útil apenas apra o programa pegar dados de um arquivo já existente

with open('valores.txt','r') as file: 
    for value in file: #rodando o loop direto no arquivo 
        print(value) #nesse caso sera printado os dados reais do arquivo

with open('valores.txt','r+') as file: 
    for value in file:
        print(value) #ler tds os valores
    file.write('456') #adicionar um valor novo
    ### o 'r+' ler e escrever 
        
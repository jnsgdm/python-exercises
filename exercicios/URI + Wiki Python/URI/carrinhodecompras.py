#carrinho de compras
itens = input().split()
if itens != []:
    x = range(len(itens))
    for i in x:
        itens[i] = int(itens[i]) #parse int

while True:
    command = input().split()
    if command[0] == 'adicionar':
        itens.append(int(command[1]))
    if command[0] == 'exibir':
        total = len(itens)
        itens.sort()
        x = range(total)
        for i in x:
            if i < total-1:
                print(itens[i], end=' ')
            else:
                print(itens[i])
    if command[0] == 'remover':
        command[1] = int(command[1])
        if command[1] in itens:
            itens.remove(command[1])
        else:
            print(f'código {command[1]} não encontrado')
    if command[0] == 'encerrar':
        itens.sort()
        x = range(len(itens))
        for i in x:
            if i < len(itens) -1:
                print(itens[i], end=' ')
            else:
                print(itens[i])
        break
    



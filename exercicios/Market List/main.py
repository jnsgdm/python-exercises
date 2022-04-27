import os 
import time

#lista de mercado...

ar = ['Miojo','Nugets','Água']

def initial():
    print('\n#### LISTA DE MERCADO ###\n')
    
    print('[1] - Ver Lista')
    print('[2] - Add Produtos')
    print('[3] - Excluir Produtos') 
    print('[4] - Arualizar Produtos') 
    print('[5] - Sair')

def clear():
    os.system('clear') or None
    
def request_1():
    while True:
        try:
            res = int(input('\nDigite o inteiro respectivo para cada ação: '))
            return res
        except ValueError:
            print('\nDigite um o INTEIRO (1 a 5) referente a ação desejada.\n')

def show_itens():
    i = 0
    count = 0
    total = len(ar)
    while i < total:
        position = i+1
        print(f'{position}° - {ar[count]}')
        count+=1
        i+=1

def do_control():
    while True:
        res_1 = request_1()
        if res_1 == 1:
            clear()
            print('##Itens na lista##\n')
            if ar == []:
                print('Ainda não tem itens na lista...')
            show_itens()
            res_2 = input('\nPara voltar as opções aperte ENTER...')
            if res_2 == '':
                res_1 = 0
                clear()
                initial()
        if res_1 == 2:
            clear()                
            new_data = str(input('Insira um produto na lista: '))
            ar.append(new_data)
            print('\nAdicionando item...')
            time.sleep(1.5)
            clear()                
            initial()
        if res_1 == 3:
            clear()
            show_itens()
            print('\n(para voltar aperte enter...)')
            x = input('\nDigite o item que dejesa excluir: ')
            if x == '':                   
                clear()
                initial()
            else:
                ar.remove(x)
                clear()
                initial()
        if res_1 == 4:
            clear()
            print('##Itens na lista##\n')
            show_itens()
            update = str(input('\nO que deseja escrever no lugar: '))
            if update == '':
                clear()
                initial()
            else:
                index = int(input('\nPasse a posição do iten desejado: '))
                real_index=index-1
                ar[real_index] = update
                clear()
                initial()
        if res_1 == 5:
            clear()
            print('Até mais..')
            time.sleep(1.0)
            break

def start():
    initial()
    do_control()

start()
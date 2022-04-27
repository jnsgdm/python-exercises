import random 
import os
import time

def inital_mensage():
    print('\n-----------------------------------------------------------------------')
    print('\tGOSTARIA DE TESTAR SUA SORTE?')
    print('-----------------------------------------------------------------------')

def explain_game():
    print('\n-----------------------------------------------------------------------')
    print('\n\tPENSAREI NUM NÚMERO INTEIRO DE 0 A 15...')
    print('\n\tVC TERÁ 5 TENTATIVAS PARA ACERTAR!')
    print('\n-----------------------------------------------------------------------')

def create_random():
    random_int = random.randrange(0,15)
    return random_int #conseguir acessar o numero gerado

def clean():
    os.system('clear') or None

def winner_mensage():
    print('PARABENSSS!!! VC ACERTOU!!!')
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

number = create_random()
tries = 0
def try_lucky(n,t): 
    while True:
        try: #tramento de erros 
            guess = int(input('\nTente um numero:'))
            if guess < 0 or guess > 15:
                print('Tente de novo um numero dentro do range de 0 a 15!')
            elif guess > n:
                print('Tente um numero menor!')
                t += 1
            elif guess < n:
                print('Tente um numero maior!')
                t += 1 
            elif guess == n:
                time.sleep(1.5)
                winner_mensage()
                print('\nGostaria de jogar de novo?')
                restart = input('(sim/nao)')
                if restart.lower() == 'sim' or restart.lower() == 's':
                    clean()
                    t = 0 #zerando tentativas
                    n = create_random() #gerando novo numero
                    continue
                elif restart.lower() == 'nao' or restart.lower() == 'n':
                    clean()
                    time.sleep(0.5)
                    print('ADEUS!')
                    time.sleep(0.5)
                    break
            if t == 5: #limite de tentativas
                time.sleep(0.5)
                clean()
                print('### SUAS TENTATIVAS ACABARAM ###')
                time.sleep(1.0)
                print('\nGostaria de jogar de novo?')
                restart = input('(sim/nao)')
                if restart.lower() == 'sim' or restart.lower() == 's':
                    clean()
                    n = create_random()
                    t = 0 
                    continue
                elif restart.lower() == 'nao' or restart.lower() == 'n':
                    clean()
                    time.sleep(0.5)
                    print('ADEUS!')
                    time.sleep(0.5)
                    break
        except ValueError: #caso nao seja um inteiro apresente esse erro 
            print('DIGITE UM NUMERO INTEIRO!!!')

def play_game():
    start = input('sim ou nao:')
    if start.lower() == 'sim' or start.lower() == 's':
        clean()
        time.sleep(0.5)
        explain_game()
        time.sleep(1.5)
        try_lucky(number,tries)
    elif start.lower() == 'nao' or start.lower() == 'n':
        clean()
        print('ADEUS!')
        time.sleep(0.5)
        
inital_mensage()
play_game()

    
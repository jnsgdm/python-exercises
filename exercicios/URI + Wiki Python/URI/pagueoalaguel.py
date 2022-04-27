# Vic Coin, em que cada unidade equivale à R$ 2,50
#Seu papel é criar um programa que receba como entrada diversas doações feitas em Vic Coin e, ao final, 
# exiba o total em Vic Coin (VCS) e o total convertido para reais (R$).
total = int(input())
value = int(input())

antes = depois = count = i = 0
while i < total:
    count += 1
    antes = total-i
    depois = antes-value
    if depois <= 0:
        depois=0
    print(f'pagamento: {count}')
    print(f'antes = {antes}')
    print(f'depois = {depois}')
    print('-'*5)
    i += value
    
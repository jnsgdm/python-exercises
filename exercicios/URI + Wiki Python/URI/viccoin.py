#Como Ramón não tem um controle adequado para atualizar o valor da 
# dívida de acordo com os valores pagos, pediu sua ajuda para construir um programa que receba 
# como entrada o valor da dívida e o valor que se comprometeu a pagar mensalmente, 
# o programa deve exibir, mês a mês, o valor da dívida antes e depois do pagamento.
'''ar = []
while True:
    x = float(input())
    if x <= -1:
        break
    else:
        ar.append(x)
        total = sum(ar)
    i = 0 
    while i <= total:
        to_real = (total*2.5)
        i+=1
print('VCS %.2f'%total)
print('R$ %.2f'%to_real)''' 


total = x = 0
while x >= 0:
    total = total+x
    x = float(input())
    to_real = total*2.5

print('VC$ %.2f'%total)
print('R$ %.2f'%to_real)


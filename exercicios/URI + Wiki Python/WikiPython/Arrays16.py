'''Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões. 
O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. 
Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, 
ou seja, um total de $470. Escreva um programa (usando um array de contadores) 
que determine quantos vendedores receberam salários nos seguintes intervalos de valores:
$200 - $299
$300 - $399
$400 - $499
$500 - $599
$600 - $699
$700 - $799
$800 - $899
$900 - $999
$1000 em diante
Desafio: Crie ma fórmula para chegar na posição da lista a partir do salário, sem fazer vários ifs aninhados'''

ar = [
    '$200 - $299',
    '$300 - $399',
    '$400 - $499',
    '$500 - $599',
    '$600 - $699'
    '$700 - $799',
    '$800 - $899',
    '$900 - $999',
    '$1000 em diante.'
]

sell = int(input('Qual a sua comissão bruta em vendas: '))
extra = sell*0.09
salary = 200+extra

i = 0
start = 200
end = 299
while i < 9:#total de elementos no ar 
    if salary in range(start,end+1):
        print('Seu salario, na semana, estará entre: ', ar[i])
    i+=1
    start+=100
    end+=100

# input
# 4000
#output 
# Seu salario, na semana, estará entre:  $500 - $599
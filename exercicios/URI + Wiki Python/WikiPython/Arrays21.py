#Exercicio 21
#O modelo do carro mais econômico;
#Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma 
# distância de 1000 quilômetros e quanto isto custará, considerando um que a gasolina custe R$ 2,25 o litro. 
# Abaixo segue uma tela de exemplo. O disposição das informações deve ser o mais próxima possível ao exemplo. 
# Os dados são fictícios e podem mudar a cada execução do programa.

cars = []
kml = []
ar = []

#input
i = 0
while i < 5:
    i+=1 #printar a partir do 1 
    print(f'Escolha o {i}° carro...')
    cars.append(input('Carro: '))
    kml.append(float(input('km/l: ')))
    
#conta e print dos dados
qnt = len(cars)
count1 = 0
n = 0
while n < qnt:
    n+=1 #printar a partir do 1
    l = 1000/kml[count1] #litros
    cost = l*2.25
    ar.append(cost) #armazenando os custos 
    print(f'{n} -  {cars[count1]} - {round(l,2)} litros - R$ {round(cost,2)}\n')
    count1+=1

#comparativos dos custos com os respectivos carros
car = ''
low = min(ar)
count2 = 0
x = 0
while x < qnt:
    if ar.index(low) == cars.index(cars[count2]):
        car = cars[count2]
    count2+=1
    x+=1

print(f'Melhor opção para a viagem é com o {car}, vc irá gastar R${round(low,2)}.')  


#exemplo de output
'''1 -  Gol - 142.86 litros - R$ 321.43

2 -  Golf - 81.3 litros - R$ 182.93

3 -  Up - 76.92 litros - R$ 173.08

4 -  A3 - 51.02 litros - R$ 114.8

5 -  Del Rey - 294.12 litros - R$ 661.76

Melhor opção para a viagem é com o A3, vc irá gastar R$114.8.'''

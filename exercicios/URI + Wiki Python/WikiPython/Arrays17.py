# Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas 
# pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos.
# O programa deve ser encerrado quando não for informado o nome do atleta.

ar = []
asks = ['Primeiro Salto: ','Segundo Salto: ','Terceiro Salto: ','Quarto Salto: ','Quinto Salto: ']
while True:
    name = input('Atleta: ')
    if name == '':
        break
    else:
        i = 0
        ask = 0
        while i < 5:
            jump = float(input(f'{asks[ask]}'))
            ar.append(jump)
            i+=1
            ask+=1

        jumps = sum(ar)
        total = len(ar)
        media = (jumps/total)

        print('Resultado fianl: ')
        print(name)
        print(f'Saltos: {ar[0]}m - {ar[1]}m - {ar[2]}m - {ar[3]}m - {ar[4]}m')
        print(f'Media dos saltos: {round(media,2)}m')
        break
#O programa deverá ler os valores até ser informado o valor 0, 
# que encerra a entrada dos dados. Não deverão ser aceitos valores além dos válidos para o programa (0 a 6). 
# Após os dados terem sido completamente informados, o programa deverá calcular a percentual de cada um dos 
# concorrentes e informar o vencedor da enquete.

windows = 0
linux = 0
unix = 0 
macos = 0 
def print_opitions():
    print('"Qual o melhor Sistema Operacional para uso em servidores?"\n')
    print('1- Windows Server\n''2- Linux\n''3- Unix\n''5- Mac OS\n')
    print('finalizar votação digitar 0')
print_opitions()

while True:
    vote = int(input('Vote em algum...\n'))
    if vote == 1:
        windows+=1
    elif vote == 2:
        linux+=1
    elif vote==3:
        unix+=1
    elif vote==4:
        macos+=1
    elif vote==0:
        break

ar = [windows,linux,unix,macos]
total = sum(ar)

pW = (windows*100)/total
pL = (linux*100)/total
pU = (unix*100)/total
pM = (macos*100)/total

print('Sitemas operacionais - Votos - %')
print(f'Windows: {ar[0]} votos {round(pW)}% \n')
print(f'Linux: {ar[1]} votos {round(pL)}% \n')
print(f'Unix: {ar[2]} votos {round(pU)}% \n')
print(f'MacOS: {ar[3]} votos {round(pM)}% \n')

#output
'''Windows: 5 votos 24%

Linux: 4 votos 19%

Unix: 10 votos 48%

MacOS: 2 votos 10%'''
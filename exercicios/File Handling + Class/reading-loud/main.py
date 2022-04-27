import gtts 
from playsound import playsound

with open('teste.txt','r') as file: #operação para ler arquivos
    for line in file: #loop para ler tds as linhas no arquivo 
        text=gtts.gTTS(line,lang='pt-br') #especificando oq no arquivo deve ser lido e em qual lingua 
        text.save('teste.mp3') #salvando em um arquivo de som 
        playsound('teste.mp3') #"lendo o arquivo em voz alta"

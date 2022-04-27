import schedule
from datetime import datetime
import time 
import random

def insert_datas():
    value = round(random.uniform(1,7),2)
    day = datetime.now().replace(microsecond=0)
    with open('dados.txt','a') as file:
        file.write('Hoje: '+str(day)+'\n')
        file.write('Valor do dolar: $'+str(value)+'\n')
    print('Dados inseridos...')
    
schedule.every(5).seconds.do(insert_datas)

while True:
    schedule.run_pending()
    time.sleep(1) 

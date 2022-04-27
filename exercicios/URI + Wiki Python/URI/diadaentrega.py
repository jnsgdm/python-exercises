week_day = input()
day_count = int(input())

hoje = 'hoje'
domingo = 'domingo'
segunda = 'segunda'
terca = 'terca'
quarta = 'quarta'
quinta = 'quinta'
sexta = 'sexta'
sabado = 'sabado' 

if week_day == 'domingo':
	if day_count == 0:
		print(f'chega {hoje}!')
	elif day_count==1:
		print(f'sera entregue {segunda}')
	elif day_count==2:
		print(f'sera entregue {terca}')	
	elif day_count==3:
		print(f'sera entregue {quarta}')	
	elif day_count==4:
		print(f'sera entregue {quinta}')	
	elif day_count==5:
		print(f'sera entregue {sexta}')	
	elif day_count==6:
		print(f'sera entregue {sabado}')
elif week_day == 'segunda':
	if day_count == 0:
		print(f'chega {hoje}!')
	elif day_count==1:
		print(f'sera entregue {terca}')
	elif day_count==2:
		print(f'sera entregue {quarta}')	
	elif day_count==3:
		print(f'sera entregue {quinta}')	
	elif day_count==4:
		print(f'sera entregue {sexta}')	
	elif day_count==5:
		print(f'sera entregue {sabado}')	
	elif day_count==6:
		print(f'sera entregue {domingo}')
elif week_day == 'terca':
	if day_count == 0:
		print(f'chega {hoje}!')
	elif day_count==1:
		print(f'sera entregue {quarta}')
	elif day_count==2:
		print(f'sera entregue {quinta}')	
	elif day_count==3:
		print(f'sera entregue {sexta}')	
	elif day_count==4:
		print(f'sera entregue {sabado}')	
	elif day_count==5:
		print(f'sera entregue {domingo}')	
	elif day_count==6:
		print(f'sera entregue {segunda}')
elif week_day == 'quarta':
	if day_count == 0:
		print(f'chega {hoje}!')
	elif day_count==1:
		print(f'sera entregue {quinta}')
	elif day_count==2:
		print(f'sera entregue {sexta}')	
	elif day_count==3:
		print(f'sera entregue {sabado}')	
	elif day_count==4:
		print(f'sera entregue {domingo}')	
	elif day_count==5:
		print(f'sera entregue {segunda}')	
	elif day_count==6:
		print(f'sera entregue {terca}')
elif week_day == 'quinta':
	if day_count == 0:
		print(f'chega {hoje}!')
	elif day_count==1:
		print(f'sera entregue {sexta}')
	elif day_count==2:
		print(f'sera entregue {sabado}')	
	elif day_count==3:
		print(f'sera entregue {domingo}')	
	elif day_count==4:
		print(f'sera entregue {segunda}')	
	elif day_count==5:
		print(f'sera entregue {terca}')	
	elif day_count==6:
		print(f'sera entregue {quarta}')
elif week_day == 'sexta':
	if day_count == 0:
		print(f'chega {hoje}!')
	elif day_count==1:
		print(f'sera entregue {sabado}')
	elif day_count==2:
		print(f'sera entregue {domingo}')	 
	elif day_count==3:
		print(f'sera entregue {segunda}')	
	elif day_count==4:
		print(f'sera entregue {terca}')	
	elif day_count==5:
		print(f'sera entregue {quarta}')	
	elif day_count==6:
		print(f'sera entregue {quinta}')
elif week_day == 'sabado':
	if day_count == 0:
		print(f'chega {hoje}!')
	elif day_count==1:
		print(f'sera entregue {domingo}')
	elif day_count==2:
		print(f'sera entregue {segunda}')	
	elif day_count==3:
		print(f'sera entregue {terca}')	
	elif day_count==4:
		print(f'sera entregue {quarta}')	
	elif day_count==5:
		print(f'sera entregue {quinta}')	
	elif day_count==6:
		print(f'sera entregue {sexta}')
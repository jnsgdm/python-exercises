print('Digite o id do produto desejado:')
confirmed = False
product_name = input()
datas = ['xiaomi','airpods','iphone 12 pro','ps5','air fryer philips walita']
for product in datas:
    if product == product_name:
        confirmed = True
        local = datas.index(product_name)
if confirmed:
    print(f'Produto encontre-se no setor: {local}.')
else:
    print('Produto não encontrado!')

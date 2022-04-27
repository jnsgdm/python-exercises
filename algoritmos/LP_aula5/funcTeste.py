
def soma(n1,n2):
    return n1+n2

if __name__ == '__main__':
    print('Testando função soma:')
    print('Soma(6,2) => valor esperado: 8')
    if soma(6,2) == 8:
        print("Valor obtido => OK!")
    else:
        print("Valor não obitdo => algo deu errado =(")
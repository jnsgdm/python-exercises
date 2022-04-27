# __initi__ => construtor, cria a função inicial de uma classe e suas propriedades 
# self => acessar as propriedades, atributos ou metodos de uma instância  

#pensar em algo, fazer algo, sentir algo
class Cérebro:
    def __init__(self,pensar,fazer,sentir):
        self.pensar = pensar   
        self.fazer = fazer
        self.sentir = sentir

    def think(self):
        print('pensei em',self.pensar)
    
    def do_something(self):
        print('fiz',self.fazer)

    def feel(self):
        print('senti',self.sentir)
    
pessoa1 = Cérebro('programar!','café.','cheiro de torta de maçã...') #instanciando um objeto
pessoa1.think()
pessoa1.do_something()
pessoa1.feel()
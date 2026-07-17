
def nome(nome):
    print ('Meu nome é {nome}'.format(nome=nome))
    print ('Meu nome é {nome}'.format(nome=nome.upper()))

nome("Paulo")
print("-------------------")

# É um comportamento de um decorator receber uma função como parâmetro, fazer a modificação 
# do comportamento e retornar uma string

class uppercase(object):
    
    def __init__(self, f):
        self.f = f
        print ("Quem é self ? {s} ".format(s=self))
        print ("Quem é f ? É a função promriamente dita =>  {f} ".format(f=f))
        print("======")
        
    def __call__(self, *args):
        self.f(args[0].upper())
        print("Quem é self ? {s} ".format(s=self))
        print("Esse cara é chamado depois do method principal ser atendido pela chamada do decorator")
        print("======")

@uppercase
def nome(nome):
    print('Meu nome é {nome}'.format(nome=nome))

nome("Paulo")

###########################################################################

import time

def calcula_duracao(fun):

    def wrapper():

        tempo_inicial = time.time()
        fun()
        tempo_final = time.time()

        print("[{fun}] Tempo total de execução: {tempo_total}".format(fun=fun.__name__,tempo_total=str(tempo_final - tempo_inicial)))
    
    return wrapper

@calcula_duracao
def funcao_loop():
    for n in range(0, 700000):
        pass

funcao_loop()
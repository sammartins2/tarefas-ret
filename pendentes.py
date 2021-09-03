import random

def tarefas():

    lista = ['Limpar a casa', 'Lavar o banheiro', 'Lavar a louça', 'Lavar a roupa']

    #listar as tarefas embaixo da outra
    for lista in lista: 
        print(lista)

    lista = str(input("Adicionar tarefa: "))
    
    #riscar o texto
    def strike (text):
        return ''.join([u'\u0336{}'.format(tarefas) for tarefas in text])
    print(strike(lista))

    

#if(__name__=="__main__"): 
 #   tarefas()
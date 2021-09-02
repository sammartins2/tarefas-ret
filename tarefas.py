lista = ['Limpar a casa', 'Lavar o banheiro', 'Lavar a louça', 'Lavar a roupa']

#listar as tarefas embaixo da outra
for lista in lista: 
    print(lista)

#riscar o texto
def strike (text):
    return ''.join([u'\u0336{}'.format(lista['Limpar a casa']) for lista in text])
print(strike(lista))

#lista = str(input("Adicionar tarefa: "))

print(lista)

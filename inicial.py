import pendentes
import completas
import total

def escolhe_tarefas():
    print("Bem-Vindo, escolha a tarefa desejada.")

    print("Tarefas pendentes (1), Tarefas completas (2), Tarefas total(3)")

    tarefas = int(input("Qual tarefa deseja escolher? "))

    if(tarefas == 1):
        print()
        print("tarefas pendentes")
        print()
        pendentes.tarefas()

    elif(tarefas == 2):
        print()
        print("tarefas completas")
        print()
        completas.tarefas()

    else:
        tarefas == 3
        print()
        print("Tarefas total")
        print()
        total.tarefas()

if(__name__=="__main__"):
    escolhe_tarefas()
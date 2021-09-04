# Gerenciador de tarefas

- Faca um sistema que gerencie tarefas para uma pessoa.

Requisitos:

1.  O sistema deve ter um script que sera executado pelo usuário
    - Você pode usar quantos arquivos quiser, mas todas as opcoes devem ser mostradas quando esse unico script for executado
    - Pode usar qualquer linguagem, mas deve ser algo que possa ser executado no terminal

1.  O script deve ser executado de maneira interativa e as seguintes opções devem ser dadas (texto pode ser diferente):
    - Visualizar todas as tarefas
    - Visualizar tarefas concluídas
    - Visualizar tarefas pendentes
    - Adicionar tarefa
    - Excluir tarefa(s) (usuário pode selecionar uma ou mais tarefas)
    - Sair
    
1. Após o usuário finalizar uma das opções, o menu principal é mostrado novamente

1. Se o usuário selecionar "Sair", o programa deve ser encerrado.

1. Se o usuário selecionar "Visualizar tarefas", ele deve ver o nome dessa tarefa, a data e o status (in/completo)

1. Para adicionar uma tarefa, o usuário precisa fornecer os seguintes dados:
    - Nome: obrigatório
    - Data: opcional, mas deve ser uma data hoje ou no futuro
    
1. As informações devem ser salvas (em arquivo, por enquanto) e podem ser acessadas a qualquer momento. Quando um usuário rodar os programa novamente, todas as tarefas adicionadas à lista devem estar disponíveis.

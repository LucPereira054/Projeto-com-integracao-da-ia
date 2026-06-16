tarefas=[]

def adcionar_tarefas(descricao):
    tarefa={"descricao": descricao, "status": "pendente"}
    tarefas.append(tarefa)
    print(f"Tarefa '{descricao}' adcionada com sucesso!")

def listar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa encontrada.")
    else:
        for index, tarefa in enumerate(tarefas, start=1):
            print(f"{index}. {tarefa['descricao']} - {tarefa['status']}")

def marcar_concluida(index):
    try:
        tarefas[index-1]["status"]="concluída"
        print("------------------------------------------------")
        print(f"Tarefa '{tarefas[index-1]['descricao']}' marcada como concluída.")
        print("------------------------------------------------")
    except IndexError:
        print("Índice inválido. Nenhuma tarefa encontrada.")

adcionar_tarefas("Estudar Python")
adcionar_tarefas("Fazer exercícios de programação")
listar_tarefas()
marcar_concluida(1)
listar_tarefas()

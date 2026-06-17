import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url="https://api.groq.com/openai/v1/",
    api_key=os.environ.get("GROQ_API_KEY")
)



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



def otimizar_com_ai(lista):
    lista_formatada="\n".join(f"-{t['descricao']} ({t['status']})" for t in lista)
    prompt=f"analise minhas taarefas e sugira uma ordem de execução mais eficiente:\n{lista_formatada}"
    response=client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[{"role":"user","content":prompt}]
        )
    return response.choices[0].message.content


print("\n---Otimização com AI---")
print(otimizar_com_ai(tarefas))


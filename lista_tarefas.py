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
    return tarefas


def marcar_concluida(lista,index):
   idx_corrigido=index-1
   if 0<=idx_corrigido<len(lista):
       lista[idx_corrigido]["status"]="concluida"
       return True
   return False



def otimizar_com_ai(lista):
    lista_formatada="\n".join(f"-{t['descricao']} ({t['status']})" for t in lista)
    prompt=f"Você é um assistente de produtividade pessoal.Analise as tarefas e faça duas coisas:1-Sugira uma ordem de execução mais eficiente, 2-Dê uma dica curta de como priorizar o que é mais importaante. Essas são suas tarefas:\n{lista_formatada}"
    response=client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[{"role":"user","content":prompt}]
        )
    return response.choices[0].message.content




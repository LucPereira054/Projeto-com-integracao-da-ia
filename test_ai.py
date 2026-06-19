import pytest
from unittest.mock import patch
from lista_tarefas import otimizar_com_ai

@patch('lista_tarefas.client.chat.completions.create')
def test_ia_recebe_informacoes(mock_openai):
    # Simulamos uma resposta da IA
    mock_openai.return_value.choices = [
        type('obj', (object,), {'message': type('msg', (object,), {'content': 'Sugestão fake'})})
    ]
    
    tarefas = [{"descricao": "Tarefa A", "status": "pendente"}]
    otimizar_com_ai(tarefas)
    

    args, kwargs = mock_openai.call_args
    mensagens = kwargs.get('messages', [])
    conteudo_enviado = str(mensagens) 
    assert "Tarefa A" in conteudo_enviado


@patch('lista_tarefas.client.chat.completions.create')
def test_ia_devolve_sugestao(mock_openai):
    mock_openai.return_value.choices = [
        type('obj', (object,), {'message': type('msg', (object,), {'content': 'Otimize seu dia'})})
    ]
    
    resultado = otimizar_com_ai([])
    assert resultado == "Otimize seu dia"
    
import streamlit as st
from datetime import datetime
import random

st.set_page_config(page_title="Assistente Virtual", page_icon="🤖")

class AssistenteVirtual:
    def __init__(self):
        self.nome = "Assistente Virtual"

    def responder(self, pergunta):
        pergunta = pergunta.lower()

        if "olá" in pergunta or "oi" in pergunta:
            return random.choice([
                "Olá! Como posso ajudar?",
                "Oi! Em que posso ser útil hoje?"
            ])

        elif "como você está" in pergunta or "tudo bem" in pergunta:
            return "Estou funcionando bem, obrigado! E com você?"

        elif "hora" in pergunta:
            return f"Agora são {datetime.now().strftime('%H:%M')}."

        elif "data" in pergunta:
            return f"Hoje é {datetime.now().strftime('%d/%m/%Y')}."

        elif "matemática" in pergunta:
            return "Posso ajudar com matemática básica, fórmulas e resolução de problemas. Me envie sua dúvida."

        elif "história" in pergunta:
            return "Posso ajudar com dúvidas de história. Se quiser, diga o tema ou o período histórico."

        elif "ciência" in pergunta or "biologia" in pergunta or "física" in pergunta or "química" in pergunta:
            return "Posso tentar ajudar com assuntos de ciências. Faça sua pergunta com detalhes."

        elif "recomenda" in pergunta or "sugestão" in pergunta:
            return "Posso sugerir estudos, organização, rotina, filmes, livros ou ideias do dia a dia. O que você precisa?"

        else:
            return (
                "Entendi. Posso tentar ajudar com isso. "
                "Se quiser, reformule a pergunta com mais detalhes para eu responder melhor."
            )

bot = AssistenteVirtual()

st.title("🤖 Assistente Virtual")
st.write("Um chatbot simples com personalidade amigável para dúvidas do dia a dia e acadêmicas.")

if "mensagens" not in st.session_state:
    st.session_state.mensagens = [
        {"autor": "bot", "texto": "Olá! Eu sou seu assistente virtual. Como posso ajudar?"}
    ]

for msg in st.session_state.mensagens:
    if msg["autor"] == "bot":
        st.chat_message("assistant").write(msg["texto"])
    else:
        st.chat_message("user").write(msg["texto"])

pergunta = st.chat_input("Digite sua pergunta...")

if pergunta:
    st.session_state.mensagens.append({"autor": "user", "texto": pergunta})
    resposta = bot.responder(pergunta)
    st.session_state.mensagens.append({"autor": "bot", "texto": resposta})

    st.chat_message("user").write(pergunta)
    st.chat_message("assistant").write(resposta)

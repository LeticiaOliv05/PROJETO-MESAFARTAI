"""
MESAFARTAI - Aplicação Streamlit integrada
Execute na raiz do projeto: streamlit run src/app.py
"""

from pathlib import Path
import sqlite3
import sys

import pandas as pd
import streamlit as st

PASTA_SRC = Path(__file__).resolve().parent
RAIZ_PROJETO = PASTA_SRC.parent
sys.path.insert(0, str(PASTA_SRC))

from nlu import MotorNLU
from entities import ExtratorEntidades
from matchmaking import MotorMatchmaking

BANCO = RAIZ_PROJETO / "mesafartai.db"

st.set_page_config(
    page_title="MESAFARTAI - Combate à Fome",
    page_icon="🥫",
    layout="wide",
)

nlu = MotorNLU()
extrator = ExtratorEntidades()
matchmaker = MotorMatchmaking(db_path=str(BANCO))

st.title("🥫 MESAFARTAI")
st.caption("Conectando doadores e organizações para combater a fome.")

aba_chat, aba_dashboard = st.tabs(
    ["💬 Chatbot de Doações", "📊 Dashboard de Impacto Social"]
)

with aba_chat:
    st.subheader("Converse com o Assistente de Doações")

    if "mensagens" not in st.session_state:
        st.session_state.mensagens = [{
            "role": "assistant",
            "content": (
                "Olá! Eu sou o assistente do MESAFARTAI. 😊 "
                "Você deseja doar alimentos ou solicitar doações? "
                "Exemplo: Tenho 20 kg de arroz para doar hoje."
            ),
        }]

    for mensagem in st.session_state.mensagens:
        st.chat_message(mensagem["role"]).write(mensagem["content"])

    prompt = st.chat_input("Digite sua mensagem...")
    if prompt:
        st.session_state.mensagens.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)

        resultado = nlu.processar_mensagem(prompt)
        intencao = resultado["intencao"]
        confianca = resultado["confianca"]

        if intencao == "cadastrar_doacao" and confianca >= 0.60:
            dados = extrator.processar_texto(prompt)
            match = matchmaker.encontrar_ong_mais_proxima(-23.615, -46.785)

            resposta = (
                "**Doação identificada!**\n\n"
                f"- **Alimento:** {dados['alimento']}\n"
                f"- **Quantidade:** {dados['quantidade_kg']} kg\n"
                f"- **Validade estimada:** {dados['data_validade']}\n\n"
                "Confira os dados antes de combinar a entrega."
            )

            if match:
                resposta += (
                    "\n\n**ONG mais próxima (KNN):** "
                    f"{match['ong_nome']} "
                    f"(aproximadamente {match['distancia_estimada']} km)."
                )

        elif intencao == "solicitar_alimentos":
            resposta = (
                "Entendi! Sua mensagem foi identificada como uma solicitação "
                "de alimentos. O sistema pode consultar as organizações "
                "cadastradas para ajudar no atendimento."
            )
        elif intencao == "consultar_status":
            resposta = (
                "Para consultar o status, precisamos localizar o registro "
                "da doação ou solicitação no sistema."
            )
        else:
            resposta = resultado.get(
                "resposta",
                "Não entendi. Você deseja doar alimentos ou solicitar doações?",
            )

        st.session_state.mensagens.append(
            {"role": "assistant", "content": resposta}
        )
        st.chat_message("assistant").write(resposta)

with aba_dashboard:
    st.subheader("Indicadores Logísticos e Sociais")

    try:
        with sqlite3.connect(BANCO) as conexao:
            df_ongs = pd.read_sql_query(
                "SELECT id, nome, latitude, longitude "
                "FROM usuarios WHERE tipo = 'ONG'",
                conexao,
            )

        col1, col2, col3 = st.columns(3)
        col1.metric("Total de ONGs cadastradas", len(df_ongs))
        col2.metric("Alimentos arrecadados", "1.250 kg")
        col3.metric("Refeições estimadas", "2.500")

        st.markdown("---")
        st.write("### Unidades de atendimento cadastradas")
        if not df_ongs.empty:
            st.dataframe(df_ongs, use_container_width=True, hide_index=True)
        else:
            st.info("Nenhuma ONG cadastrada no banco de dados.")
    except Exception as erro:
        st.error("Não foi possível carregar os dados do banco.")
        st.caption(f"Verifique o arquivo mesafartai.db. Detalhe: {erro}")

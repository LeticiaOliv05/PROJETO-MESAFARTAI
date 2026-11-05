# Painel de Doações - Aula de Streamlit
# Execute na raiz do projeto: streamlit run app_streamlit.py

import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Painel de Doações", page_icon="🥫", layout="wide")

st.title("🥫 Painel de Doações de Alimentos")
st.caption("Acompanhe as doações e a meta de arrecadação.")

if "doacoes" not in st.session_state:
    st.session_state.doacoes = []

st.sidebar.header("Configurações")
meta = st.sidebar.slider("Meta de arrecadação (kg)", 50, 500, 200, 10)

if st.sidebar.button("Zerar painel"):
    st.session_state.doacoes = []
    st.rerun()

st.subheader("Registrar nova doação")
col1, col2 = st.columns(2)

with col1:
    doador = st.text_input("Nome do doador")
    categoria = st.selectbox(
        "Categoria",
        ["Arroz", "Feijão", "Macarrão", "Óleo", "Enlatados", "Outros"],
    )

with col2:
    quantidade = st.number_input(
        "Quantidade (kg)", min_value=1, max_value=25, value=5, step=1
    )

if st.button("Registrar doação", type="primary"):
    if not doador.strip():
        st.warning("Informe o nome do doador.")
    else:
        st.session_state.doacoes.append({
            "Hora": datetime.now().strftime("%H:%M:%S"),
            "Doador": doador.strip(),
            "Categoria": categoria,
            "Kg": int(quantidade),
        })
        st.success(f"Doação de {quantidade} kg registrada!")

total = sum(item["Kg"] for item in st.session_state.doacoes)
qtd_doacoes = len(st.session_state.doacoes)
faltam = max(meta - total, 0)
progresso = min(total / meta, 1.0)

st.divider()
m1, m2, m3 = st.columns(3)
m1.metric("Total arrecadado", f"{total} kg")
m2.metric("Número de doações", qtd_doacoes)
m3.metric("Faltam para a meta", f"{faltam} kg")
st.progress(progresso, text=f"{progresso:.0%} da meta de {meta} kg")

if total >= meta:
    st.balloons()
    st.success(f"Meta atingida! Foram arrecadados {total} kg.")

if st.session_state.doacoes:
    df = pd.DataFrame(st.session_state.doacoes)
    st.subheader("Doações por categoria")
    st.bar_chart(df.groupby("Categoria")["Kg"].sum())
    st.subheader("Histórico de doações")
    st.dataframe(df, use_container_width=True, hide_index=True)
else:
    st.info("Nenhuma doação registrada ainda. Use o formulário acima!")

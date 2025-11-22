import streamlit as st
import re
from nl2cpc import traducao_nl_para_cpc
from cpc2nl import traduzir_formula

# ===============================
# CONFIGURAÇÕES
# ===============================
st.set_page_config(page_title="NL ↔ CPC", page_icon="🧠", layout="centered")

st.title("🧠 Conversor NL ↔ CPC")
st.write("Tradução entre linguagem natural e lógica proposicional clássica (CPC).")
st.markdown("---")

# ===============================
# 🔁 MODO 1 — NL → CPC
# ===============================
st.subheader("🗣️ Linguagem Natural → Fórmula Lógica (CPC)")

frase = st.text_area("Digite a frase:", height=100, key="entrada_nl")

if st.button("Gerar Fórmula Lógica"):
    if frase.strip() == "":
        st.warning("Digite uma frase antes de converter.")
    else:
        try:
            formula, mapping = traducao_nl_para_cpc(frase)
            st.success(f"**Fórmula lógica gerada:** {formula}")

            if mapping:
                st.markdown("### 🔤 Mapeamento das proposições:")
                for k, v in mapping.items():
                    st.write(f"**{k}** → {v}")

        except Exception as e:
            st.error(f"Erro: {e}")

st.markdown("---")

# ===============================
# 🔁 MODO 2 — CPC → NL
# ===============================
st.subheader("🔤 Fórmula Lógica (CPC) → Linguagem Natural")

formula_cpc = st.text_area(
    "Digite a fórmula lógica (ex: P ∧ ¬Q):",
    height=100,
    key="entrada_cpc"
)

st.markdown("### 📘 Significados")
significados_texto = st.text_area(
    "Informe no formato:\nP = chove\nQ = faz frio\nR = neva",
    height=100,
    key="significados_box"
)

# Converte para dicionário
def parse_significados(txt):
    sig = {}
    for linha in txt.split("\n"):
        match = re.match(r"([A-Za-z])\s*=\s*(.+)", linha.strip())
        if match:
            letra = match.group(1)
            texto = match.group(2).strip()
            sig[letra] = texto
    return sig


if st.button("Traduzir para Português"):
    sig = parse_significados(significados_texto)

    if not sig:
        st.error("Você precisa informar pelo menos 1 significado!")
    else:
        try:
            frase_final = traduzir_formula(formula_cpc, sig)
            st.success("### 📝 Frase gerada:")
            st.write(frase_final)

        except Exception as e:
            st.error(f"Erro ao traduzir: {e}")

st.markdown("---")
st.caption("Feito para atividade NL ↔ CPC")

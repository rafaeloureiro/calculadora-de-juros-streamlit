import streamlit as st

st.title("Calculadora de juros 📈")

def formato_brasil(valor):
    return f"{valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

valor_inicial = st.number_input(
    "Valor inicial (R$)",
    min_value=0.0,
    format="%.2f"
)

valor_final = st.number_input(
    "Valor final (R$)",
    min_value=0.0,
    format="%.2f"
)

if st.button("Calcular"):
    if valor_inicial <= 0:
        st.error("O valor inicial deve ser maior que zero.")
    else:
        juros = valor_final - valor_inicial
        juros_percentual = (juros / valor_inicial) * 100

        st.subheader("Resultado")
        st.write(f"Juros cobrados: **R${formato_brasil(juros)}**")
        st.write(f"Juros percentual: **{formato_brasil(juros_percentual)}%**")

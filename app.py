import streamlit as st

st.title("Calculadora de juros 📈")

st.write("Informe os valores para calcular os juros.")

# Inputs
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

# Botão
if st.button("Calcular"):
    if valor_inicial <= 0:
        st.error("O valor inicial deve ser maior que zero.")
    else:
        juros = valor_final - valor_inicial
        juros_percentual = (juros / valor_inicial) * 100

        st.subheader("Resultado")
        st.write(f"Juros cobrados: **R$ {juros:.2f}**")
        st.write(f"Juros percentual: **{juros_percentual:.2f}%**")

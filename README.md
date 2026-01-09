# Calculadora de juros (Streamlit)

Aplicação simples desenvolvida em **Python + Streamlit** para calcular **juros em valor absoluto e percentual**, a partir de um valor inicial e um valor final.

Ideal para análises rápidas de cobranças, multas, correções ou diferenças de pagamento.

---

## Funcionalidades

* Input do **valor inicial**
* Input do **valor final**
* Cálculo automático de:

  * 💰 Juros cobrados (R$)
  * 📈 Juros percentual (%)
* Interface simples e intuitiva
* Compatível com **Streamlit Cloud**

---

## Fórmulas utilizadas

* **Juros (R$):**

```
juros = valor_final - valor_inicial
```

* **Juros percentual (%):**

```
juros_percentual = (juros / valor_inicial) * 100
```

---

## Estrutura do projeto

```
.
├── app.py
└── requirements.txt
```

---

## Requisitos

Arquivo `requirements.txt`:

```
streamlit
```

---


## 👤 Autor

Desenvolvido por **Rafael Fernandes Loureiro Pereira**

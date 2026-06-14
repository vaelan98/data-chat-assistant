import streamlit as st
import pandas as pd
from openai import OpenAI
from dotenv import load_dotenv
import os

# ── Cargar API key desde .env ──────────────────────────
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# ── Configuración de la página ─────────────────────────
st.set_page_config(
    page_title="Data Chat Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Data Chat Assistant")
st.markdown("Subí un CSV y hacé preguntas sobre tus datos en lenguaje natural.")

# ── Subir archivo CSV ──────────────────────────────────
uploaded_file = st.file_uploader("📂 Subí tu archivo CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.success(f"✅ Archivo cargado: {df.shape[0]} filas × {df.shape[1]} columnas")

    # Preview de los datos
    with st.expander("👀 Ver datos", expanded=True):
        st.dataframe(df.head(10))

    st.divider()

    # ── Chat con los datos ─────────────────────────────
    st.subheader("💬 Preguntale a tus datos")

    # Historial de conversación
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Mostrar historial
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # Input del usuario
    pregunta = st.chat_input("Ej: ¿Cuál es el promedio de ventas? ¿Cuáles son los 5 clientes con mayor riesgo?")

    if pregunta:
        # Mostrar pregunta del usuario
        st.session_state.messages.append({"role": "user", "content": pregunta})
        with st.chat_message("user"):
            st.markdown(pregunta)

        # Preparar contexto del DataFrame para el LLM
        resumen_df = f"""
        El DataFrame tiene {df.shape[0]} filas y {df.shape[1]} columnas.
        Columnas: {list(df.columns)}
        Tipos de datos: {df.dtypes.to_dict()}
        Primeras 3 filas:
        {df.head(3).to_string()}
        Estadísticas básicas:
        {df.describe().to_string()}
        """

        # Llamar al LLM
        with st.chat_message("assistant"):
            with st.spinner("Analizando..."):

                try:
                    respuesta = client.chat.completions.create(
                        model="gpt-4o-mini",
                        messages=[
                            {
                                "role": "system",
                                "content": """Eres un experto en análisis de datos con Python y pandas.
                                El usuario te hace preguntas sobre un DataFrame llamado 'df'.
                                
                                Tu respuesta debe tener SIEMPRE este formato:
                                
                                **Análisis:**
                                [Explicación clara de lo que encontraste en los datos]
                                
                                **Código Python:**
                                ```python
                                [código pandas para responder la pregunta]
                                ```
                                
                                **Conclusión:**
                                [Resumen ejecutivo de 1-2 oraciones con el hallazgo principal]
                                
                                Sé directo, usa números concretos y responde en el mismo idioma que el usuario."""
                            },
                            {
                                "role": "user",
                                "content": f"Información del DataFrame:\n{resumen_df}\n\nPregunta: {pregunta}"
                            }
                        ] + [
                            {"role": m["role"], "content": m["content"]}
                            for m in st.session_state.messages[:-1]
                        ],
                        max_tokens=1000
                    )

                    respuesta_texto = respuesta.choices[0].message.content
                    st.markdown(respuesta_texto)

                    # Guardar en historial
                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": respuesta_texto
                    })

                except Exception as e:
                    st.error(f"Error: {str(e)}")

    # Botón para limpiar el chat
    if st.session_state.messages:
        if st.button("🗑️ Limpiar chat"):
            st.session_state.messages = []
            st.rerun()

else:
    # Pantalla de bienvenida
    st.info("👆 Subí un CSV para empezar")

    st.markdown("""
    ### 💡 Ejemplos de preguntas que podés hacer:
    - *¿Cuál es el promedio de ventas por región?*
    - *¿Cuáles son los 5 clientes con mayor riesgo?*
    - *¿Hay valores nulos en los datos?*
    - *¿Cuál es la correlación entre X e Y?*
    - *Resumí los datos en un párrafo ejecutivo*
    - *¿Qué mes tuvo más pérdidas?*
    
    ### 🛠️ Tech Stack
    `Python` · `OpenAI GPT-4o-mini` · `Pandas` · `Streamlit`
    """)

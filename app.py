#Nombre del proyecto: FlowConnect 
#Autor: Héctor Ayuso Martín



#FlowConnect fue elegido como nombre porque resalta la fluidez en la conexión entre backend y frontend.




import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt

# URL base de la API
api_url = "http://127.0.0.1:8000"

st.title("FlowConnect Visualización")

# Cargar usuarios
st.subheader("Usuarios")
try:
    usuarios_response = requests.get(f"{api_url}/usuarios")
    usuarios_response.raise_for_status()
    usuarios = usuarios_response.json()
    usuarios_df = pd.DataFrame(usuarios)
    st.dataframe(usuarios_df)
except requests.exceptions.RequestException as e:
    st.error(f"No se pudo cargar la lista de usuarios: {e}")

# Cargar transacciones
st.subheader("Transacciones")
try:
    transacciones_response = requests.get(f"{api_url}/transacciones")
    transacciones_response.raise_for_status()
    transacciones = transacciones_response.json()
    transacciones_df = pd.DataFrame(transacciones)
    st.dataframe(transacciones_df)
except requests.exceptions.RequestException as e:
    st.error(f"No se pudo cargar la lista de transacciones: {e}")

# Opciones de visualización
st.subheader("Opciones de Visualización")
if 'transacciones_df' in locals() and not transacciones_df.empty:
    # Seleccionar tipo de gráfico
    tipo_grafico = st.selectbox(
        "Selecciona el tipo de gráfico",
        ["Monto total por usuario", "Transacciones por fecha"]
    )

    if tipo_grafico == "Monto total por usuario":
        montos_por_usuario = transacciones_df.groupby("id_usuario")["monto"].sum()
        fig, ax = plt.subplots()
        montos_por_usuario.plot(kind="bar", ax=ax)
        ax.set_title("Monto total por usuario")
        ax.set_xlabel("ID de Usuario")
        ax.set_ylabel("Monto Total")
        st.pyplot(fig)

    elif tipo_grafico == "Transacciones por fecha":
        transacciones_por_fecha = transacciones_df.groupby("fecha")["monto"].sum()
        fig, ax = plt.subplots()
        transacciones_por_fecha.plot(kind="line", ax=ax, marker='o')
        ax.set_title("Transacciones por fecha")
        ax.set_xlabel("Fecha")
        ax.set_ylabel("Monto Total")
        st.pyplot(fig)
else:
    st.warning("No hay datos para graficar.")

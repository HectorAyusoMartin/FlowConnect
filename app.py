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


st.sidebar.title("Acerca de FlowConnect")
st.sidebar.info(
    """
    FlowConnect es un proyecto personal diseñado para aprender y demostrar habilidades en desarrollo backend y frontend.

    -Backend: Los datos son servidos desde una API creada con FastAPI.
    
    -Frontend: Las visualizaciones interactivas son generadas en tiempo real utilizando Streamlit.

    """
)

st.sidebar.markdown("---")  # Línea divisoria

st.sidebar.title("Sobre mí")
st.sidebar.info(
    """
    Nombre: Héctor Ayuso Martín  
    Desarrollador Junior en Python y Java.  
    Ubicación: Barcelona  

    Contacto:  
    
    -Email: hayusomartin@gmail.com  
    -GitHub: https://github.com/HectorAyusoMartin
    -LinkedIn: www.linkedin.com/in/hector-ayuso-martin
    """
)


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


st.subheader("Gráficos Interactivos con Filtros")

# Verifica que las transacciones estén disponibles
if 'transacciones_df' in locals() and not transacciones_df.empty:
    # Selección de usuario
    usuarios_unicos = transacciones_df["id_usuario"].unique()
    usuario_seleccionado = st.selectbox(
        "Selecciona un usuario para filtrar las transacciones",
        options=["Todos"] + list(usuarios_unicos)
    )

    # Selección de rango de fechas
    fechas_min = transacciones_df["fecha"].min()
    fechas_max = transacciones_df["fecha"].max()
    rango_fechas = st.date_input(
        "Selecciona el rango de fechas",
        value=[pd.to_datetime(fechas_min), pd.to_datetime(fechas_max)],
        min_value=pd.to_datetime(fechas_min),
        max_value=pd.to_datetime(fechas_max)
    )

    # Filtrar datos según usuario y rango de fechas
    datos_filtrados = transacciones_df.copy()
    if usuario_seleccionado != "Todos":
        datos_filtrados = datos_filtrados[datos_filtrados["id_usuario"] == usuario_seleccionado]
    datos_filtrados = datos_filtrados[
        (datos_filtrados["fecha"] >= rango_fechas[0].strftime("%Y-%m-%d")) &
        (datos_filtrados["fecha"] <= rango_fechas[1].strftime("%Y-%m-%d"))
    ]

    # Selección de tipo de gráfico
    grafico_seleccionado = st.selectbox(
        "Selecciona el gráfico que quieres visualizar",
        ["Monto total por usuario", "Número de transacciones por usuario", "Transacciones por fecha"]
    )

    # Generar gráficos según la selección
    if not datos_filtrados.empty:
        if grafico_seleccionado == "Monto total por usuario":
            montos_por_usuario = datos_filtrados.groupby("id_usuario")["monto"].sum()
            fig, ax = plt.subplots()
            montos_por_usuario.plot(kind="bar", ax=ax, color="skyblue")
            ax.set_title("Monto total por usuario")
            ax.set_xlabel("ID de Usuario")
            ax.set_ylabel("Monto Total (€)")
            st.pyplot(fig)

        elif grafico_seleccionado == "Número de transacciones por usuario":
            transacciones_por_usuario = datos_filtrados["id_usuario"].value_counts()
            fig, ax = plt.subplots()
            transacciones_por_usuario.plot(kind="bar", ax=ax, color="lightgreen")
            ax.set_title("Número de transacciones por usuario")
            ax.set_xlabel("ID de Usuario")
            ax.set_ylabel("Número de Transacciones")
            st.pyplot(fig)

        elif grafico_seleccionado == "Transacciones por fecha":
            transacciones_por_fecha = datos_filtrados.groupby("fecha")["monto"].sum()
            fig, ax = plt.subplots()
            transacciones_por_fecha.plot(kind="line", ax=ax, marker="o", color="coral")
            ax.set_title("Transacciones por fecha")
            ax.set_xlabel("Fecha")
            ax.set_ylabel("Monto Total (€)")
            st.pyplot(fig)
    else:
        st.warning("No hay datos para graficar con los filtros seleccionados.")
else:
    st.warning("No hay datos para graficar.")




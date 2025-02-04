import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")  # Expande el ancho de la página

# Cargar el archivo Excel
file_path = r"C:\Users\mateo\Downloads\ALERTAS EN WEB\ALERTAS 03-02-2025-2.xlsx"
df = pd.read_excel(file_path, sheet_name="DETALLE DE ACTUALIZACIÓN ")

# Título del dashboard
st.title("📊 Dashboard de Alertas")

# Filtros interactivos
asesores = st.multiselect("Filtrar por Asesor", df["ASESOR"].unique())
estados = st.multiselect("Filtrar por Estado", df["ESTADO EN HSA"].unique())

# Aplicar filtros
if asesores:
    df = df[df["ASESOR"].isin(asesores)]
if estados:
    df = df[df["ESTADO EN HSA"].isin(estados)]

# Función para aplicar colores a toda la fila
def highlight_row(row):
    estado = str(row["ESTADO DE ACTUALIZACIÓN"]).strip().upper()  # Convertir a texto y eliminar espacios
    
    if "AL DÍA" in estado:
        color = "background-color: green; color: white"  # 🟢 Verde
    elif "PENDIENTE" in estado or "PENDIENTE DE ACTUALIZAR" in estado:
        color = "background-color: yellow; color: black"  # 🟡 Amarillo
    elif estado == "NO ACTUALIZÓ":
        color = "background-color: red; color: white"  # 🔴 Rojo
    else:
        color = ""  # Sin color

    return [color] * len(row)  # Aplicar el color a toda la fila

# Mostrar tabla con mayor tamaño
st.dataframe(df.style.apply(highlight_row, axis=1), use_container_width=True)

# Gráfica de estados
st.bar_chart(df["ESTADO EN HSA"].value_counts())

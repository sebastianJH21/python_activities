import streamlit as st
import pandas as pd
import io


# Configuración de la página
st.set_page_config(   
    page_icon="📌",
    layout="wide"
)

st.title("Momento 2 - Actividad 2")

st.header("Descripción de la actividad")
st.markdown("""
Aprender a inspeccionar y resumir datos utilizando métodos básicos de Pandas como .head(), .tail(), .info(), .describe(), además de realizar filtrado básico de filas y columnas. También integraremos estas funcionalidades en una aplicación interactiva con Streamlit para visualizar estadísticas descriptivas.
""")

st.header("Objetivos de aprendizaje")

st.markdown("""
- Aplicar filtrado básico de datos en pandas, seleccionando columnas especficas.
- Inspeccionar y comprender la estructura de un DataFrame en pandas.
- Integrar estas herramientas en una aplicación interactiva con Streamlit.
""")

st.header("Solución")

df = pd.read_csv("static/datasets/estudiantes_colombia.csv")

st.markdown('<h4 margin-top: 0px;">Mostrar 5 primeras filas:</h3>', unsafe_allow_html=True)
code = """
    import streamlit as st
    import pandas as pd

    df = pd.read_csv("static/datasets/estudiantes_colombia.csv")

    st.dataframe(df.head())
"""
st.code(code)
st.dataframe(df.head())

st.markdown('<h4 margin-top: 0px;">Mostrar 5 últimas filas:</h3>', unsafe_allow_html=True)
code = """
    import streamlit as st
    import pandas as pd

    df = pd.read_csv("static/datasets/estudiantes_colombia.csv")

    st.dataframe(df.tail())
"""
st.code(code)
st.dataframe(df.tail())

st.markdown('<h4 margin-top: 0px;">Información del dataset:</h3>', unsafe_allow_html=True)
code = """
    import streamlit as st
    import pandas as pd
    import io

    df = pd.read_csv("static/datasets/estudiantes_colombia.csv")

    buffer = io.StringIO()
    df.info(buf=buffer)
    info_str = buffer.getvalue()

    st.text(info_str)
"""
st.code(code)
buffer = io.StringIO()
df.info(buf=buffer)
st.dataframe(df)

st.markdown('<h4 margin-top: 0px;">Descripción del dataset:</h3>', unsafe_allow_html=True)
code = """
    import streamlit as st
    import pandas as pd

    df = pd.read_csv("static/datasets/estudiantes_colombia.csv")

    st.dataframe(df.describe())
"""
st.code(code)
st.dataframe(df.describe())

st.markdown('<h4 margin-top: 0px;">Información por columnas especificas:</h3>', unsafe_allow_html=True)
code = """
    import streamlit as st
    import pandas as pd

    df = pd.read_csv("static/datasets/estudiantes_colombia.csv")

    st.dataframe(df[["nombre", "edad", "promedio"]])
"""
st.code(code)
st.dataframe(df[["nombre", "edad", "promedio"]])

st.markdown('<h4 margin-top: 0px;">Información por promedio de estudiantes:</h3>', unsafe_allow_html=True)
code = """
    import streamlit as st
    import pandas as pd

    df = pd.read_csv("static/datasets/estudiantes_colombia.csv")

    min_promedio = float(df["promedio"].min())
    max_promedio = float(df["promedio"].max())

    prom = st.slider(
        "Mostrar estudiantes con promedio mayor a:",
        min_value=min_promedio,
        max_value=max_promedio,
        value=min_promedio,
        step=0.1
    )

    df_filtrado = df[df["promedio"] > prom]

    st.write(f"Estudiantes con promedio mayor a {prom}:")
    st.dataframe(df_filtrado)
"""
st.code(code)
min_promedio = float(df["promedio"].min())
max_promedio = float(df["promedio"].max())

prom = st.slider(
    "Mostrar estudiantes con promedio mayor a:",
    min_value=min_promedio,
    max_value=max_promedio,
    value=min_promedio,
    step=0.1
)

df_filtrado = df[df["promedio"] > prom]

st.write(f"Estudiantes con promedio mayor a {prom}:")
st.dataframe(df_filtrado)
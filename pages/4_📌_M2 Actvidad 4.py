import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(   
    page_icon="📌",
    layout="wide"
)

st.title("Momento 2 - Actividad 4")

st.header("Descripción de la actividad")
st.markdown("""
Pandas es una biblioteca de Python ampliamente utilizada para el análisis de datos. Los métodos .loc y .iloc permiten acceder a filas y columnas de un DataFrame de manera precisa. La principal diferencia entre ellos radica en cómo seleccionan los datos:
""")

st.header("Objetivos de aprendizaje")

st.markdown("""
- Aprender de la utilización de .loc y .iloc con dataframe.
- Dominar .loc y .iloc por medio de filtros.
- Modificar campos de una base de datos.
""")

st.header("Solución")

data = {
    'Nombre': ['Ana', 'Luis', 'María', 'Carlos', 'Laura'],
    'Departamento': ['Ventas', 'IT', 'Recursos Humanos', 'IT', 'Ventas'],
    'Salario': [3500, 4500, 4000, 4800, 3600]
}


df = pd.DataFrame(data)

st.subheader("Datos a trabajar")

code = """
    data = {
        'Nombre': ['Ana', 'Luis', 'María', 'Carlos', 'Laura'],
        'Departamento': ['Ventas', 'IT', 'Recursos Humanos', 'IT', 'Ventas'],
        'Salario': [3500, 4500, 4000, 4800, 3600]
    }

    df = pd.DataFrame(data)
"""

st.code(code)

st.subheader("Filtrar por departamento encargado")

code = """
    import streamlit as st
    import  pandas as pd

    departamento = st.selectbox("Selecciona un departamento:", ['Seleccione el departamento', 'IT', 'Recursos Humanos', 'Ventas'])
    if (departamento == 'Seleccione el departamento'):
        filtrp_departamento = df
    else:
        filtrp_departamento = df.loc[df['Departamento'] == departamento]

    st.dataframe(filtrp_departamento)
"""

st.code(code)

departamento = st.selectbox("Selecciona un departamento:", ['Seleccione el departamento', 'IT', 'Recursos Humanos', 'Ventas'])
if (departamento == 'Seleccione el departamento'):
    filtrp_departamento = df
else:
    filtrp_departamento = df.loc[df['Departamento'] == departamento]

st.dataframe(filtrp_departamento)

st.subheader("Filtrar por salario")

code = """"
    import streamlit as st
    import  pandas as pd

    salario_min = st.slider("Salario:", min_value=3000, max_value=6000, step=100, value=3000)
    filtro_salario = df.loc[df['Salario'] >= salario_min]
    
    st.dataframe(filtro_salario)
"""

salario_min = st.slider("Salario:", min_value=3000, max_value=6000, step=100, value=3000)
filtro_salario = df.loc[df['Salario'] >= salario_min]
        
st.dataframe(filtro_salario)

st.subheader("Filtrar fila especifica")

code = """
    import streamlit as st
    import pandas as pd

    fila_idx = st.number_input(f"Índice de la fila (0 a {len(df) - 1}):", min_value=0, max_value=len(df) - 1, step=1)
    st.write(df.iloc[fila_idx])
"""

st.code(code)

fila_idx = st.number_input(f"Índice de la fila (0 a {len(df) - 1}):", min_value=0, max_value=len(df) - 1, step=1)
st.write(df.iloc[fila_idx])

st.subheader("Actualizar información especifica")

code = """
    import streamlit as st
    import pandas as pd

    id_mod = st.selectbox("ID del empleado:", df.index)
    col_mod = st.selectbox("Columna a actualizar:", df.columns)
    nuevo_valor = st.text_input("Nuevo valor:")

    if st.button("Actualizar"):
        if nuevo_valor == "":
            st.error('Los datos no pueden estar vacíos')
        else:
            if col_mod == 'Salario':
                df.loc[id_mod, col_mod] = float(nuevo_valor)
            else:
                df.loc[id_mod, col_mod] = nuevo_valor
            st.success(f"Se modificó {col_mod} del ID {id_mod} con éxito.")

    st.dataframe(df)
"""

st.code(code)

id_mod = st.selectbox("ID del empleado:", df.index)
col_mod = st.selectbox("Columna a actualizar:", df.columns)
nuevo_valor = st.text_input("Nuevo valor:")

if st.button("Actualizar"):
    if nuevo_valor == "":
        st.error('Los datos no pueden estar vacíos')
    else:
        if col_mod == 'Salario':
            df.loc[id_mod, col_mod] = float(nuevo_valor)
        else:
            df.loc[id_mod, col_mod] = nuevo_valor
        st.success(f"Se modificó {col_mod} del ID {id_mod} con éxito.")

st.dataframe(df)




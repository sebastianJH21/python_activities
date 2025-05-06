import streamlit as st
import pandas as pd
import sqlite3
import numpy as np
from pymongo import MongoClient

# Configuración de la página
st.set_page_config(   
    page_icon="📌",
    layout="wide"
)

st.title("Momento 2 - Actividad 1")

st.header("Descripción de la actividad")
st.markdown("""
Familiarizarse con la creación de DataFrames en Pandas y mostrarlos usando Streamlit.
""")

st.header("Objetivos de aprendizaje")

st.markdown("""
- Identificar diferentes fuentes de datos estructurados que pueden ser transformados en un DataFram.
- Comprender las ventajas y limitaciones de cada fuente de datos al trabajar con panda.
- Integrar datos provenientes de diferentes fuentes en un único DataFrame cuando sea necesari.
""")

st.header("Solución")

# Diccionario

code = """
    import streamlit as st
    import pandas as pd

    libros = {
        "Titulo": ["Cien años de soledad", "Piense y hágase rico", "Hábitos atómicos", "El Psicoanalista"],
        "Autor": ["Gabriel Garcia Marquez", "Napoleon Hill", "James Clear", "John Katzenbach"],
        "Año": [1967, 1937, 2018, 2002],
        "Genero": ["Novela", "Autoayuda", "Autoayuda", "Thriller" ]
    }

    df = pd.DataFrame(libros)

    st.dataframe(df)
"""

# st.markdown('<h4 margin-top: 0px;">DataFrame de libros</h4>', unsafe_allow_html=True)

st.markdown('<h4 margin-top: 0px;">Código:</h4>', unsafe_allow_html=True)

st.code(code, language="python")

libros = {
    "Titulo": ["Cien años de soledad", "Piense y hágase rico", "Hábitos atómicos", "El Psicoanalista"],
    "Autor": ["Gabriel Garcia Marquez", "Napoleon Hill", "James Clear", "John Katzenbach"],
    "Año": [1967, 1937, 2018, 2002],
    "Genero": ["Novela", "Autoayuda", "Autoayuda", "Thriller" ]
}

df = pd.DataFrame(libros)

# st.markdown('<h4 margin-top: 0px;">DataFrame de Libros:</h4>', unsafe_allow_html=True)
st.dataframe(df)


# Lista de diccionarios:

code = """
    import streamlit as st
    import pandas as pd

    ciudades = [{"Nombre": "Tokio", "Población": 37977000, "País": "Japón"},
         {"Nombre": "Shanghái", "Población": 24677000, "País": "China"},
         {"Nombre": "Yakarta", "Población": 34540000, "País": "Indonesia"}]

    df = pd.DataFrame(ciudades)

    st.dataframe(df)
"""

st.markdown('<h4 margin-top: 0px;">DataFrame desde una lista de diccionarios</h4>', unsafe_allow_html=True)

st.markdown('<h4 margin-top: 0px;">Código:</h4>', unsafe_allow_html=True)

st.code(code, language="python")

ciudades = [{"Nombre": "Tokio", "Población": 37977000, "País": "Japón"},
         {"Nombre": "Shanghái", "Población": 24677000, "País": "China"},
         {"Nombre": "Yakarta", "Población": 34540000, "País": "Indonesia"}]

df = pd.DataFrame(ciudades)


st.markdown('<h4 margin-top: 0px;">Información de ciudades:</h4>', unsafe_allow_html=True)
st.dataframe(df)


# Lista de listas:

code = """
    import streamlit as st
    import pandas as pd

    productos = [
    ["Televisor", 1300000, 5],
    ["Computador", 500000, 15], 
    ["Mouse", 20000, 50]
    ]

    df = pd.DataFrame( productos, columns=["Nombre", "Precio", "Cantidad"] )

    st.dataframe(df);
"""

st.markdown('<h4 margin-top: 0px;">DataFrame desde una Lista de Listas</h4>', unsafe_allow_html=True)

st.markdown('<h4 margin-top: 0px;">Código:</h4>', unsafe_allow_html=True)

st.code(code, language="python")

productos = [
  ["Televisor", 1300000, 5],
  ["Computador", 500000, 15], 
  ["Mouse", 20000, 50]
]

df = pd.DataFrame( productos, columns=["Nombre", "Precio", "Cantidad"] )

st.markdown('<h4 margin-top: 0px;">Productos en Inventario:</h4>', unsafe_allow_html=True)
st.dataframe(df);

# Series
code = """
    import streamlit as st
    import pandas as pd

    sNombres = pd.Series(["Juan", "Camilo", "Andrés", "Mariana"])
    sEdades = pd.Series([10, 27, 21, 21])
    sCiudaes = pd.Series(["Medellín", "Cali", "Bucaramanga", "Medellín"])

    datos = {
    "Nombre¨": sNombres,
    "Edades": sEdades,
    "Ciudades": sCiudaes
    }

    df = pd.DataFrame(datos)

    st.dataframe(df)
"""

st.markdown('<h4 margin-top: 0px;">DataFrame desde series</h4>', unsafe_allow_html=True)

st.markdown('<h4 margin-top: 0px;">Código:</h4>', unsafe_allow_html=True)

st.code(code, language="python")

sNombres = pd.Series(["Laura", "Santiago", "Valentina", "Mateo"])
sEdades = pd.Series([32, 45, 29, 38])
sCiudades = pd.Series(["Bogotá", "Cartagena", "Manizales", "Barranquilla"])

datos = {
  "Nombre¨": sNombres,
  "Edades": sEdades,
  "Ciudades": sCiudades
}

df = pd.DataFrame(datos)

st.markdown('<h4 margin-top: 0px;">Datos de personas:</h4>', unsafe_allow_html=True)
st.dataframe(df)

# Archivo CSV

code = """
    import streamlit as st
    import pandas as pd

    #Tomamos la ruta relativa del archivo a leer
    df = pd.read_csv("static/datasets/data.csv")

    st.dataframe(df)    
"""
st.markdown('<h4 margin-top: 0px;">DataFrame desde CSV</h4>', unsafe_allow_html=True)

st.markdown('<h4 margin-top: 0px;">Código:</h4>', unsafe_allow_html=True)

st.code(code, language="python")

#Tomamos la ruta relativa del archivo a leer
df = pd.read_csv("static/datasets/data.csv")

st.markdown('<h4 margin-top: 0px;">Datos desde CSV:</h4>', unsafe_allow_html=True)

st.dataframe(df)

# Archivo Excel

code = """
    import streamlit as st
    import pandas as pd

    #Tomamos la ruta relativa del archivo a leer
    df = pd.read_excel("static/datasets/data.xlsx")

    st.dataframe(df)    
"""

st.markdown('<h4 margin-top: 0px;">DataFrame desde excel</h4>', unsafe_allow_html=True)

st.markdown('<h4 margin-top: 0px;">Código:</h4>', unsafe_allow_html=True)

st.code(code, language="python")

#Tomamos la ruta relativa del archivo a leer
df = pd.read_excel("static/datasets/data.xlsx")

st.markdown('<h4 margin-top: 0px;">Datos desde excel:</h4>', unsafe_allow_html=True)
st.dataframe(df)


# JSON

ode = """
    import streamlit as st
    import pandas as pd

    #Tomamos la ruta relativa del archivo a leer
    df = pd.read_json("static/datasets/data.json")

    st.dataframe(df)    
"""

st.markdown('<h4 margin-top: 0px;">DataFrame desde JSON</h4>', unsafe_allow_html=True)

st.markdown('<h4 margin-top: 0px;">Código:</h4>', unsafe_allow_html=True)

st.code(code, language="python")

df = pd.read_json("static/datasets/data.json")

st.markdown('<h4 margin-top: 0px;">Datos de Usuarios desde JSON:</h4>', unsafe_allow_html=True)
st.dataframe(df)

# URL
code = """
    import streamlit as st
    import pandas as pd

    df = pd.read_csv("https://people.sc.fsu.edu/~jburkardt/data/csv/hw_200.csv")

    st.dataframe(df)
"""

st.markdown('<h4 margin-top: 0px;">DataFrame desde URL</h4>', unsafe_allow_html=True)

st.markdown('<h4 margin-top: 0px;">Código:</h4>', unsafe_allow_html=True)

st.code(code, language="python")

df = pd.read_csv("https://people.sc.fsu.edu/~jburkardt/data/csv/hw_200.csv")

st.markdown('<h4 margin-top: 0px;">Datos desde URL:</h4>', unsafe_allow_html=True)
st.dataframe(df)

# SQLITE
code = """
    import streamlit as st
    import pandas as pd
    import sqlite3

    data = {
        "Nombre": ["Carla", "Esteban", "Lucía", "Fernando"],
        "Edad": [6.5, 7.0, 5.8, 6.2]
    }
    df = pd.DataFrame(data)

    conn = sqlite3.connect("estudiantes.db")

    df.to_sql("estudiantes", conn, if_exists='replace', index=False)

    df_sql = pd.read_sql_query("SELECT * FROM estudiantes", conn)

    st.dataframe(df_sql)

    conn.close()
"""

st.markdown('<h4 margin-top: 0px;">DataFrame desde SQLite</h4>', unsafe_allow_html=True)

st.markdown('<h4 margin-top: 0px;">Código:</h4>', unsafe_allow_html=True)

st.code(code, language="python")

data = {"Nombre": ["Ana", "Luis", "Juan"], "Edad": [5.0, 4.3, 3.0]}
df = pd.DataFrame(data)

conn = sqlite3.connect("estudiantes.db")

df.to_sql("estudiantes", conn, if_exists='replace', index=False)

df_sql = pd.read_sql_query("SELECT * FROM estudiantes", conn)

st.markdown('<h4 margin-top: 0px;">Datos desde SQLite:</h4>', unsafe_allow_html=True)
st.dataframe(df_sql)

conn.close()

# NUMPY
code = """
    import streamlit as st
    import pandas as pd
    import numpy as np

    numeros = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])

    df = pd.DataFrame(numeros)

    st.dataframe(df)
"""

st.markdown('<h4 margin-top: 0px;">DataFrame desde Numpy</h4>', unsafe_allow_html=True)

st.markdown('<h4 margin-top: 0px;">Código:</h4>', unsafe_allow_html=True)

st.code(code, language="python")

numeros = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

df = pd.DataFrame(numeros)

st.markdown('<h4 margin-top: 0px;">Datos desde numPy:</h4>', unsafe_allow_html=True)
st.dataframe(df)

# FIREBASE
dbCode = """
    #Abrimos la shell de MongoDB e ingresamos el siguiente comando
    use Tecnoloiga

    #Creamos la colección con el siguiente comando
    db.usuarios.insertMany([
        { nombre: "Laura", ciudad: "Bogotá" },
        { nombre: "Andrés", ciudad: "Manizales" },
        { nombre: "Valeria", ciudad: "Cartagena" },
        { nombre: "Tomás", ciudad: "Pereira" }
    ])
"""

code = """
    import streamlit as st
    import pandas as pd
    from pymongo import MongoClient

    uri = "mongodb+srv://python:<IMtMS5M3Ia81SltN>@pythonactivities.9pcn5qh.mongodb.net/?retryWrites=true&w=majority&appName=pythonactivities"

    client = MongoClient(uri)

    db = client["python"]
    collection = db["activity_1"]

    df = pd.DataFrame(list(collection.find()))
    st.dataframe(df)
"""

st.markdown('<h4 margin-top: 0px;">DataFrame desde MongoDB</h4>', unsafe_allow_html=True)

st.markdown('<h4 margin-top: 0px;">Código MongoDB:</h4>', unsafe_allow_html=True)

st.code(dbCode)

st.markdown('<h4 margin-top: 0px;">Código:</h4>', unsafe_allow_html=True)

st.code(code, language="python")
uri = "mongodb+srv://python:IMtMS5M3Ia81SltN@pythonactivities.9pcn5qh.mongodb.net/?retryWrites=true&w=majority&appName=pythonactivities&ssl=false"


try:
    client = MongoClient(uri, serverSelectionTimeoutMS=5000)
    client.server_info()  # fuerza conexión
    st.success("✅ Conectado a MongoDB")
except Exception as e:
    st.error(f"❌ No se pudo conectar: {e}")

client = MongoClient(uri)
db = client["python"]
collection = db["activity_1"]

df = pd.DataFrame(list(collection.find()))

st.dataframe(df)
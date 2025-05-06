import streamlit as st
import pandas as pd
from datetime import datetime
from faker import Faker
import random
import numpy as np

# Configuración de la página
st.set_page_config(   
    page_icon="📌",
    layout="wide"
)

st.title("Momento 2 - Actividad 3")

st.header("Descripción de la actividad")
st.markdown("""
Brindar una comprensión profunda y práctica sobre las diversas técnicas de filtrado en Pandas, sin utilizar los métodos loc ni iloc. A través de ejemplos claros basados en un DataFrame con datos representativos de Colombia, aprenderás a utilizar operadores de comparación, operadores lógicos, y métodos como query(), isin(), where(), mask() y otros. Al finalizar, estarás en capacidad de aplicar estos conocimientos para seleccionar y manipular subconjuntos de datos de manera eficiente.
""")

st.header("Objetivos de aprendizaje")

st.markdown("""
- Aprender sobre las diversas técnicas de filtrado en Pandas.
- Aprender sobre los operadores de compararción,operadores lógicos.
- Aprender sobre los métodos com query(), isin(), where(), mask(), between(), isnull(), notnull() y str() y fechas.
""")

st.header("Solución")

st.markdown('<h4 margin-top: 0px;">Link de Google Colab:</h3>', unsafe_allow_html=True)
st.write('https://colab.research.google.com/drive/11aflsBT7MKFHwH-W839on3dA_eyy1pLD#scrollTo=PGatlGDmct5r')

fake = Faker('es_CO')

np.random.seed(123)
random.seed(123)
fake.seed_instance(123)

n = 50
data = {
    'id': range(1, n + 1),
    'nombre_completo': [fake.name() for _ in range(n)],
    'edad': np.random.randint(15, 76, n),
    'region': random.choices(
        ['Caribe', 'Andina', 'Pacífica', 'Orinoquía', 'Amazonía'],
        weights=[0.3, 0.4, 0.15, 0.1, 0.05],
        k=n
    ),
    'municipio': random.choices(
        [
            'Barranquilla', 'Santa Marta', 'Cartagena',  # Caribe
            'Bogotá', 'Medellín', 'Tunja', 'Manizales',  # Andina
            'Cali', 'Quibdó', 'Buenaventura',           # Pacífica
            'Villavicencio', 'Yopal',                    # Orinoquía
            'Leticia', 'Puerto Inírida'                  # Amazonía
        ],
        k=n
    ),
    'ingreso_mensual': np.random.randint(800000, 12000001, n),
    'ocupacion': random.choices(
        [
            'Estudiante', 'Docente', 'Comerciante', 'Agricultor',
            'Ingeniero', 'Médico', 'Desempleado', 'Pensionado',
            'Emprendedor', 'Obrero'
        ],
        k=n
    ),
    'tipo_vivienda': random.choices(
        ['Propia', 'Arrendada', 'Familiar'],
        k=n
    ),
    'fecha_nacimiento': [
        fake.date_of_birth(minimum_age=15, maximum_age=75) for _ in range(n)
    ],
    'acceso_internet': random.choices([True, False], weights=[0.7, 0.3], k=n)
}

# Crear DataFrame
df_nuevo = pd.DataFrame(data)

# Introducir algunos valores nulos
df_nuevo.loc[3:5, 'ingreso_mensual'] = np.nan
df_nuevo.loc[15:17, 'ocupacion'] = np.nan

# Convertir fecha_nacimiento a datetime
df_nuevo['fecha_nacimiento'] = pd.to_datetime(df_nuevo['fecha_nacimiento'])

df_filtrado = df_nuevo.copy()

if st.sidebar.checkbox("Filtrar por rango de edad"):
    min_edad, max_edad = st.sidebar.slider("Selecciona el rango de edad", 15, 75, (15, 75 ))
    df_filtrado = df_filtrado[df_filtrado['edad'].between(min_edad, max_edad)]

if st.sidebar.checkbox("Filtrar por municipios"):
    municipios = ['Barranquilla', 'Santa Marta', 'Cartagena', 'Bogotá', 'Medellín', 'Tunja',
                  'Manizales', 'Cali', 'Quibdó', 'Buenaventura', 'Villavicencio', 'Yopal',
                  'Leticia', 'Puerto Inírida']
    seleccionados = st.sidebar.multiselect("Selecciona municipios", municipios)
    if seleccionados:
        df_filtrado = df_filtrado[df_filtrado['municipio'].isin(seleccionados)]


if st.sidebar.checkbox("Filtrar por ingreso mensual mínimo"):
    ingreso_minimo = st.sidebar.slider("Ingreso mínimo (COP)", 800000, 12000000, 800000, step=100000)
    df_filtrado = df_filtrado[df_filtrado['ingreso_mensual'] > ingreso_minimo]

if st.sidebar.checkbox("Filtrar por ocupación"):
    ocupaciones = ['Estudiante', 'Docente', 'Comerciante', 'Agricultor', 'Ingeniero', 'Médico',
                   'Desempleado', 'Pensionado', 'Emprendedor', 'Obrero']
    seleccion_ocupaciones = st.sidebar.multiselect("Selecciona ocupaciones", ocupaciones)
    if seleccion_ocupaciones:
        df_filtrado = df_filtrado[df_filtrado['ocupacion'].isin(seleccion_ocupaciones)]

if st.sidebar.checkbox("Filtrar personas sin vivienda propia"):
    df_filtrado = df_filtrado[~(df_filtrado['tipo_vivienda'] == 'Propia')]

if st.sidebar.checkbox("Filtrar por nombre"):
    texto = st.sidebar.text_input("Nombre contiene...")
    if texto:
        df_filtrado = df_filtrado[df_filtrado['nombre_completo'].str.contains(texto, case=False, na=False)]

if st.sidebar.checkbox(" Filtrar por año de nacimiento"):
    años = list(range(1949, 2010)) 
    año_seleccionado = st.sidebar.selectbox("Selecciona un año", años)
    df_filtrado = df_filtrado[df_filtrado['fecha_nacimiento'].dt.year == año_seleccionado]

if st.sidebar.checkbox("Filtrar por acceso a internet"):
    acceso = st.sidebar.radio("¿Tiene acceso a internet?", ["Sí", "No"])
    if acceso == "Sí":
        df_filtrado = df_filtrado[df_filtrado['acceso_internet'] == True]
    else:
        df_filtrado = df_filtrado[df_filtrado['acceso_internet'] == False]

if st.sidebar.checkbox("Filtrar por ingresos nulos"):
    df_filtrado = df_filtrado[df_filtrado['ingreso_mensual'].isnull()]

if st.sidebar.checkbox("Filtrar por rango de fechas de nacimiento"):
    fecha_inicio = st.sidebar.date_input("Fecha de inicio", datetime(1949, 1, 1), min_value=datetime(1949, 1, 1), max_value=datetime(2009, 12, 31))
    fecha_fin = st.sidebar.date_input("Fecha final", datetime(2009, 12, 31), min_value=datetime(1949, 1, 1), max_value=datetime(2009, 12, 31))
    fecha_inicio = pd.to_datetime(fecha_inicio)
    fecha_fin = pd.to_datetime(fecha_fin)
    if fecha_inicio <= fecha_fin:
        df_filtrado = df_filtrado[df_filtrado['fecha_nacimiento'].between(fecha_inicio, fecha_fin)]
    else:
        st.text("La fecha de inicio debe ser menor o igual a la fecha final.")

# Mostrar resultados
st.subheader("Resultado de filtrado:")
st.dataframe(df_filtrado)

# app_streamlit/app.py

import streamlit as st
import pandas as pd
import joblib  # para cargar el modelo

# 1. Cargar modelo entrenado
model = joblib.load("models/random_forest_model.pkl") 

# 2. Título
st.title("✈️ Predicción de precio de vuelos")

# 3. Formulario de entrada del usuario
airline = st.selectbox("Aerolínea", ['SpiceJet', 'Indigo', 'Vistara', 'Air_India', 'GO_FIRST', 'AirAsia'])
source_city = st.selectbox("Ciudad origen", ['Delhi', 'Mumbai', 'Bangalore', 'Kolkata', 'Chennai', 'Hyderabad'])
destination_city = st.selectbox("Ciudad destino", ['Delhi', 'Mumbai', 'Bangalore', 'Kolkata', 'Chennai', 'Hyderabad'])
departure_hour = st.slider("Hora de salida", 0, 23, 10)
days_left = st.slider("Días de antelación", 1, 60, 30)
stops = st.radio("Número de escalas", [0, 1, 2])
duration_mins = st.slider("Duración (minutos)", 30, 1500, 120)
class_type = st.radio("Clase del vuelo", ["Economy", "Business"])

# 4. Procesamiento de entrada
data_dict = {
    'airline': [airline],
    'source_city': [source_city],
    'destination_city': [destination_city],
    'departure_hour': [departure_hour],
    'days_left': [days_left],
    'stops': [stops],
    'duration_mins': [duration_mins],
    'class_Economy': [1 if class_type == "Economy" else 0]
}

input_df = pd.DataFrame(data_dict)

# 5. Predicción
if st.button("Predecir precio"):
    prediction = model.predict(input_df)[0]
    st.success(f"💸 El precio estimado del vuelo es: **{prediction:.2f} €**")



# src/data_processing.py

import os
import pandas as pd
import numpy as np

path_raw = "data/raw/Clean_Dataset.csv"


#  1. Cargar datos
def load_data(path_raw):
    return pd.read_csv(path_raw)

#  2. Limpiar datos (si hace falta)
def clean_data(df):
    # Eliminar columnas innecesarias (ejemplo)
    if 'Unnamed: 0' in df.columns:
        df = df.drop(columns=['Unnamed: 0'])
    return df

#  3. Feature Engineering
def feature_engineering(df):
    # Conversión de moneda 
    if 'price_eur' not in df.columns:
        exchange_rate = 0.009896
        df['price_eur'] = (df['price'] * exchange_rate).round(2)

    # Conversión de duración a minutos
    df['duration_mins'] = (df['duration'] * 60).astype(int)

    # Agrupar días de antelación
    df['days_left_group'] = pd.cut(
        df['days_left'],
        bins=[-1, 10, 20, 40, 1000],
        labels=["0-10 días", "11-20 días", "21-40 días", "40+ días"]
    )

    return df

#  4. Guardar dataset procesado
def save_processed_data(df, path_processed):
    os.makedirs(os.path.dirname(path_processed), exist_ok=True)
    df.to_csv(path_processed, index=False)

#  5. Función principal
def main():
    path_raw = "data/raw/Clean_Dataset.csv"
    path_processed = "data/processed/dataset_clean.csv"

    df = load_data(path_raw)
    df = clean_data(df)
    df = feature_engineering(df)
    save_processed_data(df, path_processed)

    print(f" Datos procesados guardados en: {path_processed}")


if __name__ == "__main__":
    main()

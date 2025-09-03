# src/evaluation.py

import pandas as pd
import joblib
import numpy as np

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Función para cargar el modelo
def load_model(path):
    return joblib.load(path)

# Función para cargar los datos de test
def load_test_data(path):
    return pd.read_csv(path)

# Función de evaluación
def evaluate_model():
    # Cargar modelo y test
    model = load_model("models/final_model.pkl")
    df_test = load_test_data("data/test/test.csv")

    # Separar X e y
    X_test = df_test.drop(columns=["price_eur"])
    y_test = df_test["price_eur"]

    # Predicción
    y_pred = model.predict(X_test)

    # Métricas
    mae = mean_absolute_error(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    r2 = r2_score(y_test, y_pred)

    # Resultados
    print(" Resultados de la Evaluación del Modelo Final")
    print(f" MAE:  {mae:.2f} €")
    print(f" RMSE: {rmse:.2f} €")
    print(f" R²:   {r2:.4f}")

if __name__ == "__main__":
    evaluate_model()

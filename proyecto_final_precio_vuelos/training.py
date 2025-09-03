# src/training.py

import pandas as pd
import os
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from sklearn.model_selection import GridSearchCV

def load_data(path):
    return pd.read_csv(path)

def save_dataset(df, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df.to_csv(path, index=False)

def save_model(model, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    joblib.dump(model, path)

def train_model():
    df = load_data("data/processed/dataset_clean.csv")

    # Separar variables
    X = df.drop(columns=["price_eur"])
    y = df["price_eur"]

    # Separar numéricas y categóricas
    num_features = X.select_dtypes(include=["int64", "float64"]).columns.tolist()
    cat_features = X.select_dtypes(include=["object", "category"]).columns.tolist()

    # Dividir en train/test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Pipeline
    preprocessor = ColumnTransformer(transformers=[
        ("num", StandardScaler(), num_features),
        ("cat", OneHotEncoder(handle_unknown="ignore"), cat_features)
    ])

    pipeline = Pipeline([
        ("preprocessor", preprocessor),
        ("model", RandomForestRegressor(random_state=42))
    ])

    # Hiperparámetros
    param_grid = {
        "model__n_estimators": [100, 200],
        "model__max_depth": [None, 10],
    }

    grid = GridSearchCV(pipeline, param_grid, cv=3, scoring="neg_mean_absolute_error", n_jobs=-1)
    grid.fit(X_train, y_train)

    # Guardar modelo y datasets
    save_model(grid.best_estimator_, "models/final_model.pkl")
    save_dataset(X_train.assign(price_eur=y_train), "data/train/train.csv")
    save_dataset(X_test.assign(price_eur=y_test), "data/test/test.csv")

    print(" Entrenamiento completo. Modelo guardado como final_model.pkl")

if __name__ == "__main__":
    train_model()

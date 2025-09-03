# Proyecto de Predicción de Precios de Vuelos

## 1. Objetivo
Predecir el precio en euros de un billete de avión nacional en India, a partir de variables como la aerolínea, clase, ciudades de origen/destino, número de escalas, etc.

## 2. Dataset
- Fuente: Kaggle
- Registros: 300.000+
- Variables: 11 originales → 13 finales
- Target: `price_eur`

## 3. Proceso de desarrollo

### 3.1 Limpieza de datos
- Eliminación de columnas irrelevantes
- Conversión de moneda
- Tratamiento de nulos

### 3.2 Feature Engineering
- Conversión de duración a minutos
- Extracción de hora de salida
- Codificación de variables categóricas
- Agrupación de días de antelación

### 3.3 Modelado
Se probaron 5 modelos supervisados:
- Random Forest (modelo final)
- CatBoost
- XGBoost
- Gradient Boosting
- Lasso

Y 2 no supervisados:
- PCA (reducción de dimensiones)
- KMeans (segmentación de vuelos)

### 3.4 Evaluación
- MAE: 16.53 €
- RMSE: 34.17 €
- R²: 0.9770 (Random Forest)

### 3.5 Despliegue
- App desarrollada en Streamlit
- Predicción en tiempo real con inputs del usuario

## 4. Conclusiones
- Random Forest fue el modelo con mejor balance entre rendimiento y eficiencia.
- El modelo permite prever precios con gran precisión.
- Ideal para integrarse en plataformas de venta de billetes.

## 5. Futuro
- Introducir rutas internacionales
- Añadir clima, temporada, eventos
- Incorporar precios históricos
#  Presentación Técnica – Data Science

---

##  Objetivo del Proyecto

El objetivo de este proyecto es predecir el precio de vuelos nacionales en India utilizando técnicas de Machine Learning.  
Este sistema permitiría a empresas o plataformas de comparación ofrecer precios estimados y optimizar sus estrategias de precios.

---

##  Adquisición y Preprocesado de Datos

- **Fuente**: Kaggle – "Flight Fare Prediction"
- +300.000 registros y 11 columnas
- Limpieza realizada:
  - Conversión de duración a minutos
  - Extracción de hora de salida
  - Conversión de moneda (INR → EUR)
  - Eliminación de columnas no útiles
  - Codificación de variables categóricas
  - Agrupación de días de antelación

---

## Análisis Exploratorio (EDA)

- Se exploraron relaciones entre `days_left`, `class`, `duration` y `price_eur`.
- Los vuelos con mayor antelación tienden a tener menor precio.
- La clase Business multiplica el precio respecto a Economy.
- Algunas aerolíneas tienen consistentemente precios más altos.

---

##  Preparación para Modelado

- División en `X` e `y` (`price_eur` como variable objetivo).
- División en `train` y `test` (80/20).
- Codificación con:
  - `OneHotEncoder` (en varios modelos)
  - `CatBoostEncoder` (para CatBoost)
- Escalado y pipelines implementados para garantizar reproducibilidad.

---

##  Modelos Supervisados Probados

- Regresor de Árbol de Decisión
- Random Forest Regressor ✅ (modelo final)
- Gradient Boosting Regressor
- XGBoost Regressor
- CatBoost Regressor

 Todos evaluados con **GridSearchCV** e hiperparámetros optimizados.

---

##  Métricas y Resultados

**Modelo final: Random Forest Regressor**
- R²: 0.9770
- MAE: 16.53 €
- RMSE: 34.17 €

Otros modelos obtuvieron también buenos resultados (CatBoost, XGBoost), pero Random Forest presentó mejor equilibrio entre precisión y estabilidad.

---

##  Modelos No Supervisados

- **KMeans** → agrupación en 4 clusters basada en precio, clase, duración, antelación.
- **DBSCAN** → detección de vuelos atípicos o extremadamente caros/baratos.

Esto permitió entender mejor segmentos de usuarios o tipos de vuelos.

---

##  Modelo Final y Guardado

El modelo final (`RandomForestRegressor`) fue entrenado, validado y guardado como `final_model.pkl` para uso en la aplicación.

---

##  App en Streamlit

- Se creó una aplicación web con Streamlit para que cualquier usuario pueda predecir el precio de un vuelo introduciendo variables clave.
- Uso del modelo guardado
- App completamente funcional y ejecutable desde terminal

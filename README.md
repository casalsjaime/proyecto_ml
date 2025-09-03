

##  Objetivo del Proyecto

> Predecir el precio de un billete de avión nacional (India), facilitando la toma de decisiones para empresas que reserven vuelos frecuentes para sus empleados.

---

##  Dataset

- **Fuente**: Kaggle
- **Registros**: +300.000
- **Variables**:
  - `airline`, `source_city`, `destination_city`, `stops`, `class`, `duration`, `days_left`, `price`

---

##  Preprocesamiento y Feature Engineering

- Conversión de duración a minutos (`duration_mins`)
- Conversión de `departure_time` a hora numérica (`departure_hour`)
- Agrupación de antelación en categorías (`days_left_group`)
- Codificación de clase (`class_Economy`)
- One-hot encoding para variables categóricas
- Clustering no supervisado con KMeans y DBSCAN

---

##  Análisis Exploratorio (EDA)

- Relación entre precio y antelación
- Comparativas por clase, escalas y aerolínea
- Distribución de precios según duración del vuelo
- Insights aplicables a empresas (ej. política de reservas anticipadas)

---

##  Modelado

### Modelos Supervisados Aplicados:

| Modelo              | Métrica R² | MAE (€) | RMSE (€) |
|---------------------|-----------:|--------:|---------:|
| Random Forest       | **0.977**  | 16.5    | 34.2     |
| CatBoost            | 0.9657     | 23.7    | 41.6     |
| Gradient Boosting   | 0.9656     | 24.1    | 41.7     |
| Decision Tree       | 0.919      | 39.8    | 64.9     |
| XGBoost             | 0.9733     | 18.9    | 35.5     |

>  Hiperparámetros optimizados con `GridSearchCV`

---

### Modelos No Supervisados:

- **KMeans** (`n_clusters=4`)
- **DBSCAN** (detección de clústeres densos)

> Las etiquetas de cluster se utilizaron como nuevas features en modelos supervisados.

---

## 🖥 Despliegue en Streamlit

La app fue desarrollada con `Streamlit` y permite al usuario predecir el precio introduciendo los datos del vuelo.

```bash
cd app_streamlit
streamlit run app.py

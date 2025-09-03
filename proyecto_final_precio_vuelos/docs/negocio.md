#  Presentación Ejecutiva – Negocio

---

##  ¿Qué problema resolvemos?

Actualmente los usuarios no saben si el precio de un billete es razonable o caro.  
Este proyecto permite predecir el precio estimado de un vuelo en base a variables conocidas: antelación, duración, aerolínea, clase, etc.

---

##  Objetivo del Proyecto

Crear un sistema inteligente capaz de **predecir el precio de un vuelo** con alta precisión para ayudar tanto a consumidores como a plataformas de viaje.

---

##  Datos utilizados

- Dataset de Kaggle: +300.000 registros reales de vuelos
- Variables clave: aerolínea, origen, destino, clase, duración, días de antelación
- Transformados y preparados para uso en modelos predictivos

---

##  Principales Resultados

- Predicciones con un **error medio de solo 16.5 €**
- Precisión del modelo: **R² = 0.977**
- El modelo entiende la lógica de precios: más antelación = mejor precio

---

##  Aplicación Web

Creamos una aplicación visual e intuitiva donde el usuario puede:
- Introducir datos de su vuelo
- Obtener precio estimado en segundos
- Visualizar cómo cambian los precios según variables clave

---

##  Impacto en el negocio

- Mejora la toma de decisiones para usuarios y agencias
- Permite diseñar campañas segmentadas (clustering)
- Reducción de errores en estimación

---

##  Futuras mejoras

- Incluir más datos temporales (día de la semana, temporada alta)
- Añadir datos de vuelos internacionales
- Modelo en producción con API o integración web

---
title: "Sobre el libro: qué aprendemos, con qué herramientas y para quién"
---

## Para quién

Para ingenieros y técnicos que han trabajado en campo y quieren trabajar con datos espaciales como se hace hoy en las empresas. Para topógrafos, técnicos forestales, profesionales del sector eléctrico y especialistas en SIG: gente que conoce bien su terreno, pero que nunca ha estudiado estadística, o la tiene olvidada, y no programa.

No hace falta saber nada de antemano. Python se explica desde cero en el primer libro de la serie, *PyQGIS from Scratch*. Aquí nos limitamos a usarlo, y explicamos cada línea nueva.

## Qué aprendemos

Recorremos el camino completo, desde la primera tabla hasta un modelo de riesgo, sobre un proyecto real.

- **Los datos y cómo mirarlos.** Abrir cualquier tabla, revisarla, entender los tipos de datos, hacer el gráfico adecuado y el primer mapa. Describir el centro y la dispersión, también de forma que un solo valor atípico no nos estropee el resultado.
- **Modelos.** Cómo depende una magnitud de otra; cómo predecir un «sí o no».
- **Probabilidad.** Con simulaciones en el ordenador, no con fórmulas. Las distribuciones que describen el número de sucesos, el viento y el error de medida.
- **Cuándo podemos fiarnos de un resultado.** Pruebas de permutación, bootstrap e intervalo de confianza, errores de decisión y un umbral fijado antes de calcular.
- **Datos espaciales en Python.** Vectores, ráster, sistemas de coordenadas y variables a lo largo de una línea.
- **Superficies.** Variograma, interpolación, krigeado y validación de la interpolación.
- **Áreas.** Vecinos, autocorrelación espacial y puntos calientes.
- **Eventos.** Si los puntos están repartidos al azar o se agrupan, y por qué en unos sitios hay más que en otros.
- **Aprendizaje automático con datos geográficos.** Variables, árboles de decisión y métodos de conjunto. Y, sobre todo, una validación honesta del modelo en un lugar nuevo.
- **Las tareas del proyecto Pajares.** El error de la diferencia entre dos levantamientos y el cambio mínimo detectable, la incertidumbre de la tasa de crecimiento, los temporales poco frecuentes, la revisión de etiquetas automáticas, qué parte de las interrupciones de suministro se deben a los árboles, y el modelo de riesgo con su validación frente a eventos reales.

## Con qué herramientas

Solo con lo que se usa hoy:

- Python en el editor VS Code, con un entorno conda;
- pandas para las tablas; seaborn y matplotlib para los gráficos;
- geopandas, rasterio y rioxarray para vectores y ráster;
- NumPy y SciPy para simulaciones y distribuciones; statsmodels para regresión y contraste de hipótesis;
- scikit-learn para aprendizaje automático y validación de modelos;
- PySAL para vecindad, autocorrelación espacial y procesos de puntos;
- scikit-gstat y GSTools para variograma y krigeado.

Todo el código se puede copiar y ejecutar. Los datos son abiertos: lidar y modelos digitales del terreno del IGN, incendios de NASA FIRMS, OpenStreetMap e indicadores de calidad del suministro eléctrico del MITECO.

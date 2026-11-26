---
title: "Sobre el libro"
---

## Para quién es este libro

Para ingenieros que han pasado muchos años trabajando en campo con el instrumento. Sabemos cartografía, trabajamos en QGIS, sabemos tomar puntos y comprobar un levantamiento. Pero estadística, casi ninguno de nosotros la ha estudiado a fondo. Y las herramientas con las que hoy se calcula en las empresas tampoco las conocemos.

Justo ahí empieza el libro. No hace falta saber nada de antemano.

## Qué enseña este libro

Cada libro de la serie tiene una tarea. La de este es **la estadística espacial con Python, desde cero.**

Primero, veamos qué es eso.

**La estadística** nos ayuda a entender qué dicen los números y si podemos fiarnos de ellos. Por ejemplo, qué altura de un apoyo es normal y cuál es rara. O si el bosque ha empezado a crecer más deprisa, o solo nos lo parece porque el levantamiento no es preciso.

**La estadística espacial** añade algo que cualquier ingeniero de campo sabe por experiencia: lo que está cerca se parece. Las laderas vecinas las barre el mismo viento, los árboles vecinos tienen la misma edad. Las fórmulas habituales de la estadística no lo saben. Para ellas, cada medida va por separado y no tiene relación con nada. Por eso, sobre un mapa, dan una respuesta demasiado segura. Vamos a aprender a tenerlo en cuenta.

Los demás libros de la serie toman la estadística de aquí. Por ejemplo, el libro sobre lidar calcula a qué ritmo crece el bosque, y si podemos fiarnos de ese ritmo lo explica una lección de este libro.

## Qué no enseña este libro

Dejemos claras tres cosas desde el principio.

1. **Aquí no enseñamos Python desde cero.** El lenguaje en sí lo explica el primer libro de la serie, *PyQGIS desde cero*. Aquí lo usamos. Cada línea de código nueva la explicamos con palabras: qué hace y para qué.
2. **Tampoco enseñamos toda la estadística del mundo.** Nos quedamos con las bases que necesita el proyecto, y las aprendemos bien.
3. **No es un manual de ejercicios de programación.** El código se puede copiar y ejecutar, pero el libro también se puede leer sin más. Lo importante es entender qué hacemos, para qué y cómo comprobamos que no nos hemos equivocado.

## Cómo trabajamos

El libro lo escribe un ingeniero como tú, que también está aprendiendo ahora. No tenemos respuestas preparadas. Avanzamos por el proyecto paso a paso, y cada lección es un paso.

En cada lección, todo va en el mismo orden:

1. Primero nos hacemos una pregunta.
2. Luego anotamos lo que creemos que vamos a ver. Lo anotamos **antes de calcular.**
3. Después calculamos.
4. Y comparamos el resultado con lo que esperábamos.

Si la hipótesis no se confirma, eso también es un resultado. Buscamos el porqué. Los errores con los que hemos tropezado también se quedan en la lección: son los que más enseñan.

## Nuestro proyecto

Pajares es un puerto de montaña entre Asturias y León. Aquí, en una misma ladera, coinciden el bosque, la nieve húmeda, el viento fuerte y las líneas eléctricas de 400 kV. En invierno, los árboles caen sobre los conductores y cortan las carreteras por las que las brigadas van a reparar la avería.

Todo el proyecto responde a una sola pregunta: **¿dónde caerá el bosque sobre las líneas en un temporal, y de qué números podemos fiarnos?** Por qué la pregunta es precisamente esta lo cuenta el prólogo.

## Qué vamos a recorrer

El camino va de lo sencillo a lo complejo. Cada parte se apoya en la anterior.

1. **Miramos los datos.** Abrimos una tabla, comprobamos qué hay en ella, hacemos los primeros gráficos y el primer mapa.
2. **Describimos los números.** Qué valor es el normal, cuánta dispersión hay, qué hacemos con los valores raros.
3. **Buscamos relaciones.** Cómo depende una magnitud de otra, por ejemplo la altura de un árbol del grosor de su tronco.
4. **Entendemos la probabilidad.** Con experimentos en el ordenador, no con fórmulas complicadas.
5. **Comprobamos si podemos fiarnos de un número.** ¿Puede ser casualidad? ¿Hasta qué punto estamos seguros del resultado?
6. **Trabajamos con mapas en Python.** Puntos, líneas, ráster, sistemas de coordenadas.
7. **Superficies.** Cómo estimar el valor entre los puntos de medida y hasta qué punto estamos seguros de esa estimación.
8. **Áreas.** Si los municipios vecinos se parecen entre sí.
9. **Eventos.** Si los incendios están repartidos al azar o se agrupan, y por qué.
10. **Aprendizaje automático.** Y, sobre todo, cómo validar con honestidad un modelo en un lugar que no ha visto nunca.
11. **Las tareas del proyecto.** Aquí todo lo que hemos aprendido se pone a trabajar en las preguntas reales de Pajares.

## Herramientas

Solo lo que se usa hoy en las empresas:

- **Python** en el editor **VS Code**. Las bibliotecas las instala el programa **conda**.
- **pandas**: tablas.
- **seaborn** y **matplotlib**: gráficos.
- **geopandas**: capas de puntos, líneas y polígonos, casi como en QGIS, pero en código.
- **rasterio**: ráster.
- **NumPy** y **SciPy**: cálculos y experimentos con números aleatorios.
- **statsmodels**: relaciones entre magnitudes y contraste de hipótesis.
- **scikit-learn**: aprendizaje automático.
- **PySAL**: los vecinos en el mapa y todo lo que tiene que ver con ellos.
- **scikit-gstat** y **GSTools**: superficies, es decir, cómo cambia un valor con la distancia y cómo estimarlo entre los puntos.

Cada herramienta la explicamos desde cero cuando la necesitamos por primera vez en el trabajo.

## Datos

Todos los datos son abiertos:

- el lidar y los modelos digitales del terreno del Instituto Geográfico Nacional (IGN);
- los puntos de incendio de los satélites de la NASA;
- OpenStreetMap;
- los indicadores de calidad del suministro eléctrico del ministerio;
- las llamadas al 112 Asturias.

En cada lección se indica de dónde salen los datos. También hay un recuadro «Tus datos»: qué cambiar para hacer lo mismo en tu propia zona.

## Cómo es una lección

Para que sea fácil orientarse en cualquier lección, el orden es siempre el mismo:

- **Dónde lo dejamos**: en pocas palabras, para no tener que volver atrás.
- **Qué queremos saber**: la pregunta y nuestra hipótesis.
- **Pasos**: cada paso, su código y la explicación línea a línea.
- **Qué ha salido**: el resultado frente a la hipótesis.
- **Si algo falla**: los errores reales y cómo encontramos la causa.
- **Tus datos.**
- **Resumen**: conceptos nuevos, código nuevo y lo esencial.
- **Preguntas para un ingeniero**: con las respuestas justo debajo.
- **Ejercicios**: tres cortos, de memoria, y uno de práctica: lo mismo con otros datos; las respuestas, en una página aparte al final del libro.
- **La pregunta que queda abierta.**
- **Notas y fuentes.**

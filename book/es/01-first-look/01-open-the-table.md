---
title: "Lección 1. Abrimos la tabla de apoyos"
---

(es-ch01-l01-lesson)=
## Dónde lo dejamos

El proyecto tiene una pregunta principal: dónde caerá el bosque sobre las líneas en un temporal y de qué números podemos fiarnos. Vamos a responderla paso a paso, y el primer paso son los datos. Empezamos por la tabla más sencilla y más importante: los apoyos de las líneas de 400 kV en el puerto de Pajares. Todo lo demás irá luego ligado a ellos: el bosque junto al apoyo, la pendiente de la ladera, la distancia al conductor.

## Cómo aborda un estadístico cualquier problema

Antes de abrir el archivo, conviene saber en qué punto del trabajo estamos. Los estadísticos describen cualquier trabajo con datos como un ciclo de cinco pasos. Por las iniciales de las palabras en inglés se llama PPDAC:

1. **Pregunta.** ¿Qué queremos saber?
2. **Plan.** ¿Qué datos necesitamos para eso y cómo vamos a comprobarlos?
3. **Datos.** Reunirlos, abrirlos y entender qué contienen.
4. **Análisis.** Tablas, gráficos, cálculos.
5. **Conclusión.** La respuesta a la pregunta, y lo que los datos no pueden decirnos.

El error más común al empezar es saltar directamente al cuarto paso y ponerse a calcular. Pero si no hemos entendido qué significa cada columna, cualquier cálculo puede acabar sin sentido. Recordemos la siderúrgica del prólogo que resultaba ser «el principal foco de incendios». Eso es justo un tercer paso que nos saltamos.

Hoy estamos en el tercer paso: abrimos la tabla y vemos qué hay en ella.

## Qué queremos saber

La pregunta de la lección es sencilla: qué hay en la tabla de apoyos y si podemos trabajar con ella.

Del corredor ya sabemos algunas cosas. Tiene cinco tramos de línea, los apoyos están en la montaña, y los apoyos de 400 kV suelen medir varias decenas de metros. Así que esperamos ver:

- unas tres decenas de filas, una por apoyo;
- coordenadas en metros;
- alturas de los apoyos de unos 25–40 m.

Si vemos algo muy distinto, por ejemplo un apoyo de 80 m o coordenadas vacías, hay un error en algún sitio o un caso especial, y tendremos que averiguar qué pasa.

## Datos

- **Tabla de apoyos** `powerline_reference_east400_towers.csv`: los 33 apoyos del corredor oriental de las líneas de 400 kV en el puerto de Pajares. La posición de los apoyos procede de OpenStreetMap y se revisó a mano con la ortofoto del PNOA y los datos lidar en octubre de 2026. Son datos derivados: © colaboradores de OpenStreetMap (ODbL); «PNOA cedido por © Instituto Geográfico Nacional».

:::{admonition} Tus datos
Sirve cualquier tabla en formato CSV en la que una fila sea un objeto: los apoyos de tu línea, sondeos, puntos de levantamiento. Solo hay que cambiar la ruta del archivo en el código de abajo.
:::

## Paso 1. Preparamos el puesto de trabajo

Trabajamos en VS Code con el entorno `field-to-code-statistics`. En él ya están instaladas todas las bibliotecas que vamos a necesitar.

1. Abrimos en VS Code la carpeta del proyecto: **File → Open Folder…** → `field-to-code-statistics`.
2. En la carpeta `code` creamos un archivo nuevo, `ch01_first_look.py`.
3. Elegimos el entorno: **Cmd+Shift+P** en Mac o **Ctrl+Shift+P** en Windows y Linux → **Python: Select Interpreter** → `field-to-code-statistics`.

Vamos a ejecutar el código a trozos, por celdas. Una celda empieza con la línea `# %%`. Encima, VS Code muestra el botón **Run Cell**. Lo pulsamos y el resultado aparece a la derecha, en la ventana **Interactive**. Así es cómodo mirar los datos paso a paso, en vez de ejecutar todo el archivo de golpe.

:::{admonition} Tus datos
Si todavía no tienes el entorno, se crea en unos minutos.

1. Instalamos conda, un programa que instala Python y las bibliotecas y las mantiene separadas para cada proyecto. Lo más sencillo es instalar Miniforge: https://conda-forge.org/download/
2. Creamos una sola carpeta para todo el proyecto, por ejemplo `my-project`, y dentro una carpeta `data` para los datos y otra `code` para los scripts. Guardamos todos los archivos del proyecto solo aquí; así las rutas del código no se rompen.
3. En el terminal (en Windows, en Miniforge Prompt) creamos el entorno con las bibliotecas necesarias y lo activamos:

   ```bash
   conda create -n my-project -c conda-forge python=3.12 pandas ipykernel
   conda activate my-project
   ```

   Para esta lección basta con pandas, e `ipykernel` hace falta para que VS Code pueda ejecutar las celdas. La lista completa de bibliotecas del libro está en el archivo `environment.yml` del repositorio del libro. Se instala todo de una vez con un solo comando: `conda env create -f environment.yml`.
4. En VS Code instalamos las extensiones **Python** y **Jupyter** de Microsoft (pestaña **Extensions**) y elegimos nuestro entorno con **Python: Select Interpreter**.
:::

## Paso 2. Cargamos pandas

Para trabajar con tablas en Python, casi todo el mundo usa la biblioteca pandas. Es el estándar en análisis de datos y en las empresas geoespaciales. Su pieza central es la tabla, que se llama DataFrame. Podemos imaginarla como una hoja de Excel que Python entiende: cada columna tiene un nombre y cada fila, un número.

```python
# %%
from pathlib import Path
import pandas as pd
```

- `from pathlib import Path` es una herramienta para trabajar con rutas de archivos. Con ella, la ruta se escribe igual en Mac, Windows y Linux.
- `import pandas as pd` carga pandas con el nombre corto `pd`. Es la abreviatura habitual; se usa en todas partes.

Si la celda se ejecuta sin mensajes, todo va bien: las bibliotecas se han encontrado.

## Paso 3. Abrimos la tabla

```python
# %%
data_dir = Path.home() / "geodata" / "pajares" / "outputs"
towers_file = data_dir / "powerline_reference_east400_towers.csv"
towers = pd.read_csv(towers_file)
```

Vamos línea a línea.

- `Path.home()` es nuestra carpeta personal. El signo `/` entre las partes las une en una ruta: carpeta personal → `geodata` → `pajares` → `outputs`. Así obtenemos la ruta a la carpeta de datos, y la llamamos `data_dir`.
- La segunda línea añade a la carpeta el nombre del archivo. Es la ruta completa a la tabla.
- `pd.read_csv(...)` lee el archivo CSV y lo convierte en una tabla de pandas. La guardamos con el nombre `towers`.

CSV es un formato de tabla en texto simple: cada línea del archivo es una fila de la tabla, y los valores van separados por comas. Lo abre cualquier programa, por eso los datos abiertos casi siempre se publican en CSV.

:::{admonition} Tus datos
Cambiamos la ruta en `data_dir` y el nombre del archivo en `towers_file`. Si los datos están en la carpeta `data` dentro de la carpeta del proyecto, la ruta es más corta: `data_dir = Path("data")`.
:::

## Paso 4. Cuántas filas y columnas

Lo primero que hace un ingeniero con una tabla nueva es comprobar su tamaño. Es como contar las cajas al recibir un envío.

```python
# %%
towers.shape
```

```text
(33, 28)
```

`shape` es el tamaño de la tabla: primero el número de filas y luego el de columnas. 33 filas y 28 columnas.

33 filas son exactamente los apoyos de nuestro corredor. Coincide con lo esperado: una fila, un apoyo. Es una comprobación importante. Si hubiera, por ejemplo, 66 filas, sospecharíamos que cada apoyo está registrado dos veces.

## Paso 5. Qué columnas hay

```python
# %%
towers.columns.tolist()
```

```text
['osm_node', 'label', 'old_seq', 'lines', 'x', 'y', 'lon', 'lat',
 'z_base_mdt02', 'z_base_dtm_cyl', 'dz_dtm_mdt02', 'height_ndsm_m',
 'lidar_x', 'lidar_y', 'dist_osm_lidar_m', 'lidar_note', 'bend_deg',
 'anchor_candidate', 'anchor_reason', 'rlat_zone', 'lidar_sheet',
 'surveys', 'slope_deg', 'dtm_interpolated', 'inside_corridor',
 'control_section', 'verified', 'screenshot']
```

`columns` son los nombres de todas las columnas, y `tolist()` los muestra como una lista simple.

Los nombres son cortos y en inglés. Es lo habitual: en el código no se usan espacios ni letras con tilde. Pero el nombre no siempre basta para saber qué hay en la columna. Por ejemplo, ¿qué es `dz_dtm_mdt02`? Por eso el siguiente paso es el diccionario de datos.

## Paso 6. El diccionario de datos

El diccionario de datos es la descripción de cada columna: qué significa, en qué unidades está y de dónde sale. Sin él no se puede calcular. Si tomamos una altura en metros por una en pies, o un ángulo en grados por un porcentaje, todas las conclusiones serán erróneas.

Para nuestra tabla hemos preparado el diccionario a partir de la descripción de la referencia de líneas que está en los documentos del proyecto:

**Cómo identificar el apoyo**
- `osm_node`: número del punto del apoyo en OpenStreetMap. Es fijo; con él siempre podemos encontrar el apoyo.
- `label`: nuestro nombre corto para el apoyo: N01…N10, A01…A05, etc. La letra indica el tramo de línea.
- `old_seq`: número de fila de la primera descarga de OpenStreetMap. Es interno; no hace falta para el análisis.
- `lines`: a qué tramo de línea pertenece el apoyo: N, A, B, C o S. Dos apoyos son comunes a varios tramos y tienen varias letras.

**Dónde está el apoyo**
- `x`, `y`: coordenadas en metros, sistema ETRS89 / UTM 30N (EPSG:25830). En él es cómodo medir distancias.
- `lon`, `lat`: los mismos puntos en grados de longitud y latitud (WGS 84). Sirven para los mapas web.
- `lidar_x`, `lidar_y`: dónde apareció el apoyo en la nube de puntos lidar.
- `dist_osm_lidar_m`: distancia entre el punto de OpenStreetMap y el punto del lidar, en metros.
- `lidar_note`: una nota cuando no se pudo encontrar el apoyo en el lidar.

**Alturas**
- `z_base_mdt02`: altitud del terreno en la base del apoyo según el modelo digital del terreno oficial MDT02, en metros sobre el nivel del mar.
- `z_base_dtm_cyl`: lo mismo, según nuestro modelo del terreno hecho con el lidar de 2025.
- `dz_dtm_mdt02`: diferencia entre esas dos altitudes, en metros. Nos dice cuánto coinciden los dos modelos del terreno.
- `height_ndsm_m`: altura del propio apoyo sobre el terreno según el lidar, en metros.

**El apoyo y el relieve**
- `slope_deg`: pendiente de la ladera junto al apoyo, en grados.
- `bend_deg`: cuántos grados gira la línea en este apoyo.
- `anchor_candidate`: posible apoyo de amarre, en el que el conductor va fijado de forma rígida, normalmente en los cambios de dirección. Valores `True` (sí) o `False` (no).
- `anchor_reason`: por qué lo hemos decidido así.
- `rlat_zone`: zona por altitud según el reglamento de líneas de alta tensión: A, B o C. En la zona C, por encima de 1000 m, el reglamento tiene en cuenta el hielo sobre los conductores.
- `dtm_interpolated`: 1 si hubo que completar la altitud del terreno en el apoyo porque debajo no había puntos de suelo; 0 si no.

**Notas de control**
- `lidar_sheet`: hoja lidar del PNOA en la que está el apoyo.
- `surveys`: qué vuelos cubren el apoyo: CYL, Castilla y León 2025; AST, Asturias 2024.
- `inside_corridor`: el apoyo está dentro del corredor de 100 m desde los conductores (`True` o `False`).
- `control_section`: el apoyo está en el tramo de control, donde lo comprobamos todo a mano (`True` o `False`).
- `verified`: quién revisó el apoyo, cuándo y cómo.
- `screenshot`: ruta a la captura de pantalla de la revisión.

Vemos que hay columnas de varias clases: nombres y notas, números en metros y en grados, respuestas de «sí o no». Son distintos **tipos de variables**, y del tipo depende lo que podemos hacer con ellas.

:::{admonition} Tus datos
La descripción de las columnas casi siempre está junto a los datos:

- en las webs donde se descargan datos abiertos, en un archivo de descripción o de metadatos (en el IGN y el CNIG, en la sección de documentación de cada conjunto; en NASA FIRMS, en la descripción de los campos del archivo; en OpenStreetMap, en la wiki, donde se explica cada etiqueta);
- en la carpeta de los datos, en archivos `README`, `readme.txt` o un PDF descriptivo.

Si no hay descripción, se la pedimos a quien nos dio los datos. Y mientras llega la respuesta, escribimos nuestro propio diccionario: miramos los valores de cada columna y marcamos con honestidad aquello de lo que no estamos seguros.
:::

## Paso 7. Las primeras filas

```python
# %%
towers.head()
```

```text
     osm_node  ...                       screenshot
0  2002883828  ...  screenshots/power-towers/48.png
1  2002883818  ...  screenshots/power-towers/47.png
2  2002883813  ...  screenshots/power-towers/46.png
3  2002883812  ...  screenshots/power-towers/45.png
4  2002883810  ...  screenshots/power-towers/44.png

[5 rows x 28 columns]
```

`head()` muestra las cinco primeras filas. Pero 28 columnas no caben en la pantalla, y pandas esconde las del medio tras unos puntos suspensivos `...`. Por eso elegimos solo las columnas que necesitamos:

```python
# %%
towers[["label", "lines", "x", "y", "slope_deg", "height_ndsm_m"]].head()
```

```text
  label lines          x           y  slope_deg  height_ndsm_m
0   N01     N  274101.61  4766898.64        7.5           28.6
1   N02     N  274178.44  4766662.48       18.0           36.1
2   N03     N  274313.17  4766250.94       25.2           29.3
3   N04     N  274267.19  4765923.44       18.6           33.7
4   N05     N  274307.95  4765728.18       15.5           22.6
```

Los corchetes dobles son una lista con los nombres de las columnas que queremos ver. Los de fuera dicen «elegir de la tabla»; los de dentro, «esta es la lista».

A la izquierda están los números de fila: pandas empieza a contar desde cero, así que el primer apoyo tiene el número 0.

## Qué ha salido

Lo comparamos con lo que esperábamos:

- **33 filas**, una por apoyo. Coincide.
- **Coordenadas en metros:** x alrededor de 274 000 e y alrededor de 4 766 000. Son metros en el sistema UTM 30N, no grados. Coincide.
- **Alturas de los apoyos** en las primeras filas: de 22,6 a 36,1 m. Coincide en general. Solo N05, con 22,6 m, es más bajo de lo que esperábamos. Lo apuntamos.
- **Pendientes** de 7,5 a 25,2 grados: terreno de montaña, como debe ser.

La tabla parece apta para trabajar. Pero solo hemos mirado cinco filas de 33.

## Si algo falla

- **`FileNotFoundError`**: Python no ha encontrado el archivo. Casi siempre es una errata en la ruta o el archivo está en otra carpeta. Comprobamos la ruta: imprimimos `towers_file` y la comparamos con el sitio donde está el archivo en las carpetas del ordenador (Finder en Mac, Explorador de archivos en Windows).
- **`ModuleNotFoundError: No module named 'pandas'`**: el entorno elegido no es el correcto. Volvemos a **Python: Select Interpreter** → `field-to-code-statistics`.
- **No aparece el botón Run Cell**: en VS Code no están instaladas las extensiones Python y Jupyter de Microsoft. Se instalan en la pestaña **Extensions**.

## Resumen

**Conceptos nuevos**
- **Ciclo PPDAC**: los cinco pasos de cualquier trabajo con datos: pregunta, plan, datos, análisis, conclusión. Ejemplo: hoy estamos en el paso «datos».
- **Tabla (DataFrame)**: tabla de pandas en la que las columnas tienen nombre y las filas, número. Ejemplo: `towers`.
- **Diccionario de datos**: la descripción de cada columna: significado, unidades, origen. Ejemplo: `height_ndsm_m` es la altura del apoyo sobre el terreno en metros.
- **Tamaño de la tabla**: número de filas y columnas. Ejemplo: `(33, 28)`.

**Código nuevo**

```python
import pandas as pd                       # connect pandas
towers = pd.read_csv("towers.csv")        # open a CSV table
towers.shape                              # number of rows and columns
towers.columns.tolist()                   # list of column names
towers.head()                             # first five rows
towers[["label", "height_ndsm_m"]]        # only the columns we need
```

**Lo esencial**
- Antes de calcular, comprobamos el tamaño de la tabla y preparamos el diccionario de datos.
- Una fila, un objeto. Aquí, una fila es un apoyo.

## Preguntas para un ingeniero

1. ¿Por qué hemos comprobado que hay exactamente 33 filas en vez de ponernos a calcular directamente?

   :::{dropdown} Respuesta

   Es la comprobación de que una fila es un apoyo. Si hubiera apoyos repetidos o faltara alguno, todos los cálculos posteriores, como la altura media o el número de apoyos en pendientes fuertes, serían erróneos.
   :::

2. ¿Para qué sirve el diccionario de datos, si los nombres de las columnas ya dan alguna pista?

   :::{dropdown} Respuesta

   El nombre no dice ni las unidades, ni el origen, ni el significado exacto. Por ejemplo, `dz_dtm_mdt02` no se entiende sin el diccionario. Y si confundimos las unidades o el significado, cualquier conclusión será errónea.
   :::

3. En las primeras filas, el apoyo N05 mide 22,6 m y los demás, unos 30 m. ¿Qué hacemos con esto ahora?

   :::{dropdown} Respuesta

   De momento, no cambiamos ni borramos nada. Es un motivo para mirar con más atención. Puede que el apoyo sea de verdad más bajo, o puede que el lidar no lo haya captado bien. Decidimos solo cuando lo hayamos aclarado.
   :::

## Ejercicios

1. ¿Con qué comando de pandas se abre una tabla CSV?

2. Completa el código para saber cuántas filas y columnas tiene la tabla: `towers.____`

3. ¿Qué tres tipos de datos espaciales encontramos en el puerto de Pajares?

[Respuestas](#es-ch01-l01)

## La pregunta que queda abierta

Las cinco filas tienen buena pinta. Pero ¿qué hay en las otras 28? ¿Hay valores vacíos o números raros? Por ejemplo, ¿hay algún apoyo cuya altura sea muy distinta de la de los demás?

## Notas y fuentes

- Tabla de apoyos: referencia del corredor oriental de las líneas de 400 kV, proyecto Pajares, revisión del 17/10/2026; © colaboradores de OpenStreetMap (ODbL); «PNOA cedido por © Instituto Geográfico Nacional».
- pandas: https://pandas.pydata.org
- Miniforge (conda): https://conda-forge.org/download/

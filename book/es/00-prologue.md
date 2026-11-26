---
title: "Prólogo. ¿De qué números podemos fiarnos?"
---

## Octubre de 2018 en el puerto de Pajares

A finales de octubre de 2018, el invierno llegó pronto a Pajares. Nevó con fuerza cuando los árboles todavía tenían las hojas. La nieve se pegaba a las copas, los árboles no aguantaban el peso, se partían, se arrancaban de raíz y caían sobre las líneas. Esos mismos árboles cortaron las carreteras, y a los electricistas, con las quitanieves, les costaba hasta llegar al lugar de la avería [1, 2].

Al tercer día, Viesgo todavía tenía 679 clientes sin luz: 384 en Pajares, 79 en la parte alta de Casomera y 224 en la parte alta de Tuiza (por lugares suman 687; así lo da la fuente). EDP tenía otros 4000 [1].

Y era ya la segunda vez ese año. En febrero, el 112 Asturias también había relacionado los cortes con árboles caídos y desprendimientos de tierra. Entonces se quedaron sin luz unos 10 000 abonados. Lo que retrasaba las reparaciones eran, otra vez, los árboles caídos, los desprendimientos y los puertos cerrados por la nieve [3].

**En la montaña, un árbol caído hace dos cosas a la vez: rompe el cable y corta el camino para llegar a él.**

## Qué exige la norma

En España, las líneas aéreas de alta tensión tienen su norma: la ITC-LAT 07. En el apartado 5.12.1 exige talar los árboles que, al inclinarse o caer, puedan alcanzar los conductores [4].

Es decir, la norma responde a una pregunta: si este árbol cae, ¿llega al cable? Lo que no pregunta es si ese árbol va a caer en un temporal.

Y la diferencia es grande. En la montaña, a lo largo de las líneas, hay muchísimos árboles que podrían llegar al cable. Talarlos todos de una vez es imposible, y la distribuidora necesita saber por cuáles empezar. Para decidirlo, hay que saber cuáles tienen más probabilidades de caer. **Y eso ya es una pregunta de probabilidad.**

## Un solo número no basta

En España, la calidad del suministro eléctrico se mide con el TIEPI. A grandes rasgos, son las horas al año que, de media, nos quedamos sin luz. El ministerio calcula por separado la parte que se debe al mal tiempo y a otras causas que la distribuidora no puede controlar. Así evolucionó esa parte en la zona rural dispersa, es decir, en montañas, aldeas y caseríos [5]:

- 2008: 0,05 horas;
- 2009: 1,83 horas;
- 2010: 3,66 horas;
- 2011: 0,04 horas.

En dos años se multiplica por setenta, y al tercero vuelve a ser casi cero. Está claro que la red no empeoró setenta veces para luego arreglarse en un año. Simplemente llegaron los temporales y después se fueron.

Hay una segunda dificultad. Las distribuidoras comunican estos indicadores cada año, municipio por municipio. Pero el ministerio solo los publica en abierto por país, comunidad autónoma, provincia y tipo de zona. Las causas también aparecen, pero solo en grandes grupos: mal tiempo, causas propias de la distribuidora, etc. Si fue un árbol, el viento o la nieve no se publica en abierto en ningún sitio [5, 6].

Por eso, con un número así no podemos saber lo esencial:

1. **¿Es una tendencia o una casualidad?** Puede que haya más temporales, o puede que simplemente hayan tocado dos años malos seguidos.
2. **¿Dónde pasó?** La media del país no dice qué líneas ni qué laderas sufrieron.
3. **¿Por qué?** Viento, nieve húmeda, árboles caídos: en la media todo queda mezclado.

**Para separar lo que sigue un patrón de lo que es casualidad, y entender dónde y por qué pasan las cosas, necesitamos la estadística.**

## Cuando el cambio es menor que el error

A veces, lo que queremos medir es más pequeño que el error de la propia medida.

Para talar a tiempo los árboles cerca de las líneas, hay que saber a qué ritmo crece el bosque. La altura del bosque en toda España se puede medir gratis con los vuelos lidar repetidos del PNOA. Pero el más antiguo de esos vuelos tiene un error en altura de hasta 20 centímetros en terreno llano y despejado [7]. En el bosque y en pendientes fuertes, el error es todavía mayor.

Y un haya en Asturias crece unos 12 centímetros al año [8]. En los 12 años que separan el primer vuelo del tercero, eso es alrededor de 1,4 metros. Y los errores del vuelo antiguo en un bosque de montaña son comparables a ese crecimiento.

**Así que, antes de creernos cualquier tasa de crecimiento, tenemos que saber qué cambio somos capaces de distinguir del error.** La respuesta será un número, y ese número también tendrá su incertidumbre. Calcularlo es cosa de la estadística.

Donde el bosque crece deprisa —en franjas de seguridad tras un desbroce, en zonas quemadas, en bosque joven—, medir el crecimiento es más fácil.

## Los datos también pueden engañar

Antes de calcular nada, hay que mirar los datos.

Los satélites de la NASA detectan cada día en la Tierra puntos con temperaturas anormalmente altas y los suben al archivo abierto FIRMS. Normalmente son incendios. Entre 2012 y 2025, el sensor VIIRS del satélite S-NPP detectó en Asturias 31 668 de esos puntos. Pero 18 273 de ellos, el 58 %, los marca el propio archivo como fuentes de calor permanentes: lugares que están calientes todos los años [9]. La mayoría están en la costa industrial entre Avilés y Gijón, donde los altos hornos funcionan sin parar.

Si cogiéramos todos los puntos sin más y buscáramos dónde arde más a menudo en Asturias, el lugar con más «riesgo de incendio» sería una siderúrgica. Y la fórmula no tendría ninguna culpa. **Simplemente no habríamos mirado los datos.**

Para nuestro proyecto, los incendios también importan por sí mismos. Los árboles quemados se parten y caen con los primeros vientos fuertes [10]. **Por eso, una zona quemada junto a una línea son árboles que pueden caer sobre el cable ya el primer invierno.**

## Las tres partes del proyecto

El proyecto Pajares tiene tres partes. Siempre van en el mismo orden, porque cada una se apoya en la anterior.

1. **El crecimiento de los árboles con vuelos lidar repetidos.** Queremos saber a qué ritmo crece el bosque junto a las líneas y hasta qué punto podemos fiarnos de esas cifras. Aquí la pregunta principal es dónde el crecimiento se distingue del error de medida.
2. **Un recopilador abierto de eventos.** Es un catálogo de temporales, nevadas de nieve húmeda, incendios y cortes de suministro por municipio, con las marcas «árbol sobre la línea» y «árbol sobre la carretera». Aquí queremos entender qué parte de los cortes se debe a los árboles y hasta qué punto podemos fiarnos de las marcas automáticas.
3. **El riesgo de que caigan árboles sobre las líneas desde fuera de la franja de seguridad.** Aquí valoramos tres cosas a la vez: cuánto está expuesto el lugar a los temporales, cuánto de inestable es el árbol y si llegaría al cable. Y comprobamos si esta valoración funciona con temporales reales mejor que la simple regla de la norma.

La relación entre las partes es directa. De la primera sacamos la altura y el crecimiento de los árboles para la tercera. En la segunda reunimos los eventos reales con los que ponemos a prueba la tercera. **Si las cifras de la primera parte no son fiables, no tenemos sobre qué construir todo lo demás.**

## Lo que está cerca se parece

En Pajares tenemos los tres tipos de datos espaciales, y cada uno tiene su propia estadística.

1. **Puntos:** sucesos y objetos en un lugar concreto. Por ejemplo, los 33 apoyos de las líneas de 400 kV o los puntos de incendio. Nos interesa saber si están repartidos al azar o se agrupan.
2. **Superficies:** una magnitud que existe en todas partes, como el relieve, la altura del bosque o la diferencia entre dos vuelos. Solo la conocemos en algunos puntos o celdas, y queremos saber qué hay entre ellos y con cuánta certeza lo sabemos.
3. **Áreas:** una magnitud calculada para un territorio. Por ejemplo, los 78 municipios de Asturias o los cortes de suministro por municipio. Aquí miramos si las áreas vecinas se parecen entre sí.

Los tres tienen algo en común: lo que está cerca suele parecerse. Las celdas vecinas de un bosque tienen la misma edad; las laderas vecinas las barre el mismo viento. Las fórmulas habituales de la estadística dan por hecho que cada medida es independiente de las demás. En un mapa no es así, y esas fórmulas nos dan más certeza de la que realmente tenemos. **La estadística espacial es precisamente la que tiene en cuenta a los vecinos.**

## Nuestra pregunta

**¿Dónde caerá el bosque sobre las líneas en un temporal, y de qué números podemos fiarnos?**

Vamos hacia la respuesta paso a paso, lección a lección, con Python y con datos abiertos de Asturias y del puerto de Pajares. No hace falta saber estadística ni programar de antemano: cada concepto nuevo lo vemos en el momento en que lo necesitamos para el trabajo.

Y empezamos por donde empieza cualquier trabajo con datos: abrimos una tabla y miramos qué hay dentro.

## Preguntas para comprobar lo que hemos entendido

1. **¿Qué exige la norma ITC-LAT 07 y qué es lo que no pregunta?**

   :::{dropdown} Respuesta
   Exige talar los árboles que podrían alcanzar el cable si cayeran. Pero no pregunta si el árbol va a caer en un temporal.
   :::

2. **¿Por qué la serie del TIEPI no nos permite decir que la red empeoró en 2010?**

   :::{dropdown} Respuesta
   El salto lo produjo el mal tiempo, no el estado de la red: en 2011 el indicador vuelve a estar casi a cero. Con un solo número no se distingue una tendencia de una casualidad.
   :::

3. **¿Para qué necesita estadística la primera parte del proyecto, si el lidar ya mide la altura?**

   :::{dropdown} Respuesta
   Lo que crece un haya en 12 años es comparable al error del vuelo antiguo. Mientras no estimemos la incertidumbre, no podemos decir si lo que vemos es crecimiento o error.
   :::

4. **¿Por qué las fórmulas habituales de la estadística dan demasiada certeza cuando trabajamos con mapas?**

   :::{dropdown} Respuesta
   Consideran que cada medida es independiente. Pero en un mapa los lugares vecinos se parecen entre sí, así que hay menos información realmente independiente de la que parece.
   :::


## Fuentes

1. OKDiario, 30.10.2018. <https://okdiario.com/espana/temporal-deja-sin-luz-tres-dias-mas-4-500-personas-asturias-3291859>
2. La Voz del Trubia, 29.10.2018. <https://lavozdeltrubia.es/2018/10/29/somiedo-teverga-y-parte-de-quiros-siguen-sin-luz-por-el-temporal/>
3. 112 Asturias, febrero de 2018. <https://www.112asturias.es/112-asturias-coordinara-actuaciones-para-restablecimiento-suministro-electrico-telefonico>
4. ITC-LAT 07 (RD 223/2008), apartado 5.12.1. <https://normatia.com/es/normativa/reglamento-lineas-alta-tension/2025/instruccion-tecnica-complementaria-itc-lat-07-lineas-aereas-con-conductores/>
5. MITECO, Índices de calidad eléctrica; serie TIEPI por tipo de zona 2003–2021, zona rural dispersa, fuerza mayor. <https://www.miteco.gob.es/es/energia/energia-electrica/electricidad/calidad-servicio/indices.html>
6. Orden ECO/797/2002, BOE. <https://www.boe.es/diario_boe/txt.php?id=BOE-A-2002-7133>
7. IGN/CNIG, especificaciones técnicas del vuelo LiDAR PNOA, primera cobertura: error medio cuadrático en altura menor de 0,20 m.
8. MITECO, Cuarto Inventario Forestal Nacional (IFN4), Asturias, tabla 926 «Media del incremento anual de altura»: *Fagus sylvatica*, 0,117 m/año (media de 3285 árboles).
9. NASA FIRMS, archivo VIIRS S-NPP 375 m, Asturias, 2012–2025; campo `TYPE = 2` (fuente de calor estática). <https://firms.modaps.eosdis.nasa.gov/download/>
10. BPA, *How wildfires can contribute to power outages*. <https://www.bpa.gov/learn-and-participate/community-education/wildfires-and-public-safety>

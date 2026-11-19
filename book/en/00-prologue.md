---
title: "Prologue: Which numbers can we trust?"
---

## October 2018 on the Pajares Pass

Winter came early to Pajares at the end of October 2018. Heavy snow fell while the trees were still in leaf. The snow clung to the crowns, and the trees couldn't take the weight: they snapped, were torn out by the roots and fell straight onto the lines. They blocked the roads too, so the electricians and the snowploughs struggled even to reach the faults [1, 2].

On the third day, Viesgo still had 679 customers without power: 384 in Pajares, 79 in upper Casomera and 224 in upper Tuiza. EDP had another 4,000 customers off supply [1].

And this was already the second time that year. Back in February, Asturias's 112 emergency service had also linked outages to fallen trees and landslides. That time, around 10,000 customers lost power. Repairs were held up by the same things: fallen trees, landslides and passes closed by snow [3].

So in the mountains a fallen tree does two things at once: it brings down the wire and it blocks the road to it.

## What the regulations require

Spain has a regulation for high-voltage overhead lines, ITC-LAT 07. Section 5.12.1 requires the felling of trees that could reach the conductors if they leant over or fell [4].

In other words, the regulation answers one question: will this tree reach the wire if it falls? What it doesn't ask is whether the tree will fall in a storm.

That's a big difference. In the mountains there are a great many trees along the lines that could reach a wire. Felling them all at once is impossible, so the company needs to know where to start. And to decide that, we need to know which trees are most likely to fall. That's a question about probability.

## One number isn't enough

In Spain, quality of supply is measured with an indicator called TIEPI. Roughly speaking, it's the average number of hours a year without power. The ministry calculates separately the part caused by bad weather and other things the company can't control. Here's how that part looked in dispersed rural areas – mountains, villages and isolated farmsteads [5]:

- 2008: 0.05 hours;
- 2009: 1.83 hours;
- 2010: 3.66 hours;
- 2011: 0.04 hours.

In two years it grew seventyfold, and in the third year it was back to almost zero. Clearly the network didn't get seventy times worse and then mend itself within a year. The storms simply came, and then went.

There's a second problem too. Every year the companies report these indicators for each municipality. But the ministry only publishes them openly for the country as a whole, the autonomous communities, the provinces and the types of zone. The causes are there as well, but only in broad groups: bad weather, the company's own causes and so on. Whether it was a tree, the wind or snow isn't published openly anywhere [5, 6].

So a number like this can't tell us what matters most:

- **Is it a trend or chance?** Perhaps there are more storms now, or perhaps we just had two bad years in a row.
- **Where did it happen?** A national average doesn't tell us which lines and which slopes were hit.
- **Why?** Wind, wet snow, fallen trees – in an average it's all mixed together.

Separating pattern from chance, and understanding where and why things happen, is exactly what we need statistics for.

## When the change is smaller than the error

Sometimes what we want to measure is smaller than the error of the measurement itself.

To fell trees near the lines in time, we need to know how fast the forest grows. Forest height across the whole of Spain can be measured for free from the repeat airborne laser surveys of the PNOA programme. But the oldest of these surveys has a height error of up to 20 centimetres on flat, open ground [7]. In forest and on steep slopes it's larger still.

Beech in Asturias, meanwhile, grows about 12 centimetres a year [8]. Over the 12 years between the first and third surveys, that's about 1.4 metres. And the errors of the old survey in mountain forest are comparable to that growth.

So before we believe any growth rate, we have to work out what size of change we can actually tell apart from the error. The answer will be a number, and that number will have its own uncertainty. Statistics helps us calculate it.

Where the forest grows fast – in cleared corridors, on burnt ground, in young woodland – growth is easier to measure.

## Data can mislead us too

Before we calculate anything, we need to look at the data.

Every day, NASA satellites spot points on Earth with unusually high temperatures and put them in the open FIRMS archive. Usually these are fires. Between 2012 and 2025, the VIIRS instrument on the S-NPP satellite detected 31,668 such points in Asturias. But the archive itself flags 18,273 of them, or 58%, as persistent heat sources – places that are hot every year [9]. Most of them are on the industrial coast between Avilés and Gijón, where the blast furnaces run non-stop.

If we took every point as it came and went looking for where Asturias burns most often, the most 'fire-prone' place would turn out to be a steelworks. And no formula would be to blame: we would simply have failed to look at the data.

Fires also matter to our project in their own right. Burnt trees snap and fall in the first strong winds [10]. So burnt areas near the lines are trees that could fall on a wire as early as the very first winter.

## Three parts of the project

The Pajares project has three parts. They always come in the same order, because each one builds on the one before.

1. **Tree growth from repeat lidar surveys.** We want to know how fast the forest near the lines is growing and how far we can trust those figures. The key question here is where the growth stands out from the measurement error.
2. **An open event collector.** This is a catalogue of storms, wet snow, fires and outages by municipality, tagged 'tree on line' and 'tree on road'. Here we want to find out what share of outages is caused by trees, and how far we can trust the automatic tags.
3. **The risk of trees falling on the lines from outside the cleared corridor.** Here we assess three things together: how exposed the site is to storms, how unstable the tree is, and whether it can reach the wire. Then we check whether this assessment works better on real storms than the regulation's simple rule.

The parts are directly linked. From the first we take tree height and growth for the third. In the second we collect the real events on which we test the third. If the figures in the first part can't be trusted, there's nothing to build the rest on.

## Near things are alike

Pajares has all three kinds of spatial data, and each kind has its own statistics.

- **Points** – events and objects at a specific location. For example, the 33 towers of the 400 kV lines, or fire points. What interests us is whether they're scattered at random or cluster together.
- **Surfaces** – a quantity that exists everywhere: terrain, forest height, the difference between two surveys. We only know it at individual points or cells, and we want to understand what lies between them and how sure we can be.
- **Areas** – a quantity calculated over a territory. For example, the 78 municipalities of Asturias, or outages by municipality. Here we look at whether neighbouring areas resemble each other.

All three have one thing in common: things that are close together are usually alike. Neighbouring forest cells are the same age; neighbouring slopes are swept by the same wind. Ordinary statistical formulas assume that each measurement is independent of the others. On a map that isn't true, so ordinary formulas give us more confidence than we really have. Spatial statistics takes the neighbours into account.

## Our question

Where will the forest fall on the lines in a storm – and which numbers can we trust?

We'll work towards the answer step by step, lesson by lesson, in Python and with open data for Asturias and the Pajares Pass. There's no need to know statistics or programming beforehand: we deal with each new idea at the moment the work calls for it.

And we start where all work with data starts: we open a table and look at what's inside.

## Comprehension questions

1. **What does ITC-LAT 07 require, and what doesn't it ask?**

   :::{dropdown} Answer
   It requires felling trees that could reach a wire if they fell. But it doesn't ask whether the tree will fall in a storm.
   :::

2. **Why can't we say from the TIEPI series that the network got worse in 2010?**

   :::{dropdown} Answer
   The jump came from bad weather, not from the state of the network – in 2011 the figure was back to almost zero. A single number can't tell a trend from chance.
   :::

3. **Why does the first part of the project need statistics, if lidar measures height anyway?**

   :::{dropdown} Answer
   Beech growth over 12 years is comparable to the error of the old survey. Until we estimate the uncertainty, we can't say whether we're seeing growth or error.
   :::

4. **Why do ordinary statistical formulas give too much confidence on maps?**

   :::{dropdown} Answer
   They treat every measurement as independent. But on a map neighbouring places resemble each other, so there's less truly independent information than it seems.
   :::


## Sources

1. OKDiario, 30 October 2018. <https://okdiario.com/espana/temporal-deja-sin-luz-tres-dias-mas-4-500-personas-asturias-3291859>
2. La Voz del Trubia, 29 October 2018. <https://lavozdeltrubia.es/2018/10/29/somiedo-teverga-y-parte-de-quiros-siguen-sin-luz-por-el-temporal/>
3. 112 Asturias, February 2018. <https://www.112asturias.es/112-asturias-coordinara-actuaciones-para-restablecimiento-suministro-electrico-telefonico>
4. ITC-LAT 07 (RD 223/2008), section 5.12.1. <https://normatia.com/es/normativa/reglamento-lineas-alta-tension/2025/instruccion-tecnica-complementaria-itc-lat-07-lineas-aereas-con-conductores/>
5. MITECO, quality-of-supply indices; TIEPI series by zone type 2003–2021, dispersed rural zone, force majeure. <https://www.miteco.gob.es/es/energia/energia-electrica/electricidad/calidad-servicio/indices.html>
6. Orden ECO/797/2002, BOE. <https://www.boe.es/diario_boe/txt.php?id=BOE-A-2002-7133>
7. IGN/CNIG, PNOA LiDAR technical specifications, first coverage: vertical RMSE below 0.20 m.
8. MITECO, Fourth National Forest Inventory (IFN4), Asturias, table 926 'Mean annual height increment': *Fagus sylvatica*, 0.117 m/year (mean of 3,285 trees).
9. NASA FIRMS, VIIRS S-NPP 375 m archive, Asturias, 2012–2025; field `TYPE = 2` (static land source). <https://firms.modaps.eosdis.nasa.gov/download/>
10. BPA, *How wildfires can contribute to power outages*. <https://www.bpa.gov/learn-and-participate/community-education/wildfires-and-public-safety>

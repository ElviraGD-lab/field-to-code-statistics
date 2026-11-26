---
title: "About this book"
---

## Who this book is for

This book is for engineers who have spent years in the field with survey instruments. We know cartography, we work in QGIS, we can take points and check a survey. But hardly any of us ever studied statistics properly. And we don't know the tools that companies use for their calculations today, either.

That's where the book begins. No prior knowledge is needed.

## What this book teaches

Each book in the series has one job. This one's is **spatial statistics in Python, from scratch.**

First, let's work out what that actually means.

**Statistics** helps us understand what numbers are telling us, and whether we can trust them. For example, which tower heights are normal and which are odd. Or whether the forest has really started growing faster – or whether it only looks that way because the survey isn't accurate.

**Spatial statistics** adds something every field engineer knows from experience: near things are alike. Neighbouring slopes are swept by the same wind; neighbouring trees are the same age. Ordinary statistical formulas don't know this. To them, every measurement stands on its own, unconnected to anything else. That's why, on a map, they give an answer that is too confident. We'll learn how to allow for this.

The other books in the series take their statistics from here. The lidar book, for example, calculates how fast the forest grows, and a lesson in this book explains whether we can trust that growth rate.

## What this book doesn't teach

Let's agree on three things from the start.

1. **We don't teach Python from scratch here.** The language itself is covered in the first book of the series, *PyQGIS from Scratch*. Here we simply use it. We explain every new line of code in plain words: what it does and why.
2. **We don't teach all the statistics in the world, either.** We take only the basics the project needs, and we learn them properly.
3. **This isn't a coding drill book.** The code can be copied and run, but the book can also just be read. What matters is understanding what we're doing, why, and how we check that we haven't made a mistake.

## How we work

The book is written by an engineer just like us, who is learning right now too. We don't have ready-made answers. We move through the project step by step, and each lesson is one step.

Every lesson follows the same order:

1. First, we ask a question.
2. Then we write down what we think we should see. We write this down **before the calculation.**
3. Then we calculate.
4. And we compare the result with what we expected.

If our guess turns out wrong, that's a result too. We work out why. The mistakes we tripped over stay in the lesson as well: they're what we learn from most.

## Our project

Pajares is a mountain pass between Asturias and León. Here, on a single slope, forest, wet snow, strong winds and 400 kV power lines all come together. In winter, trees fall on the wires and block the roads that repair crews use to reach the faults.

The whole project answers one question: **where will the forest fall on the lines in a storm – and which numbers can we trust?** The prologue explains why the question is exactly this one.

## What we'll cover

The path goes from simple to complex. Each part builds on the one before.

1. **Looking at the data.** We open a table, check what's in it, and draw our first charts and our first map.
2. **Describing numbers.** What's a typical value, how big is the spread, and what do we do with odd values?
3. **Looking for relationships.** How one quantity depends on another – for example, a tree's height on the thickness of its trunk.
4. **Getting to grips with probability.** Through experiments on the computer, not through complicated formulas.
5. **Checking whether we can trust a number.** Could this be chance? How sure are we of the result?
6. **Working with maps in Python.** Points, lines, rasters, coordinate systems.
7. **Surfaces.** How to estimate a value between measurement points, and how sure we can be of that estimate.
8. **Areas.** Do neighbouring municipalities resemble each other?
9. **Events.** Are fires scattered at random or do they cluster together, and why?
10. **Machine learning.** And above all, how to test a model honestly on a place it has never seen.
11. **The project tasks.** This is where everything we've learnt goes to work on the real questions of Pajares.

## Tools

Only what companies work with today:

- **Python** in the **VS Code** editor. Libraries are installed with a program called **conda**.
- **pandas** – tables.
- **seaborn** and **matplotlib** – charts.
- **geopandas** – layers of points, lines and polygons, much like in QGIS, only in code.
- **rasterio** – rasters.
- **NumPy** and **SciPy** – calculations and experiments with random numbers.
- **statsmodels** – relationships between quantities and hypothesis testing.
- **scikit-learn** – machine learning.
- **PySAL** – neighbours on the map and everything to do with them.
- **scikit-gstat** and **GSTools** – surfaces: how a value changes with distance and how to estimate it between points.

We explain each tool from scratch the first time the work needs it.

## Data

All the data is open:

- lidar and elevation models from Spain's National Geographic Institute (IGN);
- fire points from NASA satellites;
- OpenStreetMap;
- the ministry's quality-of-supply indicators;
- calls to Asturias's 112 emergency service.

Every lesson says where its data comes from. There's also a 'Your data' box: what to change to do the same thing for our own area.

## How a lesson is laid out

To make every lesson easy to find our way around, the order is always the same:

- **Where we left off** – briefly, so we don't have to page back.
- **What we want to know** – the question and our guess.
- **Steps** – each step, its code and a line-by-line explanation.
- **What we found** – the result set against our guess.
- **If something goes wrong** – the real errors we hit and how we found the cause.
- **Your data.**
- **Summary** – new terms, new code and key points.
- **Questions for an engineer** – with the answers right below the questions.
- **Exercises** – three short ones, from memory, and one for practice: the same thing on other data; the answers are on a separate page at the end of the book.
- **The open question.**
- **Notes and sources.**

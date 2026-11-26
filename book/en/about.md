---
title: "About this book: what we learn, which tools we use and who it's for"
---

## Who it's for

This book is for engineers and technicians who have worked in the field and now want to work with spatial data the way companies do today. Surveyors, foresters, power engineers, GIS specialists: people who know their own field inside out, but who never studied statistics (or forgot it long ago) and don't write code.

No prior knowledge is needed. The Python language itself is covered from scratch, inside QGIS, in the first book of the series, *PyQGIS from Scratch*. Here we learn from scratch how to run Python outside QGIS (conda, VS Code, code cell by cell), and we explain every new line as it comes.

## What we learn

We go all the way from our first table to a risk model, working on a real project.

- **Data, and how to look at it.** We open any table, check it, understand its data types, draw the right chart and our first map, and describe the centre and the spread – in a way that stops a single outlier from spoiling the result.
- **Models.** How one quantity depends on another, and how to predict a yes or a no.
- **Probability.** We learn it through simulation on the computer, not through formulas. Then come the distributions that describe the number of events, wind and measurement error.
- **When we can trust a result.** Permutation tests, the bootstrap and the confidence interval, decision errors, and setting the threshold before we calculate.
- **Spatial data in Python.** Vectors, rasters, coordinate reference systems, and features along a line.
- **Surfaces.** The variogram, interpolation, kriging, and how to check an interpolation.
- **Areas.** Neighbours, spatial autocorrelation and hotspots.
- **Events.** Are points scattered at random, or do they cluster together? And why are there more of them in some places than in others?
- **Machine learning on geodata.** Features, decision trees and ensembles – and, most importantly, testing the model honestly on a new location.
- **The Pajares project tasks.** The error in the difference between two surveys and the minimum detectable change, the uncertainty in the growth rate, rare storms, checking automatic labels, the share of outages caused by trees, and the risk model, tested against real events.

## Which tools we use

Only the tools people actually work with today:

- Python in the VS Code editor, with a conda environment;
- pandas for tables; seaborn and matplotlib for charts;
- geopandas, rasterio and rioxarray for vectors and rasters;
- NumPy and SciPy for simulations and distributions; statsmodels for regression and hypothesis testing;
- scikit-learn for machine learning and model validation;
- PySAL for neighbourhoods, spatial autocorrelation and point processes;
- scikit-gstat and GSTools for variograms and kriging.

All the code can be copied and run as it is. The data is open: lidar and elevation models from the IGN, fires from NASA FIRMS, OpenStreetMap, and quality-of-supply indicators from MITECO.

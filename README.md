# From Field to Code: Spatial Statistics from Scratch

**Del campo al código: estadística espacial desde cero**

An open book on **spatial statistics in Python**, written for engineers and field specialists who have never studied statistics. It starts with the foundations (looking at data, describing it, probability, intervals, tests, models) and moves step by step into spatial statistics: point patterns, geostatistics and areal data.

Book 3 of the *From Field to Code* series. Written in Spanish and English.

> Status: work in progress (started November 2026).

## The data

Every chapter works on real open data from Asturias (Spain), most of it from the Pajares project on forests, storms and power lines: national LiDAR and elevation models, power line towers and spans, wildfire detections, weather records and municipal boundaries. Sources and licences are listed in [`data/README.md`](data/README.md).

## Run the code

Every code block in the book is also in a tested script in [`code/`](code/). The scripts run top to bottom without errors.

```bash
conda env create -f environment.yml
conda activate field-to-code-statistics
python code/ch01_first_look.py
```

## The series

*From Field to Code* is a series of open books for engineers and field specialists who want to work with spatial data the way the industry does today. All books: https://elviragd-lab.github.io

## Read and build

The book is written in [MyST Markdown](https://mystmd.org). To build it locally:

```bash
npm install -g mystmd@1.12.0
cd book
myst start
```

## Licence

- Code: Apache License 2.0 (`LICENSE`)
- Text and figures: CC BY 4.0 (`LICENSE-docs`)
- Data attributions: see `data/README.md`

© 2026 Elvira Gayanova

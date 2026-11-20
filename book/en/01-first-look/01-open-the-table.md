---
title: "Lesson 1. Opening the tower table"
---

(en-ch01-l01-lesson)=
## Where we are

The project has one main question: where will the forest fall on the lines in a storm, and which numbers can we trust? We're going to answer it step by step, and the first step is the data. We start with the simplest and most important table: the towers of the 400 kV lines on the Pajares Pass. Everything else will later be tied to them: the forest around each tower, the slope it stands on, the distance to the wire.

## How a statistician approaches any task

Before we open the file, it helps to know where we are in the work. Statisticians describe any work with data as a cycle of five steps. It's called PPDAC, after the first letters of the English words:

1. **Problem.** What do we want to find out?
2. **Plan.** What data do we need for that, and how will we check it?
3. **Data.** We collect it, open it and understand what's in it.
4. **Analysis.** Tables, charts, calculations.
5. **Conclusion.** The answer to the question, and what the data can't tell us.

The most common beginner's mistake is to jump straight to step four and start calculating. But if we haven't understood what each column means, any calculation can turn out to be meaningless. Remember the steelworks in the prologue that turned out to be the 'main fire hotspot'? That's exactly what happens when we skip step three.

Today we're on step three: we open the table and work out what's in it.

## What we want to know

The question for this lesson is simple: what's in the tower table, and can we work with it?

We already know a few things about the corridor. It has five line sections, the towers stand in the mountains, and 400 kV towers are usually a few dozen metres tall. So we expect to see:

- about thirty rows, one row per tower;
- coordinates in metres;
- tower heights of roughly 25–40 m.

If we see something very different – say, an 80 m tower or empty coordinates – then there's an error somewhere, or a special case, and we'll need to look into it.

## Data

- **Tower table** `powerline_reference_east400_towers.csv` – 33 towers in the eastern corridor of the 400 kV lines on the Pajares Pass. The tower positions come from OpenStreetMap and were checked by hand against PNOA orthophotos and lidar data in October 2026. This is derived data: © OpenStreetMap contributors (ODbL); «PNOA cedido por © Instituto Geográfico Nacional».

:::{admonition} Your data
Any CSV table where one row is one object will do: the towers of your own line, boreholes, survey points. All we need to change is the file path in the code below.
:::

## Step 1. Setting up our workspace

We work in VS Code with the `field-to-code-statistics` environment. It already has all the libraries we'll need.

1. In VS Code, we open the project folder: **File → Open Folder…** → `field-to-code-statistics`.
2. In the `code` folder, we create a new file, `ch01_first_look.py`.
3. We choose the environment: **Cmd+Shift+P** → **Python: Select Interpreter** → `field-to-code-statistics`.

We'll run the code bit by bit, in cells. A cell starts with the line `# %%`. Above it, VS Code shows a **Run Cell** button. We click it, and the result appears on the right, in the **Interactive** window. This makes it easy to look at the data step by step instead of running the whole file at once.

:::{admonition} Your data
If we don't have the environment yet, we can set it up in a few minutes.

1. We install conda – a program that installs Python and libraries and keeps them separate for each project. The easiest way is to install Miniforge: https://conda-forge.org/download/
2. We make one folder for the whole project, for example `my-project`, and inside it a `data` folder for the data and a `code` folder for scripts. We keep all the project files here and only here, so the paths in the code don't break.
3. In Terminal, we create an environment with the libraries we need and switch it on:

   ```bash
   conda create -n my-project -c conda-forge python=3.12 pandas ipykernel
   conda activate my-project
   ```

   pandas is enough for this lesson, and `ipykernel` lets VS Code run the cells. The full list of libraries for this book is in the `environment.yml` file in the book's repository. Everything installs with a single command: `conda env create -f environment.yml`.
4. In VS Code, we install Microsoft's **Python** and **Jupyter** extensions (the **Extensions** tab) and choose our environment with **Python: Select Interpreter**.
:::

## Step 2. Bringing in pandas

For tables in Python, almost everyone uses the pandas library. It's the standard in data analysis and in geospatial companies. Its heart is a table called a DataFrame. It's easiest to think of it as an Excel sheet that Python understands: every column has a name, and every row has a number.

```python
# %%
from pathlib import Path
import pandas as pd
```

- `from pathlib import Path` – a tool for working with file paths. With it, we write a path the same way on Mac, Windows and Linux.
- `import pandas as pd` – we bring in pandas under the short name `pd`. It's the standard abbreviation, used everywhere.

If the cell runs without any messages, all is well: the libraries were found.

## Step 3. Opening the table

```python
# %%
data_dir = Path.home() / "geodata" / "pajares" / "outputs"
towers_file = data_dir / "powerline_reference_east400_towers.csv"
towers = pd.read_csv(towers_file)
```

Let's go through it line by line.

- `Path.home()` is our home folder. The `/` sign between the parts joins them into a path: home folder → `geodata` → `pajares` → `outputs`. That gives us the path to the data folder, and we call it `data_dir`.
- The second line adds the file name to the folder. This is the full path to the table.
- `pd.read_csv(...)` reads the CSV file and turns it into a pandas table. We save it under the name `towers`.

CSV is a simple text format for tables: each line of the file is a row of the table, and the values are separated by commas. Any program can open it, which is why open data is almost always published as CSV.

:::{admonition} Your data
We change the path in `data_dir` and the file name in `towers_file`. If the data sits in the `data` folder inside the project folder, the path is shorter: `data_dir = Path("data")`.
:::

## Step 4. How many rows and columns

The first thing an engineer does with a new table is check its size. It's like counting the boxes when a delivery arrives.

```python
# %%
towers.shape
```

```text
(33, 28)
```

`shape` is the size of the table: first the number of rows, then the number of columns. 33 rows and 28 columns.

33 rows is exactly the number of towers in our corridor. That matches what we expected: one row, one tower. This is an important check. If there were, say, 66 rows, we'd suspect that every tower had been recorded twice.

## Step 5. Which columns there are

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

`columns` gives us the names of all the columns, and `tolist()` prints them as a plain list.

The names are short and in English. That's the convention: code never has spaces or accented letters. But a name alone doesn't always tell us what's in the column. What is `dz_dtm_mdt02`, for example? That's why the next step is the data dictionary.

## Step 6. The data dictionary

A data dictionary describes every column: what it means, what units it's in and where it comes from. Without one, we can't calculate anything. If we take a height in metres for a height in feet, or an angle in degrees for a percentage, all our conclusions will be wrong.

For our table, we put the dictionary together from the description of the line reference dataset in the project documents:

**Identifying the tower**
- `osm_node` – the tower's point number in OpenStreetMap. It's permanent, so we can always find the tower by it.
- `label` – our short name for the tower: N01…N10, A01…A05 and so on. The letter is the line section.
- `old_seq` – the row number from the first OpenStreetMap export. It's for internal use and isn't needed for the analysis.
- `lines` – which line section the tower belongs to: N, A, B, C or S. Two towers are shared by several sections, so they have more than one letter.

**Where the tower stands**
- `x`, `y` – coordinates in metres, in the ETRS89 / UTM 30N (EPSG:25830) system. It's a convenient system for measuring distances.
- `lon`, `lat` – the same points in degrees of longitude and latitude (WGS 84). We need these for web maps.
- `lidar_x`, `lidar_y` – where the tower was found in the lidar point cloud.
- `dist_osm_lidar_m` – the distance between the OpenStreetMap point and the lidar point, in metres.
- `lidar_note` – a note if the tower couldn't be found in the lidar.

**Heights**
- `z_base_mdt02` – the ground height at the foot of the tower from the national elevation model MDT02, in metres above sea level.
- `z_base_dtm_cyl` – the same, from our own ground model built from the 2025 lidar.
- `dz_dtm_mdt02` – the difference between these two heights, in metres. It shows how well the two ground models agree.
- `height_ndsm_m` – the height of the tower itself above the ground, from the lidar, in metres.

**The tower and the terrain**
- `slope_deg` – the slope of the ground at the tower, in degrees.
- `bend_deg` – how many degrees the line turns at this tower.
- `anchor_candidate` – this may be an anchor tower, where the wire is fixed rigidly, usually at a bend. The values are `True` (yes) or `False` (no).
- `anchor_reason` – why we think so.
- `rlat_zone` – the altitude zone from the regulations for high-voltage lines: A, B or C. In zone C, above 1000 m, the regulations allow for ice on the wires.
- `dtm_interpolated` – 1 if we had to fill in the ground height at the tower because there were no ground points beneath it; 0 if not.

**Housekeeping notes**
- `lidar_sheet` – the PNOA lidar sheet the tower is on.
- `surveys` – which surveys cover the tower: CYL is Castilla y León 2025, AST is Asturias 2024.
- `inside_corridor` – the tower is inside the corridor within 100 m of the wires (`True` or `False`).
- `control_section` – the tower is on the control section, where we check everything by hand (`True` or `False`).
- `verified` – who checked the tower, when and how.
- `screenshot` – the path to the screenshot of the check.

We can see that the columns come in different kinds: names and notes, numbers in metres and degrees, yes-or-no answers. These are different **types of variable**, and the type decides what we can do with them.

:::{admonition} Your data
A description of the columns almost always sits next to the data:

- on the websites where we download open data, in a description or metadata file (for IGN and CNIG, in the dataset's documentation section; for NASA FIRMS, in the description of the archive's fields; for OpenStreetMap, on the wiki, which explains every tag);
- in the data folder, as `README` or `readme.txt` files, or a PDF with a description.

If there's no description, we ask whoever gave us the data. And until we get an answer, we write our own dictionary: we look at the values in each column and honestly mark what we're not sure about.
:::

## Step 7. The first rows

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

`head()` shows the first five rows. But 28 columns don't fit on the screen, so pandas hides the middle behind an ellipsis, `...`. So we pick just the columns we need:

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

The double square brackets are a list of the column names we want to see. The outer brackets say 'select from the table', and the inner ones say 'here's the list'.

On the left are the row numbers: pandas counts from zero, so the first tower is number 0.

## What we found

Let's compare this with what we expected:

- **33 rows** – one per tower. That matches.
- **Coordinates in metres:** x is around 274,000 and y around 4,766,000. These are metres in the UTM 30N system, not degrees. That matches.
- **Tower heights** in the first rows run from 22.6 to 36.1 m. That mostly matches. Only N05, at 22.6 m, is lower than we expected. We'll keep that in mind.
- **Slopes** from 7.5 to 25.2 degrees – mountain terrain, just as it should be.

The table looks fit to work with. But we've only looked at five rows out of 33.

## If something doesn't work

- **`FileNotFoundError`** – Python couldn't find the file. It's almost always a typo in the path, or the file is in a different folder. We check the path: we print `towers_file` and compare it with where the file actually is in Finder.
- **`ModuleNotFoundError: No module named 'pandas'`** – the wrong environment is selected. We go back to **Python: Select Interpreter** → `field-to-code-statistics`.
- **There's no Run Cell button** – Microsoft's Python and Jupyter extensions aren't installed in VS Code. We install them in the **Extensions** tab.

## Summary

**New concepts**
- **The PPDAC cycle** – the five steps of any work with data: problem, plan, data, analysis, conclusion. Example: today we're on the 'data' step.
- **Table (DataFrame)** – a pandas table where the columns have names and the rows have numbers. Example: `towers`.
- **Data dictionary** – a description of every column: meaning, units, source. Example: `height_ndsm_m` is the height of the tower above the ground, in metres.
- **Table size** – the number of rows and columns. Example: `(33, 28)`.

**New code**

```python
import pandas as pd                       # connect pandas
towers = pd.read_csv("towers.csv")        # open a CSV table
towers.shape                              # number of rows and columns
towers.columns.tolist()                   # list of column names
towers.head()                             # first five rows
towers[["label", "height_ndsm_m"]]        # only the columns we need
```

**Key points**
- Before we calculate anything, we check the size of the table and put together a data dictionary.
- One row, one object. Here, one row is one tower.

## Questions for an engineer

1. Why did we check that there were exactly 33 rows, instead of going straight to the calculations?

   :::{dropdown} Answer

   It's a check that one row is one tower. If any towers were repeated or missing, every calculation that followed – the average height, the number of towers on steep slopes – would be wrong.
   :::

2. Why do we need a data dictionary, when the column names already give us a hint?

   :::{dropdown} Answer

   A name tells us neither the units, nor the source, nor the exact meaning. We can't make sense of `dz_dtm_mdt02` without the dictionary, for example. And mixed-up units or meanings make any conclusion wrong.
   :::

3. In the first rows, tower N05 is 22.6 m tall, while the others are around 30 m. What should we do about it now?

   :::{dropdown} Answer

   For now, we don't change or delete anything. It's a reason to take a closer look. Perhaps the tower really is lower, or perhaps the lidar didn't pick it up well. We decide only once we've got to the bottom of it.
   :::

## Exercises

1. Which pandas command opens a CSV table?

2. Complete the code to find out how many rows and columns the table has: `towers.____`

3. Which three kinds of spatial data do we come across on the Pajares Pass?

[Answers](#en-ch01-l01)

## The question that remains open

The five rows look good. But what about the other 28? Are there empty values or strange numbers? For example, is there a tower whose height is very different from the others?

## Sources

- Tower table: reference dataset for the eastern corridor of the 400 kV lines, Pajares project, checked 17.10.2026; © OpenStreetMap contributors (ODbL); «PNOA cedido por © Instituto Geográfico Nacional».
- pandas: https://pandas.pydata.org
- Miniforge (conda): https://conda-forge.org/download/

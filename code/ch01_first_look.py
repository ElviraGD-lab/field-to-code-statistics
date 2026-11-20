# Chapter 1. How to open any data
# Lesson 1. Opening the tower table
# Data: 400 kV tower reference of the eastern corridor, Pajares pass
#   powerline_reference_east400_towers.csv
#   © OpenStreetMap contributors (ODbL); PNOA cedido por © Instituto Geografico Nacional
# Run cell by cell in VS Code (Run Cell above each "# %%").

# %%
from pathlib import Path
import pandas as pd

# %%
# Path to the data folder: change it for your own data
data_dir = Path.home() / "geodata" / "pajares" / "outputs"
towers_file = data_dir / "powerline_reference_east400_towers.csv"
towers = pd.read_csv(towers_file)

# %%
# Size of the table: (rows, columns)
towers.shape

# %%
# Names of all columns
towers.columns.tolist()

# %%
# First five rows (wide tables are cut with "...")
towers.head()

# %%
# Only the columns we need
towers[["label", "lines", "x", "y", "slope_deg", "height_ndsm_m"]].head()

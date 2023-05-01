"""Apresente o nome do ator/atriz com a maior média por filme."""

import numpy as np
import pandas as pd



df = pd.read_csv('actors.csv')
df2 = df["Average per Movie"].max()
df3 = df.loc[df["Average per Movie"] == df2, "Actor"]
df3 = df3.to_string(index=False)
print(df3)
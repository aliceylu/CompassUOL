"""Identifique o ator/atriz com maior número de filmes e o respectivo número de filmes."""

import numpy as np
import pandas as pd



df = pd.read_csv('actors.csv')

df2 = df["Number of Movies"].max()

df3 = df.loc[df["Number of Movies"] == df2, "Actor"]

df3 = df3.to_string(index=False)

print(df3, df2)
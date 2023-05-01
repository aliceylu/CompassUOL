"""Apresente o nome do(s) filme(s) mais frequente(s) e sua respectiva frequência."""

import numpy as np
import pandas as pd

df = pd.read_csv('actors.csv')
df2 = df['#1 Movie'].value_counts()
print(df2.head(1))
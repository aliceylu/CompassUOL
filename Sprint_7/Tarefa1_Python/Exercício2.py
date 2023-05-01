"""Apresente a média da coluna contendo o número de filmes."""



import numpy as np
import pandas as pd


df = pd.read_csv('actors.csv')
df2 = df["Number of Movies"].mean()
print(df2)
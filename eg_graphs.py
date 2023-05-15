from gragh_gen import graph

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('./data/eg_midsem.csv', on_bad_lines='skip')
df.rename(columns={'Total(70)':'Marks'}, inplace=True)
df.rename(columns={'ID NO':'ID'}, inplace=True)
df.dropna(subset=['Marks'], inplace=True)
print(df.head())

g = graph('EG Midsem', df, 70)
g.gen_all()
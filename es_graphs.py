from graph_gen import graph

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('./data/es_midsem.csv', on_bad_lines='skip')
df.rename(columns={'Mid-Sem':'Marks'}, inplace=True)
df.rename(columns={'ID NO':'ID'}, inplace=True)

df['Marks'] = pd.to_numeric(df['Marks'], errors='coerce').fillna(0)
df['Quiz1'] = pd.to_numeric(df['Quiz1'], errors='coerce').fillna(0)
df['Quiz2'] = pd.to_numeric(df['Quiz2'], errors='coerce').fillna(0)
print(df.head())

g = graph('ES Midsem', df, 105)
g.gen_all()
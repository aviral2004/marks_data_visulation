from graph_gen import graph

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('./data/wp_compre.csv')
df['code'] = df['ID'].str[4:6]
df['Marks'] = df['Part-I(30)'] + df['Part-II(120)']
print(df.head())

g = graph('Workshop Practice', df, 150)
g.gen_all()
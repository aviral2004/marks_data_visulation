import matplotlib.pyplot as plt
import pandas as pd
from graph_gen import graph

compre = pd.read_csv('./data/wp_compre.csv')
compre['code'] = compre['ID'].str[4:6]
compre['compre_marks'] = compre['Part-I(30)'] + compre['Part-II(120)']
compre = compre[['ID', 'Name', 'compre_marks', 'code']]

practice = pd.read_csv('./data/WP_PCT.csv')
practice.rename(columns={'Prac(150)':'practice_marks'}, inplace=True)
# take only specific columns
practice = practice[['ID', 'Name', 'practice_marks']]

# merge both dataframes
df = pd.merge(compre, practice, on=['ID', 'Name'])
df['Marks'] = df['compre_marks'] + df['practice_marks']

print(df.head())
g = graph('Workshop Practice', df, 300)
g.gen_all()

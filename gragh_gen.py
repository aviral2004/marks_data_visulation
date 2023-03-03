import matplotlib.ticker as ticker
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats
import os

import seaborn as sns
sns.set_theme()


class graph():
    def __init__(self, name, data, max_marks, path='./') -> None:
        self.df = pd.DataFrame(data)
        self.df['code'] = self.df['ID'].str[4:6]
        self.df = self.df[['ID', 'Marks', 'code']]

        self.name = name
        self.max_marks = max_marks
        self.fig_name = name.lower().replace(' ', '_')
        self.graph_path = path + 'graphs/' + self.fig_name + '/'
        self.percentiles_path = path + 'percentiles/' + self.fig_name + '/'

    def gen_hist(self, fig_size=(12, 8), hist_path=None):
        if not os.path.exists(self.graph_path):
            os.makedirs(self.graph_path)

        ax = self.df.plot.hist(column='Marks', bins=self.max_marks, grid=False,
                               figsize=fig_size, color='#86bf91', zorder=2, rwidth=0.9)
        ax.set_xlabel('Marks')
        ax.set_ylabel('Frequency')
        ax.set_title('Marks Distribution for ' + self.name)

        path = self.graph_path if hist_path is None else hist_path
        ax.figure.savefig(path + self.fig_name + '_hist' +
                          '.png', bbox_inches='tight')

    def gen_percentile_plot(self, percentile_path=None, fig_size=(10, 4), percentiles=[0.5, 0.75, 0.8, 0.9]):
        if not os.path.exists(self.graph_path):
            os.makedirs(self.graph_path)

        fig, ax = plt.subplots(figsize=fig_size)
        def fun(k): return [i/k for i in list(range(1, self.max_marks*k + 1))]

        a = fun(2)
        b = [stats.percentileofscore(
            self.df["Marks"], i, kind='weak') for i in a]
        ax.plot(a, b)

        for i, color in zip(percentiles, ['pink', 'green', 'yellow', 'red']):
            plt.axvline(x=self.df['Marks'].quantile([i]).values[0],
                        color=color, linestyle='--', label=f"{i*100: .0f}th percentile")

        ax.xaxis.set_major_locator(ticker.MultipleLocator(10))
        ax.set_ylim(0, 101)
        ax.set_xlim(0, self.max_marks)
        ax.set_xlabel("Marks")
        ax.set_ylabel("Percentile")
        ax.set_title("Percentile Plot for " + self.name)
        ax.legend()

        path = self.graph_path if percentile_path is None else percentile_path
        ax.figure.savefig(path + self.fig_name +
                          '_percentile' + '.png', bbox_inches='tight')

    def gen_quartiles(self, quartile_path=None, fig_size=(10, 7)):
        if not os.path.exists(self.graph_path):
            os.makedirs(self.graph_path)

        pivot = self.df.pivot_table(index="ID", columns='code', values='Marks')
        ax = pivot.plot(kind='box', figsize=fig_size)
        ax.set_title('Quartiles for ' + self.name)
        ax.set_xlabel('Code')
        ax.set_ylabel('Marks')

        path = self.graph_path if quartile_path is None else quartile_path
        ax.figure.savefig(path + self.fig_name +
                          '_quartiles' + '.png', bbox_inches='tight')

    def gen_percentiles(self):
        if not os.path.exists(self.percentiles_path):
            os.makedirs(self.percentiles_path)

        # empty file
        open(self.percentiles_path + self.fig_name + '.txt', 'w').close()

        with open(self.percentiles_path + self.fig_name + '.txt', 'a') as f:
            for i in range(1, self.max_marks + 1):
                p = stats.percentileofscore(self.df["Marks"], i, kind='weak')
                f.write(f"marks: {i} -> {p}\n")

    def gen_all(self):
        self.gen_hist()
        self.gen_percentile_plot()
        self.gen_quartiles()
        self.gen_percentiles()
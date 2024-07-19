import seaborn as sns
import matplotlib.pyplot as plt

fmri = sns.load_dataset('fmri')

g = sns.FacetGrid(fmri, col='subject', col_wrap=5, height=2, aspect=1.5)
g.map(sns.lineplot, 'timepoint', 'signal')

g.set_titles('{col_name}')

#g.fig.suptitle('relationship between time and signal', y=1.02)
g.figure.suptitle('relationship between time and signal', y=1.0)
g.set_axis_labels('time', 'signal')

plt.tight_layout()
plt.show()
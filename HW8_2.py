import seaborn as sns
import matplotlib.pyplot as plt


fmri = sns.load_dataset('fmri')
print (fmri)

sns.pointplot(x='timepoint', y='signal', hue ='region', data = fmri) 
plt.title('avg signal at each moment of time depending on the region')
plt.xlabel('timepoint')
plt.ylabel('avg of signal')
plt.show()
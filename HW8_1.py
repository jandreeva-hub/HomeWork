import seaborn as sns
import matplotlib.pyplot as plt


fmri = sns.load_dataset('fmri')
#print(fmri)

fmri = fmri[fmri['timepoint']==5]
print (fmri.head())


sns.barplot(x='event', y='signal', data = fmri) 
plt.title('event type effect at timepiont 5')
plt.xlabel('type effect')
plt.ylabel('avg of signal')
plt.show()





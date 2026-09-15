#!/usr/bin/env python
# coding: utf-8

# In[14]:


# import pandas lib as pd
import pandas as pd
import os


path = "/home/amrita/Downloads/"
os.chdir(path)


# read by default 1st sheet of an excel file
dataframe1 = pd.read_excel('MnCatForGraph.xlsx')

print(dataframe1)


# In[15]:


print(dataframe1.columns)


# In[16]:


import seaborn as sns
import matplotlib.pyplot as plt


# In[18]:


# create grouped boxplot
ax = sns.barplot(x = dataframe1['PDB'],
			y = dataframe1['BSA'],
			hue = dataframe1['InterfaceType'],palette = 'husl')
#sns.move_legend(ax, "upper left", title='Types')
#plt.show()

sns.move_legend(ax, "lower center", bbox_to_anchor=(.5, 1), ncol=2, title=None, frameon=False)
plt.setp(ax.get_legend().get_texts(), fontsize='20') 
plt.yticks(fontsize = 15,weight='bold') 
plt.xticks(fontsize = 15,weight='bold') 
plt.show()


# In[19]:


# create grouped boxplot
ax = sns.barplot(x = dataframe1['PDB'],
			y = dataframe1['InterfaceResidues'],
			hue = dataframe1['InterfaceType'],palette = 'husl')
#sns.move_legend(ax, "upper left", title='Types')
#plt.show()

sns.move_legend(ax, "lower center", bbox_to_anchor=(.5, 1), ncol=2, title=None, frameon=False)
plt.setp(ax.get_legend().get_texts(), fontsize='20') 
plt.yticks(fontsize = 15,weight='bold') 
plt.xticks(fontsize = 15,weight='bold') 
plt.show()


# In[20]:


# create grouped boxplot
ax = sns.barplot(x = dataframe1['PDB'],
			y = dataframe1['InterfaceAtoms'],
			hue = dataframe1['InterfaceType'],palette = 'husl')
#sns.move_legend(ax, "upper left", title='Types')
#plt.show()

sns.move_legend(ax, "lower center", bbox_to_anchor=(.5, 1), ncol=2, title=None, frameon=False)
plt.setp(ax.get_legend().get_texts(), fontsize='20') 
plt.yticks(fontsize = 15,weight='bold') 
plt.xticks(fontsize = 15,weight='bold') 
plt.show()


# In[21]:


# create grouped boxplot
ax = sns.barplot(x = dataframe1['PDB'],
			y = dataframe1['LocalAtomicDensity'],
			hue = dataframe1['InterfaceType'],palette = 'husl')
#sns.move_legend(ax, "upper left", title='Types')
#plt.show()

sns.move_legend(ax, "lower center", bbox_to_anchor=(.5, 1), ncol=2, title=None, frameon=False)
plt.setp(ax.get_legend().get_texts(), fontsize='20') 
plt.yticks(fontsize = 15,weight='bold') 
plt.xticks(fontsize = 15,weight='bold') 
plt.show()


# In[15]:


# import pandas lib as pd
import pandas as pd
import os


path = "/home/amrita/Downloads/"
os.chdir(path)


# read by default 1st sheet of an excel file
dataframe1 = pd.read_excel('ComparisonMnCatFerritin.xlsx')

print(dataframe1)


# In[16]:


MnCatFerritinDeltaG


# In[17]:


import seaborn as sns
import matplotlib.pyplot as plt


# In[28]:


# create grouped boxplot
ax = sns.barplot(x = dataframe1['MnCatType'],
			y = dataframe1['BSA'],
			hue = dataframe1['InterfaceType'],palette = 'husl')
#sns.move_legend(ax, "upper left", title='Types')
#plt.show()

sns.move_legend(ax, "lower center", bbox_to_anchor=(.5, 1), ncol=2, title=None, frameon=False)
plt.setp(ax.get_legend().get_texts(), fontsize='20') 
plt.yticks(fontsize = 15,weight='bold') 
plt.xticks(fontsize = 8,weight='bold') 
plt.show()


# In[22]:


# create grouped boxplot
ax = sns.barplot(x = dataframe1['MnCatType'],
			y = dataframe1['Residues'],
			hue = dataframe1['InterfaceType'],palette = 'husl')
#sns.move_legend(ax, "upper left", title='Types')
#plt.show()

sns.move_legend(ax, "lower center", bbox_to_anchor=(.5, 1), ncol=2, title=None, frameon=False)
plt.setp(ax.get_legend().get_texts(), fontsize='20') 
plt.yticks(fontsize = 15,weight='bold') 
plt.xticks(fontsize = 8,weight='bold') 
plt.show()


# In[23]:


# create grouped boxplot
ax = sns.barplot(x = dataframe1['MnCatType'],
			y = dataframe1['LocalAtomicDensity'],
			hue = dataframe1['InterfaceType'],palette = 'husl')
#sns.move_legend(ax, "upper left", title='Types')
#plt.show()

sns.move_legend(ax, "lower center", bbox_to_anchor=(.5, 1), ncol=2, title=None, frameon=False)
plt.setp(ax.get_legend().get_texts(), fontsize='20') 
plt.yticks(fontsize = 15,weight='bold') 
plt.xticks(fontsize = 8,weight='bold') 
plt.show()


# In[25]:


# create grouped boxplot
ax = sns.barplot(x = dataframe1['MnCatType'],
			y = dataframe1['Atoms'],
			hue = dataframe1['InterfaceType'],palette = 'husl')
#sns.move_legend(ax, "upper left", title='Types')
#plt.show()

sns.move_legend(ax, "lower center", bbox_to_anchor=(.5, 1), ncol=2, title=None, frameon=False)
plt.setp(ax.get_legend().get_texts(), fontsize='20') 
plt.yticks(fontsize = 15,weight='bold') 
plt.xticks(fontsize = 8,weight='bold') 
plt.show()


# In[26]:


# create grouped boxplot
ax = sns.barplot(x = dataframe1['MnCatType'],
			y = dataframe1['DeltaG(int)'],
			hue = dataframe1['InterfaceType'],palette = 'husl')
#sns.move_legend(ax, "upper left", title='Types')
#plt.show()

sns.move_legend(ax, "lower center", bbox_to_anchor=(.5, 1), ncol=2, title=None, frameon=False)
plt.setp(ax.get_legend().get_texts(), fontsize='20') 
plt.yticks(fontsize = 15,weight='bold') 
plt.xticks(fontsize = 8,weight='bold') 
plt.show()


# In[1]:


import pandas as pd
import os


path = "/home/amrita/Downloads/"
os.chdir(path)


# read by default 1st sheet of an excel file
dataframe2 = pd.read_excel('MnCatFerritinDeltaG.xlsx')

print(dataframe2)


# In[2]:


print(dataframe2.columns)


# In[3]:


import seaborn as sns
import matplotlib.pyplot as plt


# In[7]:


# create grouped boxplot
ax = sns.barplot(x = dataframe2['MnCatType'],
			y = dataframe2['DeltaGass'],
			hue = dataframe2['MnCatType'],palette=['pink', 'hotpink', 'purple'])
#sns.move_legend(ax, "upper left", title='Types')
#plt.show()

sns.move_legend(ax, "lower center", bbox_to_anchor=(.5, 1), ncol=2, title=None, frameon=False)
plt.setp(ax.get_legend().get_texts(), fontsize='20') 
plt.yticks(fontsize = 15,weight='bold') 
plt.xticks(fontsize = 8,weight='bold') 
plt.show()


# In[8]:


import pandas as pd
import os


path = "/home/amrita/Downloads/"
os.chdir(path)


# read by default 1st sheet of an excel file
dataframe3 = pd.read_excel('MnCatFerritinDeltaG(1).xlsx')

print(dataframe3)


# In[9]:


print(dataframe3.columns)


# In[11]:


# create grouped boxplot
ax = sns.barplot(x = dataframe3['MnCatType'],
			y = dataframe3['Round(DeltaGperSubunit)'],
			hue = dataframe3['MnCatType'],palette=['pink', 'hotpink', 'purple'])
#sns.move_legend(ax, "upper left", title='Types')
#plt.show()

sns.move_legend(ax, "lower center", bbox_to_anchor=(.5, 1), ncol=2, title=None, frameon=False)
plt.setp(ax.get_legend().get_texts(), fontsize='20') 
plt.yticks(fontsize = 15,weight='bold') 
plt.xticks(fontsize = 8,weight='bold') 
plt.show()


# In[3]:


import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt


path = "/home/amrita/Downloads/"
os.chdir(path)


# read by default 1st sheet of an excel file
dataframe7 = pd.read_excel('CentreOfMass2.xlsx')

print(dataframe7)


# In[6]:


# create grouped boxplot
ax = sns.barplot(x = dataframe7['ProteinType'],
			y = dataframe7['Dist'],
			hue = dataframe7['ProteinType'],palette=['pink', 'hotpink', 'purple'])
#sns.move_legend(ax, "upper left", title='Types')
#plt.show()

sns.move_legend(ax, "lower center", bbox_to_anchor=(.5, 1), ncol=2, title=None, frameon=False)
plt.setp(ax.get_legend().get_texts(), fontsize='20') 
plt.yticks(fontsize = 15,weight='bold') 
plt.xticks(fontsize = 10,weight='bold') 
plt.show()


# In[15]:


import pandas as pd
import os


path = "/home/amrita/Downloads/"
os.chdir(path)


# read by default 1st sheet of an excel file
dataframe4 = pd.read_excel('ComparisonMnCatFerritin(2).xlsx')

print(dataframe4)


# In[16]:


print(dataframe4.columns)


# In[17]:


# create grouped boxplot
ax = sns.barplot(x = dataframe4['MnCatType'],
			y = dataframe4['MinusRound'],
			hue = dataframe4['InterfaceType'],palette = 'husl')
#sns.move_legend(ax, "upper left", title='Types')
#plt.show()

sns.move_legend(ax, "lower center", bbox_to_anchor=(.5, 1), ncol=2, title=None, frameon=False)
plt.setp(ax.get_legend().get_texts(), fontsize='20') 
plt.yticks(fontsize = 15,weight='bold') 
plt.xticks(fontsize = 8,weight='bold') 
plt.show()


# In[4]:


import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt

path = "/home/amrita/Downloads/"
os.chdir(path)


# read by default 1st sheet of an excel file
dataframe4 = pd.read_excel('MnCatHbondGraph.xlsx')

print(dataframe4)


# In[5]:


print(dataframe4.columns)


# In[6]:


# create grouped boxplot
ax = sns.barplot(x = dataframe4['Type'],
			y = dataframe4['H-bond'],
			hue = dataframe4['InterfaceType'],palette = 'husl')
#sns.move_legend(ax, "upper left", title='Types')
#plt.show()

sns.move_legend(ax, "lower center", bbox_to_anchor=(.5, 1), ncol=2, title=None, frameon=False)
plt.setp(ax.get_legend().get_texts(), fontsize='20') 
plt.yticks(fontsize = 15,weight='bold') 
plt.xticks(fontsize = 8,weight='bold') 
plt.show()


# In[22]:


import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt

path = "/home/amrita/Downloads/"
os.chdir(path)


# read by default 1st sheet of an excel file
dataframe10 = pd.read_excel('ComparisonMnCatFerritin2(1).xlsx')

print(dataframe10)


# In[23]:


dataframe10["concat"] = dataframe10['MnCatType'].astype(str) +"-"+ dataframe10["InterfaceType"]


# In[24]:


print(dataframe10)


# In[25]:


colors = ['#f26b8a','#fda4ba','#fc46aa','#636363','#949292ff','#bdbdbd','#38761dff','#69dc38ff','#b7e3a4ff','#8b008b','#b47ee5','#9e7bb3']


# In[26]:


print(dataframe10.columns)



# In[27]:


# create grouped boxplot
ax = sns.barplot(x = dataframe10['MnCatType'],
			y = dataframe10['BSA'],
			hue = dataframe10['concat'],palette=colors,width=3)
plt.xticks(visible=False)
plt.gca().set_xticklabels([])
plt.legend(bbox_to_anchor=(1, 1.07), loc=2)
#sns.move_legend(ax, "upper left", bbox_to_anchor=(.5, 1), ncol=2, title=None, frameon=False)
plt.setp(ax.get_legend().get_texts(), fontsize='15') 
plt.yticks(fontsize = 15,weight='bold') 
#sns.move_legend(ax, "upper left", title='Types')
#plt.show()
for i, bar in enumerate(ax.patches):
    # Get the height of each bar and its position
    height = bar.get_height()
    x_position = bar.get_x() + bar.get_width() / 2
    # Get the standard deviation value for the bar
    std_dev = dataframe10['StdDevp BSA'].iloc[i]  # Make sure this matches the indexing of the dataframe
    # Add error bar for each bar
    ax.errorbar(x_position, height, yerr=std_dev, fmt='o', color='k', alpha=0.5)
sns.move_legend(ax, "upper left", bbox_to_anchor=(.5, 1), ncol=2, title=None, frameon=False)
plt.setp(ax.get_legend().get_texts(), fontsize='20') 
plt.yticks(fontsize = 15,weight='bold') 
#plt.xticks(fontsize = 8,weight='bold') 
plt.show()


# In[ ]:


# create grouped boxplot
ax = sns.barplot(x = dataframe10['MnCatType'],
			y = dataframe10['LD'],
			hue = dataframe10['concat'],palette=colors,width=2.2)
plt.xticks(visible=False)
plt.gca().set_xticklabels([])
plt.legend().remove()

#sns.move_legend(ax, "upper left", bbox_to_anchor=(.5, 1), ncol=2, title=None, frameon=False)
#plt.setp(ax.get_legend().get_texts(), fontsize='5') 
plt.yticks(fontsize = 15,weight='bold')
#sns.move_legend(ax, "upper left", title='Types')
#plt.show()
for i, bar in enumerate(ax.patches):
    # Get the height of each bar and its position
    height = bar.get_height()
    x_position = bar.get_x() + bar.get_width() / 2
    # Get the standard deviation value for the bar
    std_dev = dataframe10['StdDevp LD'].iloc[i]  # Make sure this matches the indexing of the dataframe
    # Add error bar for each bar
    ax.errorbar(x_position, height, yerr=std_dev, fmt='o', color='k', alpha=0.5)
 
#plt.xticks(fontsize = 8,weight='bold') 
plt.show()


# In[ ]:


# create grouped boxplot
ax = sns.barplot(x = dataframe10['MnCatType'],
			y = dataframe10['DeltaG(int)'],
			hue = dataframe10['concat'],palette=colors,width=3.5)
plt.xticks(visible=False)
plt.gca().set_xticklabels([])
plt.legend().remove()
#sns.move_legend(ax, "upper left", title='Types')
#plt.show()
#plt.legend(ax, loc='lower right')
#sns.move_legend(ax, "lower left", bbox_to_anchor=(.5, 1), ncol=2, title=None, frameon=False)
#plt.setp(ax.get_legend().get_texts(), fontsize='15') 
plt.yticks(fontsize = 15,weight='bold') 
#plt.xticks(fontsize = 8,weight='bold') 
for i, bar in enumerate(ax.patches):
    # Get the height of each bar and its position
    height = bar.get_height()
    x_position = bar.get_x() + bar.get_width() / 2
    # Get the standard deviation value for the bar
    std_dev = dataframe10['StdDev DeltaG'].iloc[i]  # Make sure this matches the indexing of the dataframe
    # Add error bar for each bar
    ax.errorbar(x_position, height, yerr=std_dev, fmt='o', color='k', alpha=0.5)
plt.show()


# In[ ]:


import seaborn as sns
import matplotlib.pyplot as plt

# Create the plot with reduced gap between grouped bars
plt.figure(figsize=(12, 6))  # Adjust the figure size
ax = sns.barplot(x=dataframe10['MnCatType'], 
                 y=dataframe10['ROUND'], 
                 hue=dataframe10['concat'], 
                 palette=colors, 
                 width=1.0,  # Thinner bars
                 dodge=True)  # Bars grouped by hue (category)

# Remove x-tick labels and legend
plt.xticks(visible=False)
plt.gca().set_xticklabels([])
plt.legend().remove()

# Adjust y-ticks fontsize
plt.yticks(fontsize=15, weight='bold')

# Adjust the spacing between groups to reduce gaps
plt.subplots_adjust(left=0.08, right=0.92)  # Fine-tune the left/right spacing

# Show the plot
plt.show()


# In[8]:


# create grouped boxplot
plt.figure(figsize=(10, 6))
ax = sns.barplot(x = dataframe10['MnCatType'],
			y = dataframe10['DeltaG(int)/BSA'],
			hue = dataframe10['concat'],palette=colors,width=0.9)
plt.xticks(visible=False)
plt.ylim(-0.040,-0.010) 
plt.gca().set_xticklabels([])
plt.legend().remove()
#sns.move_legend(ax, "upper left", title='Types')
#plt.show()

#sns.move_legend(ax, "lower center", bbox_to_anchor=(.5, 1), ncol=2, title=None, frameon=False)
#plt.setp(ax.get_legend().get_texts(), fontsize='20') 
plt.yticks(fontsize = 15,weight='bold') 
#plt.xticks(fontsize = 8,weight='bold') 

plt.show()


# In[9]:


# import pandas lib as pd
import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


path = "/home/amrita/Downloads/"
os.chdir(path)


# read by default 1st sheet of an excel file
dataframe11 = pd.read_excel('MnCatFerritinDeltaGass.xlsx')

print(dataframe11)


# In[ ]:


colors = ['pink','grey','purple']


# In[10]:


# create grouped boxplot
plt.figure(figsize=(5,4))
#ax = sns.barplot(x = dataframe1['A'],y = dataframe1['C'],hue = dataframe1['A'],palette = colors,width=o.8)

n=len(dataframe11['MnCatType'])

# Positions for the bars
x_pos = np.arange(n)  # Default positions

# Reduce the gap by modifying positions manually
# Adjust the width between the bars by setting a smaller spacing (e.g., smaller interval)
ax=plt.bar(x_pos, dataframe11['DeltaGass'],color = colors, width=0.5)  # Width of bars remains the same
plt.xticks(x_pos, dataframe11['MnCatType'])  # Set the x-axis ticks to correspond to the categories
plt.ylim(-300,0)

#sns.move_legend(ax, "upper left", title='Types')
#plt.show()
plt.yticks(fontsize = 12,weight='bold')
#plt.xticks(fontsize = 15,weight='bold')
#sns.move_legend(ax, "lower center", bbox_to_anchor=(.5,1), ncol=2, title=None, frameon=False)
#plt.setp(ax.get_legend().get_texts(), fontsize='15')
plt.show()


# In[70]:


# create grouped boxplot
ax = sns.barplot(x = dataframe11['MnCatType'],
			y = dataframe11['DeltaGass'],
			hue = dataframe11['MnCatType'],color = 'terrain', palette = [ 'tab:pink','tab:grey','tab:purple'], width=1.5)
#sns.move_legend(ax, "upper left", title='Types')
#plt.show()
ax.set_ylim(ymin=-100, ymax=-300)
plt.yticks(fontsize = 15,weight='bold')
#plt.xticks(fontsize = 12,weight='bold')
sns.move_legend(ax, "lower center", bbox_to_anchor=(.5,1), ncol=2, title=None, frameon=False)
plt.setp(ax.get_legend().get_texts(), fontsize='15') 
plt.show()


# In[1]:


# import pandas lib as pd
import pandas as pd
import os


path = "/home/amrita/Downloads/"
os.chdir(path)


# read by default 1st sheet of an excel file
dataframe1 = pd.read_excel('MnCatNPbyPratio.xlsx')

print(dataframe1)


# In[2]:


import seaborn as sns
import matplotlib.pyplot as plt


# In[3]:


colors = ['pink','grey','purple']


# In[5]:


# create grouped boxplot
plt.figure(figsize=(10, 6))
ax = sns.barplot(x = dataframe1['Location'],
			y = dataframe1['NP/Pratio'],
			hue = dataframe1['ProteinType'],palette = colors,width=0.5)
#sns.move_legend(ax, "upper left", title='Types')
#plt.show()
#plt.ylim(0.5-1.5)
plt.yticks(fontsize = 15,weight='bold')
plt.xticks(fontsize = 20,weight='bold')
sns.move_legend(ax, "lower center", bbox_to_anchor=(.5,1), ncol=2, title=None, frameon=False)
plt.setp(ax.get_legend().get_texts(), fontsize='15') 
plt.show()


# In[17]:


# import pandas lib as pd
import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


path = "/home/amrita/Downloads/"
os.chdir(path)


# read by default 1st sheet of an excel file
dataframe13 = pd.read_excel('MnCatDeltaGassWithStdDev(1).xlsx')

print(dataframe13)


# In[18]:


colors = ['pink','grey','green','purple']


# In[19]:


# create grouped boxplot
plt.figure(figsize=(5,4))
#ax = sns.barplot(x = dataframe1['A'],y = dataframe1['C'],hue = dataframe1['A'],palette = colors,width=o.8)

n=len(dataframe13['MnCatType'])

# Positions for the bars
x_pos = np.arange(n)  # Default positions

# Reduce the gap by modifying positions manually
# Adjust the width between the bars by setting a smaller spacing (e.g., smaller interval)
ax=plt.bar(x_pos, dataframe13['Average'],color =colors, width=0.5)  # Width of bars remains the same
for i, bar in enumerate(ax.patches):
    # Get the height of each bar and its position
    height = bar.get_height()
    x_position = bar.get_x() + bar.get_width() / 2
    # Get the standard deviation value for the bar
    std_dev = dataframe13['StdDev'].iloc[i]  # Make sure this matches the indexing of the dataframe
    # Add error bar for each bar
    ax.errorbar(x_position, height, yerr=std_dev, fmt='o', color='k', alpha=0.5)
plt.xticks(x_pos, dataframe13['MnCatType'])  # Set the x-axis ticks to correspond to the categories
plt.ylim(-300,0)

#sns.move_legend(ax, "upper left", title='Types')
#plt.show()
plt.yticks(fontsize = 12,weight='bold')
#plt.xticks(fontsize = 15,weight='bold')
#sns.move_legend(ax, "lower center", bbox_to_anchor=(.5,1), ncol=2, title=None, frameon=False)
#plt.setp(ax.get_legend().get_texts(), fontsize='15')
plt.show()


# In[ ]:


# create grouped boxplot
ax = sns.barplot(x = dataframe13['MnCatType'],
			y = dataframe13['Average'],color=colors)
plt.xticks(visible=False)
plt.gca().set_xticklabels([])
#sns.move_legend(ax, "upper left", title='Types')
#plt.show()
#plt.legend(ax, loc='lower right')
#sns.move_legend(ax, "lower left", bbox_to_anchor=(.5, 1), ncol=2, title=None, frameon=False)
plt.setp(ax.get_legend().get_texts(), fontsize='15') 
plt.yticks(fontsize = 15,weight='bold') 
#plt.xticks(fontsize = 8,weight='bold') 
for i, bar in enumerate(ax.patches):
    # Get the height of each bar and its position
    height = bar.get_height()
    x_position = bar.get_x() + bar.get_width() / 2
    # Get the standard deviation value for the bar
    std_dev = dataframe13['StdDev'].iloc[i]  # Make sure this matches the indexing of the dataframe
    # Add error bar for each bar
    ax.errorbar(x_position, height, yerr=std_dev, fmt='o', color='k', alpha=0.5)
plt.show()


# In[20]:


import matplotlib.pyplot as plt
import numpy as np

# Example of setting up a figure and axes
fig, ax = plt.subplots(figsize=(5, 4))

n = len(dataframe13['MnCatType'])  # Number of categories
x_pos = np.arange(n)  # Positions for the bars (x-axis)

# Plot the bars
bars = ax.bar(x_pos, dataframe13['Average'], color=colors, width=0.5)

# Adding error bars
for i, bar in enumerate(bars):
    height = bar.get_height()  # Get the height of each bar
    x_position = bar.get_x() + bar.get_width() / 2  # x-position of the bar
    std_dev = dataframe13['StdDev'].iloc[i]  # Standard deviation for error bars

    # Add error bar for each bar
    ax.errorbar(x_position, height, yerr=std_dev, fmt='o', color='k', alpha=0.5)

# Set x-axis ticks to match the categories
ax.set_xticks(x_pos)
ax.set_xticklabels(dataframe13['MnCatType'])

# Set y-axis limit
ax.set_ylim(-300, 0)
plt.yticks(fontsize = 12,weight='bold')
plt.xticks(fontsize = 5,weight='bold')
# Customize the ticks' font size and weight
ax.tick_params(axis='y', labelsize=12, labelweight='bold')

# Show the plot
plt.show()


# In[ ]:


import matplotlib.pyplot as plt
import numpy as np

# Example of setting up a figure and axes
fig, ax = plt.subplots(figsize=(5, 4))

n = len(dataframe13['MnCatType'])  # Number of categories
x_pos = np.arange(n)  # Positions for the bars (x-axis)

# Plot the bars
bars = ax.bar(x_pos, dataframe13['Average'], color=colors, width=0.5)
plt.yticks(fontsize = 15,weight='bold')
# Adding error bars
for i, bar in enumerate(bars):
    height = bar.get_height()  # Get the height of each bar
    x_position = bar.get_x() + bar.get_width() / 2  # x-position of the bar
    std_dev = dataframe13['StdDev'].iloc[i]  # Standard deviation for error bars

    # Add error bar for each bar
    ax.errorbar(x_position, height, yerr=std_dev, fmt='o', color='k', alpha=0.5)

# Set x-axis ticks to match the categories
ax.set_xticks(x_pos)
ax.set_xticklabels(dataframe13['MnCatType'])

# Set y-axis limit
ax.set_ylim(-300, 0)

# Customize the ticks' font size and weight
ax.tick_params(axis='y', labelsize=12, labelweight='bold')

# Show the plot
import matplotlib.pyplot as plt
import numpy as np

# Example of setting up a figure and axes
fig, ax = plt.subplots(figsize=(5, 4))

n = len(dataframe13['MnCatType'])  # Number of categories
x_pos = np.arange(n)  # Positions for the bars (x-axis)

# Plot the bars
bars = ax.bar(x_pos, dataframe13['Average'], color=colors, width=0.5)
plt.yticks(fontsize = 15,weight='bold')
# Adding error bars
for i, bar in enumerate(bars):
    height = bar.get_height()  # Get the height of each bar
    x_position = bar.get_x() + bar.get_width() / 2  # x-position of the bar
    std_dev = dataframe13['StdDev'].iloc[i]  # Standard deviation for error bars

    # Add error bar for each bar
    ax.errorbar(x_position, height, yerr=std_dev, fmt='o', color='k', alpha=0.5)

# Set x-axis ticks to match the categories
ax.set_xticks(x_pos)
ax.set_xticklabels(dataframe13['MnCatType'])

# Set y-axis limit
ax.set_ylim(-300, 0)

# Customize the ticks' font size and weight
ax.tick_params(axis='y', labelsize=12, labelweight='bold')
plt.yticks(fontsize = 15,weight='bold')
# Show the plot
plt.show()


# In[ ]:


import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt

path = "/home/amrita/Downloads/"
os.chdir(path)


# read by default 1st sheet of an excel file
dataframe15 = pd.read_excel('MnCatHbondGraph.xlsx')

print(dataframe15)


# In[21]:


colors = ['#f26b8a','#fda4ba','#fc46aa','#636363','#949292ff','#bdbdbd','#38761dff','#69dc38ff','#b7e3a4ff','#8b008b','#b47ee5','#9e7bb3']


# In[12]:


# create grouped boxplot
plt.figure(figsize=(10, 6))
ax = sns.barplot(x = dataframe15['Type'],
			y = dataframe15['H-bond'],
			hue = dataframe15['InterfaceType'],palette=colors, width=0.95)
plt.xticks(visible=False)
plt.gca().set_xticklabels([])
#sns.move_legend(ax, "upper left", title='Types')
#plt.show()

sns.move_legend(ax, "lower center", bbox_to_anchor=(.5, 1), ncol=2, title=None, frameon=False)
plt.setp(ax.get_legend().get_texts(), fontsize='20') 
plt.yticks(fontsize = 15,weight='bold') 
#plt.xticks(fontsize = 8,weight='bold') 
plt.show()


# In[8]:


# import pandas lib as pd
import pandas as pd
import os


path = "/home/amrita/Downloads/"
os.chdir(path)


# read by default 1st sheet of an excel file
dataframe17 = pd.read_excel('MnCatDistCOMGraph.xlsx')

print(dataframe17)


# In[9]:


colors = ['pink','grey','green','purple']


# In[12]:


plt.figure(figsize=(6, 6))
ax = sns.barplot(x = dataframe17['ProteinType'],
			y = dataframe17['Dist'],
			hue = dataframe17['ProteinType'],palette = colors,width=0.8)
#sns.move_legend(ax, "upper left", title='Types')
#plt.show()
plt.ylim(5,25)
plt.yticks(fontsize = 15,weight='bold')
plt.xticks(fontsize = 10,weight='bold')
sns.move_legend(ax, "lower center", bbox_to_anchor=(.5,1), ncol=2, title=None, frameon=False)
plt.setp(ax.get_legend().get_texts(), fontsize='15') 
plt.show()


# In[1]:


import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt


path = "/home/amrita/Downloads/"
os.chdir(path)
dataframe18 = pd.read_excel('GraphMnCatCavityFeb25.xlsx')


# In[2]:


colors = ['pink','grey','green','purple']


# In[12]:


# create grouped boxplot
ax = sns.barplot(x = dataframe18['ProteinType'],
			y = dataframe18['CavitySurfaceArea'],
			hue = dataframe18['ProteinType'],palette = colors,width=0.9)
#sns.move_legend(ax, "upper left", title='Types')
#plt.show()
plt.yticks(fontsize = 15,weight='bold')
#plt.xticks(fontsize = 12,weight='bold')
sns.move_legend(ax, "lower center", bbox_to_anchor=(.5,1), ncol=2, title=None, frameon=False)
plt.setp(ax.get_legend().get_texts(), fontsize='15') 
plt.show()


# In[11]:


# create grouped boxplot
ax = sns.barplot(x = dataframe18['ProteinType'],
			y = dataframe18['CavityVolume'],
			hue = dataframe18['ProteinType'],palette = colors, width=0.9)
#sns.move_legend(ax, "upper left", title='Types')
#plt.show()
plt.yticks(fontsize = 15,weight='bold')
#plt.xticks(fontsize = 12,weight='bold')
sns.move_legend(ax, "lower center", bbox_to_anchor=(.5,1), ncol=2, title=None, frameon=False)
plt.setp(ax.get_legend().get_texts(), fontsize='15') 
plt.show()


# In[7]:


# create grouped boxplot
ax = sns.barplot(x = dataframe18['ProteinType'],
			y = dataframe18['Cavity(S/V)'],
			hue = dataframe18['ProteinType'],palette = colors,width=0.9)
#sns.move_legend(ax, "upper left", title='Types')
#plt.show()
plt.yticks(fontsize = 15,weight='bold')
#plt.xticks(fontsize = 12,weight='bold')
sns.move_legend(ax, "lower center", bbox_to_anchor=(.5,1), ncol=2, title=None, frameon=False)
plt.setp(ax.get_legend().get_texts(), fontsize='15') 
plt.ylim([0.8, 0.9])
plt.show()


# In[6]:


import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt

path = "/home/amrita/Downloads/"
os.chdir(path)


# read by default 1st sheet of an excel file
dataframe18 = pd.read_excel('MutantMnCatalase.xlsx')

print(dataframe18)


# In[7]:


colors = ['#fda4ba','#f26b8a','#fda4ba','#c51b8a']


# In[8]:


# create grouped boxplot
ax = sns.barplot(x = dataframe18['InterfaceType'],
			y = dataframe18['BSA'],
			hue = dataframe18['PDB'],palette=colors)
plt.xticks(visible=False)
plt.gca().set_xticklabels([])
#sns.move_legend(ax, "upper left", title='Types')
#plt.show()

sns.move_legend(ax, "lower center", bbox_to_anchor=(.5, 1), ncol=2, title=None, frameon=False)
plt.setp(ax.get_legend().get_texts(), fontsize='20') 
plt.yticks(fontsize = 15,weight='bold') 
#plt.xticks(fontsize = 8,weight='bold') 
plt.show()


# In[9]:


# create grouped boxplot
ax = sns.barplot(x = dataframe18['InterfaceType'],
			y = dataframe18['Ld'],
			hue = dataframe18['PDB'],palette=colors)
plt.xticks(visible=False)
plt.gca().set_xticklabels([])
#sns.move_legend(ax, "upper left", title='Types')
#plt.show()

sns.move_legend(ax, "lower center", bbox_to_anchor=(.5, 1), ncol=2, title=None, frameon=False)
plt.setp(ax.get_legend().get_texts(), fontsize='20') 
plt.yticks(fontsize = 15,weight='bold') 
#plt.xticks(fontsize = 8,weight='bold') 
plt.show()


# In[10]:


# create grouped boxplot
ax = sns.barplot(x = dataframe18['InterfaceType'],
			y = dataframe18['ddg'],
			hue = dataframe18['PDB'],palette=colors)
plt.xticks(visible=False)
plt.gca().set_xticklabels([])
#sns.move_legend(ax, "upper left", title='Types')
#plt.show()

sns.move_legend(ax, "lower center", bbox_to_anchor=(.5, 1), ncol=2, title=None, frameon=False)
plt.setp(ax.get_legend().get_texts(), fontsize='20') 
plt.yticks(fontsize = 15,weight='bold') 
#plt.xticks(fontsize = 8,weight='bold') 
plt.show()


# In[1]:


import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt


path = "/home/amrita/Downloads/"
os.chdir(path)
dataframe18 = pd.read_excel('Book 18.xlsx')


# In[2]:


colors = ['pink','grey','green','purple']


# In[3]:


# create grouped boxplot
ax = sns.barplot(x = dataframe18['ProteinType'],
			y = dataframe18['MonomerCavityVolume'],
			hue = dataframe18['ProteinType'],palette = colors,width=0.9)
#sns.move_legend(ax, "upper left", title='Types')
#plt.show()
plt.yticks(fontsize = 15,weight='bold')
#plt.xticks(fontsize = 12,weight='bold')
sns.move_legend(ax, "lower center", bbox_to_anchor=(.5,1), ncol=2, title=None, frameon=False)
plt.setp(ax.get_legend().get_texts(), fontsize='15') 
plt.show()


# In[4]:


# create grouped boxplot
ax = sns.barplot(x = dataframe18['ProteinType'],
			y = dataframe18['MonomerCavitySA'],
			hue = dataframe18['ProteinType'],palette = colors,width=0.9)
#sns.move_legend(ax, "upper left", title='Types')
#plt.show()
plt.yticks(fontsize = 15,weight='bold')
#plt.xticks(fontsize = 12,weight='bold')
sns.move_legend(ax, "lower center", bbox_to_anchor=(.5,1), ncol=2, title=None, frameon=False)
plt.setp(ax.get_legend().get_texts(), fontsize='15') 
plt.show()


# In[5]:


# create grouped boxplot
ax = sns.barplot(x = dataframe18['ProteinType'],
			y = dataframe18['ROUND'],
			hue = dataframe18['ProteinType'],palette = colors,width=0.9)
#sns.move_legend(ax, "upper left", title='Types')
#plt.show()
plt.yticks(fontsize = 15,weight='bold')
#plt.xticks(fontsize = 12,weight='bold')
sns.move_legend(ax, "lower center", bbox_to_anchor=(.5,1), ncol=2, title=None, frameon=False)
plt.setp(ax.get_legend().get_texts(), fontsize='15') 
plt.show()


# In[1]:


import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt


path = "/home/amrita/Downloads/"
os.chdir(path)
dataframe18 = pd.read_excel('MnCatCavityByProtein(3).xlsx')


# In[2]:


colors = ['pink','grey','green','purple']


# In[3]:


# create grouped boxplot
ax = sns.barplot(x = dataframe18['ProteinType'],
			y = dataframe18['C/Pround'],
			hue = dataframe18['ProteinType'],palette = colors,width=0.9)
#sns.move_legend(ax, "upper left", title='Types')
#plt.show()
plt.yticks(fontsize = 15,weight='bold')
#plt.xticks(fontsize = 12,weight='bold')
sns.move_legend(ax, "lower center", bbox_to_anchor=(.5,1), ncol=2, title=None, frameon=False)
plt.setp(ax.get_legend().get_texts(), fontsize='15') 
plt.show()


# In[4]:


print(dataframe18)


# In[6]:


# create grouped boxplot
ax = sns.barplot(x = dataframe18['ProteinType'],
			y = dataframe18['ProteinDia'],
			hue = dataframe18['ProteinType'],palette = colors,width=0.9)
#sns.move_legend(ax, "upper left", title='Types')
#plt.show()
plt.yticks(fontsize = 15,weight='bold')
#plt.xticks(fontsize = 12,weight='bold')
sns.move_legend(ax, "lower center", bbox_to_anchor=(.5,1), ncol=2, title=None, frameon=False)
plt.setp(ax.get_legend().get_texts(), fontsize='15') 
plt.show()


# In[11]:


import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt


path = "/home/amrita/Downloads/"
os.chdir(path)
dataframe18 = pd.read_excel('MnCatCavityByProtein(3).xlsx')


# In[12]:


ax = sns.barplot(x = dataframe18['ProteinType'],
			y = dataframe18['ProteinDia'],
			hue = dataframe18['ProteinType'],palette = colors,width=0.9)
#sns.move_legend(ax, "upper left", title='Types')
#plt.show()
plt.yticks(fontsize = 15,weight='bold')
#plt.xticks(fontsize = 12,weight='bold')
sns.move_legend(ax, "lower center", bbox_to_anchor=(.5,1), ncol=2, title=None, frameon=False)
plt.setp(ax.get_legend().get_texts(), fontsize='15') 
plt.show()


# In[18]:


import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt


path = "/home/amrita/Downloads/"
os.chdir(path)


# read by default 1st sheet of an excel file
dataframe7 = pd.read_excel('CavityHistogram(1).xlsx')

print(dataframe7)


# In[19]:


colors = ['pink','grey']


# In[21]:


ax = sns.barplot(x = dataframe7['Bin'],
			y = dataframe7['Count'],
			hue = dataframe7['ProteinType'],palette = colors,width=0.9)
#sns.move_legend(ax, "upper left", title='Types')
#plt.show()
plt.yticks(fontsize = 15,weight='bold')
#plt.xticks(fontsize = 12,weight='bold')
sns.move_legend(ax, "lower center", bbox_to_anchor=(.5,1), ncol=2, title=None, frameon=False)
plt.setp(ax.get_legend().get_texts(), fontsize='15') 
plt.show()


# In[13]:


import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt


path = "/home/amrita/Downloads/"
os.chdir(path)
dataframe18 = pd.read_excel('MnCatNPbyPratio.xlsx')


# In[14]:


colors = ['pink','grey','green','purple']


# In[15]:


print(dataframe18)


# In[16]:


# create grouped boxplot
ax = sns.barplot(x = dataframe18['Location'],
			y = dataframe18['NP/Pratio'],
			hue = dataframe18['ProteinType'],palette = colors,width=0.9)
#sns.move_legend(ax, "upper left", title='Types')
#plt.show()
plt.yticks(fontsize = 15,weight='bold')
#plt.xticks(fontsize = 12,weight='bold')
sns.move_legend(ax, "lower center", bbox_to_anchor=(.5,1), ncol=2, title=None, frameon=False)
plt.setp(ax.get_legend().get_texts(), fontsize='15') 
plt.show()


# In[15]:


# import pandas lib as pd
import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt

path = "/home/amrita/Downloads/"
os.chdir(path)


# read by default 1st sheet of an excel file
dataframe1 = pd.read_excel('CavityGraphMnCatalase.xlsx')

print(dataframe1)


# In[16]:


colors = ['pink','grey','green','purple']


# In[17]:


# create grouped boxplot
ax = sns.barplot(x = dataframe1['ProteinType'],
			y = dataframe1['Diameter'],
			hue = dataframe1['ProteinType'],palette = colors,width=0.9)
#sns.move_legend(ax, "upper left", title='Types')
#plt.show()
plt.yticks(fontsize = 15,weight='bold')
#plt.xticks(fontsize = 12,weight='bold')
sns.move_legend(ax, "lower center", bbox_to_anchor=(.5,1), ncol=2, title=None, frameon=False)
plt.setp(ax.get_legend().get_texts(), fontsize='15') 
plt.show()


# In[18]:


# create grouped boxplot
ax = sns.barplot(x = dataframe1['ProteinType'],
			y = dataframe1['CV/PV'],
			hue = dataframe1['ProteinType'],palette = colors,width=0.9)
#sns.move_legend(ax, "upper left", title='Types')
#plt.show()
plt.yticks(fontsize = 15,weight='bold')
#plt.xticks(fontsize = 12,weight='bold')
sns.move_legend(ax, "lower center", bbox_to_anchor=(.5,1), ncol=2, title=None, frameon=False)
plt.setp(ax.get_legend().get_texts(), fontsize='15') 
plt.show()


# In[19]:


# create grouped boxplot
ax = sns.barplot(x = dataframe1['ProteinType'],
			y = dataframe1['CSA/CV'],
			hue = dataframe1['ProteinType'],palette = colors,width=0.9)
#sns.move_legend(ax, "upper left", title='Types')
#plt.show()
plt.ylim(0.5,0.9)
plt.yticks(fontsize = 15,weight='bold')
#plt.xticks(fontsize = 12,weight='bold')
sns.move_legend(ax, "lower center", bbox_to_anchor=(.5,1), ncol=2, title=None, frameon=False)
plt.setp(ax.get_legend().get_texts(), fontsize='15') 
plt.show()


# In[4]:


import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt


path = "/home/amrita/Downloads/"
os.chdir(path)
dataframe1 = pd.read_excel('ShannonEntropy.xlsx')


# In[5]:


colors = ['pink','grey','green','purple']


# In[6]:


# create grouped boxplot
ax = sns.barplot(x = dataframe1['ProteinType'],
			y = dataframe1['ShannonEntropy'],
			hue = dataframe1['ProteinType'],palette = colors,width=0.9)
#sns.move_legend(ax, "upper left", title='Types')
#plt.show()
plt.yticks(fontsize = 15,weight='bold')
#plt.xticks(fontsize = 12,weight='bold')
sns.move_legend(ax, "lower center", bbox_to_anchor=(.5,1), ncol=2, title=None, frameon=False)
plt.setp(ax.get_legend().get_texts(), fontsize='15') 
plt.show()


# In[2]:


import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt


path = "/home/amrita/Downloads/"
os.chdir(path)
dataframe1 = pd.read_excel('GraphHelixTurnSheet.xlsx')


# In[3]:


colors = ['pink','grey','green','purple']


# In[4]:


# create grouped boxplot
ax = sns.barplot(x = dataframe1['SecondaryStructure'],
			y = dataframe1['Fraction'],
			hue = dataframe1['ProteinType'],palette = colors,width=0.9)
#sns.move_legend(ax, "upper left", title='Types')
#plt.show()
plt.yticks(fontsize = 15,weight='bold')
#plt.xticks(fontsize = 12,weight='bold')
sns.move_legend(ax, "lower center", bbox_to_anchor=(.5,1), ncol=2, title=None, frameon=False)
plt.setp(ax.get_legend().get_texts(), fontsize='15') 
plt.show()


# In[ ]:





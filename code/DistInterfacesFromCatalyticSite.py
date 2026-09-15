#!/usr/bin/env python
# coding: utf-8

# In[17]:


# import pandas lib as pd
import pandas as pd
import os


path = "/home/amrita/Downloads/"
os.chdir(path)


# read by default 1st sheet of an excel file
dataframe1 = pd.read_excel('DistFromCatalyticSite.xlsx')


# In[18]:


print(dataframe1)


# In[19]:


print(dataframe1.columns)


# In[20]:


import seaborn as sns
import matplotlib.pyplot as plt


# In[21]:


# create grouped boxplot
ax = sns.barplot(x = dataframe1['Protein Type'],
			y = dataframe1['Distance from the parallel/major interface'],
			hue = dataframe1['Protein Type'],palette=['yellow','brown', 'purple','hotpink', 'pink'])

sns.move_legend(ax, "lower center", bbox_to_anchor=(.5,1), ncol=2, title=None, frameon=False)
plt.setp(ax.get_legend().get_texts(), fontsize='10') 
plt.yticks(fontsize = 13,weight='bold')
# Adding error bars
plt.show()


# In[1]:


import pandas as pd
import os


path = "/home/amrita/Downloads/"
os.chdir(path)


# read by default 1st sheet of an excel file
dataframe1 = pd.read_excel('GraphChemistryMetalBindingRegion2.xlsx')


# In[2]:


print(dataframe1)


# In[3]:


print(dataframe1.columns)


# In[4]:


import seaborn as sns
import matplotlib.pyplot as plt


# In[6]:


# create grouped boxplot
ax = sns.barplot(x = dataframe1['Residue Type'],
			y = dataframe1['Percent'],
			hue = dataframe1['Protein Type'],palette=['yellow','brown', 'purple','hotpink', 'pink'])

sns.move_legend(ax, "lower center", bbox_to_anchor=(.5,1), ncol=2, title=None, frameon=False)
plt.setp(ax.get_legend().get_texts(), fontsize='10') 
plt.yticks(fontsize = 13,weight='bold')
# Adding error bars
plt.show()


# In[ ]:


# create grouped boxplot
ax = sns.barplot(x = dataframe1['Residue Type'],
			y = dataframe1['Percent'],
			hue = dataframe1['Protein Type'],palette=['yellow','brown', 'purple','hotpink', 'pink'])

sns.move_legend(ax, "lower center", bbox_to_anchor=(.5,1), ncol=2, title=None, frameon=False)
plt.setp(ax.get_legend().get_texts(), fontsize='10') 
plt.yticks(fontsize = 13,weight='bold')
# Adding error bars
plt.show()


# In[10]:


for i, interface in enumerate(interfaces):

    colors_for_this_interface = [row[i] for row in bar_colors]

    ax.bar(
        x + (i - len(interfaces)/2 + 0.5)*bar_width,
        means[interface],
        width=bar_width,
        color=colors_for_this_interface,
        yerr=stds[interface],
        capsize=4,
        label=interface
    )


# In[37]:


import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

path = "/home/amrita/Downloads/"
os.chdir(path)


# read by default 1st sheet of an excel file
dataframe13 = pd.read_excel('MetalCenterFromInterface.xlsx')


# In[38]:


colors = ['#f26b8a','#fda4ba','#fc46aa','#ebecb1','#d7eea6','#ebf907','#636363','#949292ff','#bdbdbd','#f5deb3','#fbdd7e','#d1b26f','#9ebcda','#8c96c6','#8c6bb1']


# In[39]:


# create grouped boxplot
#plt.figure(figsize=(5,4))
plt.figure(figsize=(10, 6))
n = len(dataframe13['ProteinType'])

# Positions for the bars
x_pos = np.arange(n)

# Mean values
y = dataframe13['DistFromActiveSite']

# Standard deviation values
std = dataframe13['Std']

# Bar plot with standard deviation error bars
ax = plt.bar(
    x_pos,
    y,
    color=colors,
    width=0.5,
    yerr=std,              # <-- adds std deviation bars
    capsize=5,             # <-- small horizontal cap at top
    ecolor='black'         # <-- color of error bars
)

# X-axis labels
plt.xticks(x_pos, dataframe13['ProteinType'])
#plt.ylim(-4000,-2000)
# Y-axis formatting
plt.yticks(fontsize=12, weight='bold')

plt.show()


# In[40]:


# create grouped boxplot
#plt.figure(figsize=(5,4))
plt.figure(figsize=(10, 6))
n = len(dataframe13['Interface'])

# Positions for the bars
x_pos = np.arange(n)

# Mean values
y = dataframe13['DistFromActiveSite']

# Standard deviation values
std = dataframe13['Std']

# Bar plot with standard deviation error bars
ax = plt.bar(
    x_pos,
    y,
    color=colors,
    width=0.5,
    yerr=std,              # <-- adds std deviation bars
    capsize=5,             # <-- small horizontal cap at top
    ecolor='black'         # <-- color of error bars
)

# X-axis labels
plt.xticks(x_pos, dataframe13['ProteinType'])
#plt.ylim(-4000,-2000)
# Y-axis formatting
plt.yticks(fontsize=12, weight='bold')

plt.show()


# In[41]:


import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


# In[42]:


colors = ['#f26b8a','#fda4ba','#fc46aa','#ebecb1','#d7eea6','#ebf907','#636363','#949292ff','#bdbdbd','#f5deb3','#fbdd7e','#d1b26f','#9ebcda','#8c96c6','#8c6bb1']


# In[44]:


bar_colors = [
    ['#f26b8a', '#fda4ba', '#fc46aa'],
    ['#ebecb1', '#d7eea6', '#ebf907'],  
    ['#636363', '#949292', '#bdbdbd'],  
    ['#f5deb3', '#fbdd7e', '#d1b26f'],  
    ['#9ebcda', '#8c96c6', '#8c6bb1']  
]


# In[46]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


path = "/home/amrita/Downloads/"
os.chdir(path)


# read by default 1st sheet of an excel file
dataframe13 = pd.read_excel('MetalCenterFromInterface.xlsx')

# Pivot the data
means = dataframe13.pivot(index='ProteinType',
                          columns='Interface',
                          values='DistFromActiveSite')

stds = dataframe13.pivot(index='ProteinType',
                         columns='Interface',
                         values='Std')

protein_types = means.index
interfaces = means.columns

x = np.arange(len(protein_types))
bar_width = 0.25

fig, ax = plt.subplots(figsize=(12,6))
for i, interface in enumerate(interfaces):

    colors_for_this_interface = [row[i] for row in bar_colors]

    ax.bar(
        x + (i - len(interfaces)/2 + 0.5)*bar_width,
        means[interface],
        width=bar_width,
        color=colors_for_this_interface,
        yerr=stds[interface],
        capsize=4,
        label=interface
    )

ax.set_xticks(x)
ax.set_xticklabels(protein_types, rotation=45)
ax.set_ylabel('Distance from Active Site')
ax.set_xlabel('Protein Type')
#ax.legend(title='Interface')

plt.tight_layout()
plt.show()


# In[1]:


import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Set working directory
path = "/home/amrita/Downloads/"
os.chdir(path)

# Read Excel file
dataframe13 = pd.read_excel('MetalCenterFromInterface(1).xlsx')

# Preserve the order from Excel
protein_order = dataframe13['ProteinType'].drop_duplicates()
interface_order = dataframe13['Interface'].drop_duplicates()

# Pivot the data and retain Excel ordering
means = dataframe13.pivot(
    index='ProteinType',
    columns='Interface',
    values='DistFromActiveSite'
).reindex(index=protein_order, columns=interface_order)

stds = dataframe13.pivot(
    index='ProteinType',
    columns='Interface',
    values='Std'
).reindex(index=protein_order, columns=interface_order)

protein_types = means.index
interfaces = means.columns

# Colors: one unique color per ProteinType-Interface combination
bar_colors = [
    ['#f26b8a', '#fda4ba', '#fc46aa'],  # 1jku
    ['#ebecb1', '#d7eea6', '#ebf907'],  # 2cwl
    ['#636363', '#949292', '#bdbdbd'],  # 2v8t
    ['#f5deb3', '#fbdd7e', '#d1b26f'],  # 6j42
    ['#9ebcda', '#8c96c6', '#8c6bb1'],  # Arch
    ['#ff9999', '#66b3ff', '#99ff99']   # Paki
]

x = np.arange(len(protein_types))
bar_width = 0.25

fig, ax = plt.subplots(figsize=(12, 6))

for i, interface in enumerate(interfaces):

    # Get colors for this interface across all proteins
    colors_for_this_interface = [row[i] for row in bar_colors]

    ax.bar(
        x + (i - len(interfaces)/2 + 0.5) * bar_width,
        means[interface],
        width=bar_width,
        color=colors_for_this_interface,
        yerr=stds[interface],
        capsize=4,
        ecolor='black',
        label=interface
    )

ax.set_xticks(x)
ax.set_xticklabels(protein_types, rotation=45, fontsize=12)
ax.set_ylabel('Distance from Active Site', fontsize=12)
ax.set_xlabel('Protein Type', fontsize=12)

# Uncomment if you want the interface legend
# ax.legend(title='Interface')

plt.tight_layout()
plt.show()


# In[ ]:





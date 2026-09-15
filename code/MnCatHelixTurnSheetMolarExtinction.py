#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import pandas lib as pd
import pandas as pd
import os
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

path = "/home/amrita/Downloads/"
os.chdir(path)


# read by default 1st sheet of an excel file
dataframe1 = pd.read_excel('MesoThermoHelixTurnSheet(2).xlsx')


# In[2]:


print(dataframe1)


# In[3]:


column_names = dataframe1.columns
print(column_names)


# In[7]:


# create grouped boxplot
#yerr=[0,0.01,0.02,0.02,0.03,0.03,0.01,0.01,0.02,0.03,0.02,0.03,0.01,0.01,0.03,0.04,0.01,0.04]
ax = sns.barplot(x = dataframe1['SecondaryStructure'],y = dataframe1['Fraction'],hue = dataframe1['ProteinType'],color = 'terrain', palette = [ 'tab:pink','tab:grey','tab:purple','tab:blue','tab:orange','tab:green'])
ax.errorbar(x = dataframe1['SecondaryStructure'], y = dataframe1['Fraction'], yerr=dataframe1['StdDev'], fmt='o', color='b', alpha=0.5)
#sns.move_legend(ax, "upper left", title='Types')
#plt.show()
#ax.errorbar(x = dataframe1['SecondaryStructure'],y = dataframe1['Fraction'], yerr=yerr, fmt='none', ecolor='red', elinewidth=2, capsize=5)
ax.set_ylim(ymin=0.0, ymax=0.4)
#ax.errorbar(x = dataframe1['SecondaryStructure'],y = dataframe1['Fraction'],yerr=dataframe1['StdDev'], fmt='o', color='b', alpha=0.5)
#plt.errorbar(x = dataframe1['SecondaryStructure'],y = dataframe1['Fraction'],yerr=dataframe1['StdDev'], fmt="o", color="r")
plt.yticks(fontsize = 15,weight='bold')
plt.xticks(fontsize = 12,weight='bold')
sns.move_legend(ax, "lower center", bbox_to_anchor=(.5,1), ncol=2, title=None, frameon=False)
plt.setp(ax.get_legend().get_texts(), fontsize='15') 
plt.show()


# In[12]:


# Create the barplot
ax = sns.barplot(x = dataframe1['SecondaryStructure'], 
                 y = dataframe1['Fraction'], 
                 hue = dataframe1['ProteinType'], 
                 color = 'terrain', 
                 palette = ['tab:pink', 'tab:grey', 'tab:purple', 'tab:blue', 'tab:orange', 'tab:green'])

# Loop through each bar (patch) and add error bars
for i, bar in enumerate(ax.patches):
    # Get the height of each bar and its position
    height = bar.get_height()
    x_position = bar.get_x() + bar.get_width() / 2
    # Get the standard deviation value for the bar
    std_dev = dataframe1['StdDev'].iloc[i]  # Make sure this matches the indexing of the dataframe
    # Add error bar for each bar
    ax.errorbar(x_position, height, yerr=std_dev, fmt='o', color='k', alpha=0.5)
    
# Adjusting plot appearance
ax.set_ylim(ymin=0.0, ymax=0.4)
plt.yticks(fontsize=15, weight='bold')
plt.xticks(fontsize=12, weight='bold')

# Customizing legend position
sns.move_legend(ax, "lower center", bbox_to_anchor=(.5, 1), ncol=2, title=None, frameon=False)
plt.setp(ax.get_legend().get_texts(), fontsize=15)

plt.show()



# In[16]:


import seaborn as sns
import matplotlib.pyplot as plt

# Plotting the barplot with grouped categories
ax = sns.barplot(x=dataframe1['SecondaryStructure'], y=dataframe1['Fraction'], 
                 hue=dataframe1['ProteinType'], palette=['tab:pink', 'tab:grey', 'tab:purple', 'tab:blue', 'tab:orange', 'tab:green'])

# Adding error bars using the standard deviation from the dataframe
ax.errorbar(x=dataframe1,  # Convert categorical x-axis to numeric for errorbar alignment
            y=dataframe1['Fraction'], 
            yerr=dataframe1["StdDev"].values,  # Using StdDev column for error bars
            fmt='none', 
            ecolor='red', 
            elinewidth=2, 
            capsize=5)

# Adjusting plot appearance
ax.set_ylim(ymin=0.0, ymax=0.4)
plt.yticks(fontsize=15, weight='bold')
plt.xticks(fontsize=12, weight='bold')

# Customizing legend position
sns.move_legend(ax, "lower center", bbox_to_anchor=(.5, 1), ncol=2, title=None, frameon=False)
plt.setp(ax.get_legend().get_texts(), fontsize=15)

plt.show()


# In[58]:


sns.barplot(x=dataframe1['SecondaryStructure'], y=dataframe1['Fraction'], 
                 hue=dataframe1['ProteinType'], palette=['tab:pink', 'tab:grey', 'tab:purple', 'tab:blue', 'tab:orange', 'tab:green'])
plt.errorbar(range(18),  # Convert categorical x-axis to numeric for errorbar alignment
            dataframe1['Fraction'], 
            dataframe1["StdDev"],
             fmt='none', 
            ecolor='red', 
            elinewidth=2, 
            capsize=5)# Using StdDev column for error bars)


# In[53]:


dataframe1.shape


# In[45]:


dataframe1


# In[1]:


# import pandas lib as pd
import pandas as pd
import os
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

path = "/home/amrita/Downloads/"
os.chdir(path)


# read by default 1st sheet of an excel file
dataframe1 = pd.read_excel('MolarExtinctionMnCat(1).xlsx')


# In[2]:


print(dataframe1)


# In[3]:


column_names = dataframe1.columns
print(column_names)


# In[4]:


# create grouped boxplot
ax = sns.barplot(x = dataframe1['ProteinType2'],
			y = dataframe1['Molar Extinction Coefficient'],
			hue = dataframe1['ProteinType'],color = 'terrain', palette = [ 'tab:pink','tab:red','tab:purple','tab:blue','tab:orange','tab:green'], width=1.5)
#sns.move_legend(ax, "upper left", title='Types')
#plt.show()
ax.set_ylim(ymin=15000, ymax=32000)
plt.yticks(fontsize = 15,weight='bold')
#plt.xticks(fontsize = 12,weight='bold')
sns.move_legend(ax, "lower center", bbox_to_anchor=(.5,1), ncol=2, title=None, frameon=False)
plt.setp(ax.get_legend().get_texts(), fontsize='15') 
plt.show()


# In[5]:


colors = ['pink','grey','purple','darkblue','orangered','green']


# In[6]:


# create grouped boxplot
plt.figure(figsize=(5,4))
#ax = sns.barplot(x = dataframe1['A'],y = dataframe1['C'],hue = dataframe1['A'],palette = colors,width=o.8)

n=len(dataframe1['ProteinType2'])

# Positions for the bars
x_pos = np.arange(n)  # Default positions

# Reduce the gap by modifying positions manually
# Adjust the width between the bars by setting a smaller spacing (e.g., smaller interval)
plt.bar(x_pos, dataframe1['Molar Extinction Coefficient'],color = colors, width=0.5)  # Width of bars remains the same
plt.xticks(x_pos, dataframe1['ProteinType2'])  # Set the x-axis ticks to correspond to the categories
plt.ylim(15000,32000)

#sns.move_legend(ax, "upper left", title='Types')
#plt.show()
plt.yticks(fontsize = 12,weight='bold')
plt.xticks(fontsize = 15,weight='bold')
sns.move_legend(ax, "lower center", bbox_to_anchor=(.5,1), ncol=2, title=None, frameon=False)
plt.setp(ax.get_legend().get_texts(), fontsize='15')
sns.move_legend(ax, "lower center", bbox_to_anchor=(.5,1), ncol=2, title=None, frameon=False)
plt.setp(ax.get_legend().get_texts(), fontsize='15') 
plt.show()


# In[1]:


# import pandas lib as pd
import pandas as pd
import os
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

path = "/home/amrita/Downloads/"
os.chdir(path)


# read by default 1st sheet of an excel file
dataframe1 = pd.read_excel('MnCatNP-Pratio.xlsx')


# In[2]:


colors = ['pink','grey','purple','darkblue','orangered','green']


# In[7]:


# create grouped boxplot
plt.figure(figsize=(5,4))
#ax = sns.barplot(x = dataframe1['A'],y = dataframe1['C'],hue = dataframe1['A'],palette = colors,width=o.8)

n=len(dataframe1['ProteinType'])

# Positions for the bars
x_pos = np.arange(n)  # Default positions

# Reduce the gap by modifying positions manually
# Adjust the width between the bars by setting a smaller spacing (e.g., smaller interval)
plt.bar(x_pos, dataframe1['Ratio'],color = colors, width=0.5)  # Width of bars remains the same
plt.xticks(x_pos, dataframe1['ProteinType'])  # Set the x-axis ticks to correspond to the categories
plt.ylim(0.5,1.5)

#sns.move_legend(ax, "upper left", title='Types')
#plt.show()
plt.yticks(fontsize = 12,weight='bold')
#plt.xticks(fontsize = 15,weight='bold')
sns.move_legend(ax, "lower center", bbox_to_anchor=(.5,1), ncol=2, title=None, frameon=False)
plt.setp(ax.get_legend().get_texts(), fontsize='15')
sns.move_legend(ax, "lower center", bbox_to_anchor=(.5,1), ncol=2, title=None, frameon=False)
plt.setp(ax.get_legend().get_texts(), fontsize='15') 
plt.show()


# In[ ]:


# create grouped boxplot
plt.figure(figsize=(5,4))
#ax = sns.barplot(x = dataframe1['A'],y = dataframe1['C'],hue = dataframe1['A'],palette = colors,width=o.8)

n=len(dataframe1['ProteinType'])

# Positions for the bars
x_pos = np.arange(n)  # Default positions

# Reduce the gap by modifying positions manually
# Adjust the width between the bars by setting a smaller spacing (e.g., smaller interval)
for i, bar in enumerate(ax.patches):
    # Get the height of each bar and its position
    height = bar.get_height()
    x_position = bar.get_x() + bar.get_width() / 2
    # Get the standard deviation value for the bar
    std_dev = dataframe1['StdDev'].iloc[i]  # Make sure this matches the indexing of the dataframe
    # Add error bar for each bar
    ax.errorbar(x_position, height, yerr=std_dev, fmt='o', color='b', alpha=0.5)

ax=plt.bar(x_pos, dataframe1['Ratio'],color = colors, width=0.5)  # Width of bars remains the same
plt.xticks(x_pos, dataframe1['ProteinType'])  # Set the x-axis ticks to correspond to the categories
plt.ylim(0.5,1.5)

#sns.move_legend(ax, "upper left", title='Types')
#plt.show()
plt.yticks(fontsize = 12,weight='bold')
#plt.xticks(fontsize = 15,weight='bold')
sns.move_legend(ax, "lower center", bbox_to_anchor=(.5,1), ncol=2, title=None, frameon=False)
plt.setp(ax.get_legend().get_texts(), fontsize='15')
sns.move_legend(ax, "lower center", bbox_to_anchor=(.5,1), ncol=2, title=None, frameon=False)
plt.setp(ax.get_legend().get_texts(), fontsize='15') 
plt.show()


# In[4]:


# create grouped boxplot
ax = sns.barplot(x = dataframe1['ProteinType'],
			y = dataframe1['Ratio'],
			hue = dataframe1['ProteinType'],color = 'terrain', palette = [ 'tab:pink','tab:grey','tab:purple','tab:blue','tab:orange','tab:green'], width=1.5)
#sns.move_legend(ax, "upper left", title='Types')
#plt.show()
ax.set_ylim(ymin=0.5, ymax=1.5)
plt.yticks(fontsize = 15,weight='bold')
#plt.xticks(fontsize = 12,weight='bold')
sns.move_legend(ax, "lower center", bbox_to_anchor=(.5,1), ncol=2, title=None, frameon=False)
plt.setp(ax.get_legend().get_texts(), fontsize='15') 
plt.show()


# In[1]:


# import pandas lib as pd
import pandas as pd
import os
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

path = "/home/amrita/Downloads/"
os.chdir(path)


# read by default 1st sheet of an excel file
dataframe1 = pd.read_excel('GraphMnCatCavityFeb25.xlsx')


# In[2]:


colors = ['pink','grey','purple']


# In[5]:


# create grouped boxplot
ax = sns.barplot(x = dataframe1['ProteinType'],
			y = dataframe1['CavitySurfaceArea'],
			hue = dataframe1['ProteinType'],color = 'terrain', palette = [ 'tab:pink','tab:grey','tab:purple'])
#sns.move_legend(ax, "upper left", title='Types')
#plt.show()
plt.yticks(fontsize = 15,weight='bold')
#plt.xticks(fontsize = 12,weight='bold')
sns.move_legend(ax, "lower center", bbox_to_anchor=(.5,1), ncol=2, title=None, frameon=False)
plt.setp(ax.get_legend().get_texts(), fontsize='15') 
plt.show()


# In[6]:


# create grouped boxplot
ax = sns.barplot(x = dataframe1['ProteinType'],
			y = dataframe1['CavityVolume'],
			hue = dataframe1['ProteinType'],color = 'terrain', palette = [ 'tab:pink','tab:grey','tab:purple'])
#sns.move_legend(ax, "upper left", title='Types')
#plt.show()
plt.yticks(fontsize = 15,weight='bold')
#plt.xticks(fontsize = 12,weight='bold')
sns.move_legend(ax, "lower center", bbox_to_anchor=(.5,1), ncol=2, title=None, frameon=False)
plt.setp(ax.get_legend().get_texts(), fontsize='15') 
plt.show()


# In[7]:


# create grouped boxplot
ax = sns.barplot(x = dataframe1['ProteinType'],
			y = dataframe1['Cavity(S/V)'],
			hue = dataframe1['ProteinType'],color = 'terrain', palette = [ 'tab:pink','tab:grey','tab:purple'])
#sns.move_legend(ax, "upper left", title='Types')
#plt.show()
plt.yticks(fontsize = 15,weight='bold')
#plt.xticks(fontsize = 12,weight='bold')
sns.move_legend(ax, "lower center", bbox_to_anchor=(.5,1), ncol=2, title=None, frameon=False)
plt.setp(ax.get_legend().get_texts(), fontsize='15') 
plt.show()


# In[ ]:





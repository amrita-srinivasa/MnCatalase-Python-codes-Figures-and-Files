#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from biopandas.pdb import PandasPdb
import os


# In[14]:


path = "/home/amrita/Downloads/ArchaeaFrames/"
os.chdir(path)


# In[16]:


filePattern = 'frame9999.hb2'
import glob
file_name = 'Ar2HbondFinal.csv'
tmp = pd.DataFrame()


# In[17]:


df = pd.read_fwf(filePattern, skiprows=8)


# In[18]:


df


# In[19]:


df.columns =['A1','A2','A3','A4','A5','A6','A7','A8','A9','A10','A11','A12','A13']


# In[11]:


df['A1']


# In[ ]:


df["A14"] = df["A1"] + " " + df["A3"]
df['B1'] = df['A1'].astype(str).str[0]
df['B2'] = df['A3'].astype(str).str[0]


# In[43]:


for hbondFile in sorted(glob.glob(filePattern)):
    print('processing---'+hbondFile+'---')
    try:
        df = pd.read_csv(
                hbondFile,
                skiprows=8,
                sep=r"\s+",
                header=None,
                engine="python"
        )
        df.columns =['A1','A2','A3','A4','A5','A6','A7','A8','A9','A10','A11','A12','A13']
        df["A14"] = df["A1"] + " " + df["A3"]
        df['B1'] = df['A1'].astype(str).str[0]
        df['B2'] = df['A3'].astype(str).str[0]
        df1 = df[(df['B1'] != df['B2'])]
        df2= df1[(df1['B1'] == 'A') | (df1['B2'] == 'A') ]
        grouped = df2.groupby(['A14'], as_index=False).mean().groupby('A14')['A5'].mean()
        print(grouped)
        #tmp = tmp.append(grouped)
        #outputxlsx = outputxlsx.append(df, ignore_index=True)
        tmp = pd.concat([tmp, grouped])
    except:
        pass
tmp.to_csv(file_name)


# In[49]:


df1 = df[(df['B1'] != df['B2'])]
df2= df1[(df1['B1'] == 'A') | (df1['B2'] == 'A') ]


# In[56]:


df['A1'].astype(str).str[0]


# In[ ]:


grouped = df2.groupby(['A14'], as_index=False).mean().groupby('A14')['A5'].mean()
print(grouped)
        #tmp = tmp.append(grouped)
        #outputxlsx = outputxlsx.append(df, ignore_index=True)
tmp = pd.concat([tmp, grouped])


# In[44]:


df = pd.read_csv("GeoHbondFinal.csv")


# In[46]:


df


# In[7]:


df.columns =['Chain-Chain','Dist']


# In[8]:


grouped2 = df.groupby(['Chain-Chain'], as_index=False).mean().groupby('Chain-Chain')['Dist'].mean()


# In[9]:


df = df.groupby('Chain-Chain') \
       .agg(count=('Chain-Chain', 'size'), mean_sent=('Dist', 'mean')) \
       .reset_index()


# In[23]:


df


# In[24]:


df.to_csv('Arch.csv', index=False)


# In[ ]:





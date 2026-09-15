#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from biopandas.pdb import PandasPdb
import os


# In[2]:


#path = "/home/amrita/khejri/amrita-project/arabidopsis1000/"
path = "/home/amrita/Downloads/GeobacillusFrames2/"
os.chdir(path)


# In[3]:


filePattern = '*.hb2'
import glob
#file_name = 'ArabiHbondFinal.csv'
file_name = 'GeoBHbondFinal2.csv'
tmp = pd.DataFrame()


# In[4]:


for hbondFile in sorted(glob.glob(filePattern)):
    #print('processing---'+hbondFile+'---')
    try:
        df = pd.read_fwf(hbondFile, skiprows=8)
        df.columns =['A1','A2','A3','A4','A5','A6','A7','A8','A9','A10','A11','A12','A13']
        df["A14"] = df["A1"] + " " + df["A3"]
        df['B1'] = df['A1'].astype(str).str[0]
        df['B2'] = df['A3'].astype(str).str[0]
        df1 = df[(df['B1'] != df['B2'])]
        df2= df1[(df1['B1'] == 'A') | (df1['B2'] == 'A') ]
        grouped = df2.groupby(['A14'], as_index=False).mean().groupby('A14')['A5'].mean()
        #print(grouped)
        #tmp = tmp.append(grouped)
        #outputxlsx = outputxlsx.append(df, ignore_index=True)
        tmp = pd.concat([tmp, grouped])
    except:
        print('*****error in '+hbondFile+'*****')
        pass
tmp.to_csv(file_name)


# In[5]:


df = pd.read_csv("GeoBHbondFinal2.csv")


# In[6]:


df


# In[7]:


df.columns =['Chain-Chain','Dist']


# In[8]:


grouped2 = df.groupby(['Chain-Chain'], as_index=False).mean().groupby('Chain-Chain')['Dist'].mean()


# In[9]:


df = df.groupby('Chain-Chain') \
       .agg(count=('Chain-Chain', 'size'), mean_sent=('Dist', 'mean')) \
       .reset_index()


# In[10]:


df


# In[11]:


df.to_csv('MDgeofinal3.csv', index=False)


# In[ ]:





# In[ ]:





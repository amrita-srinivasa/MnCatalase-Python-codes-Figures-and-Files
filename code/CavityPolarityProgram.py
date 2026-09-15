#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from biopandas.pdb import PandasPdb
import os
import glob


# In[2]:


path = "/home/amrita/Downloads/1ji5_cavity/receptor_1_result_cavity"
os.chdir(path)
filePattern = 'this_cavity_*.pdb'


# In[71]:


ConcatenatedFile= pd.DataFrame()


# In[72]:


for cavityFile in sorted(glob.glob(filePattern)):
    print(cavityFile)
    ps = PandasPdb().read_pdb(cavityFile)
    df = ps.df['ATOM']
    ConcatenatedFile=pd.concat([ConcatenatedFile,df], axis=0)


# In[73]:


ConcatenatedFile


# In[74]:


ConcatenatedFile["concat"] = ConcatenatedFile["residue_name"].astype(str) + ConcatenatedFile["chain_id"].astype(str)+ ConcatenatedFile["residue_number"].astype(str)
c=ConcatenatedFile.drop_duplicates(subset=['concat'],keep='first')


# In[75]:


c


# In[76]:


item_counts = c.groupby(['residue_name'])['residue_name'].count()


# In[77]:


item_counts


# In[ ]:





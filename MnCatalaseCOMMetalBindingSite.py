#!/usr/bin/env python
# coding: utf-8

# In[43]:


import pandas as pd
from biopandas.pdb import PandasPdb
import os


# In[44]:


path = "/home/amrita/WD-Ferritin/pymol sessions and images"
os.chdir(path)


# In[45]:


ps = PandasPdb().read_pdb("6j42_biomolecule_new.pdb")


# In[46]:


df = ps.df['ATOM']


# In[47]:


df


# In[48]:


df1=df[df['chain_id']=='A']


# In[49]:


df2=df1[(df1['residue_number']==30)+(df1['residue_number']==31)]


# In[50]:


#df2=df1[(df1['residue_number']==35)+(df1['residue_number']==66)+(df1['residue_number']==69)+(df1['residue_number']==148)+(df1['residue_number']==181)]


# ##### df2

# In[51]:


dict = {'N' : 14, 'C' : 12, 'O' : 16,'H' : 1, 'S' : 32}


# In[52]:


df2.replace({"element_symbol": dict})


# In[53]:


df3 = df2[['x_coord', 'y_coord','z_coord','element_symbol']]


# In[54]:


df3


# In[55]:


values_array = df3.values
print(values_array)


# In[56]:


df4=df3.replace({"element_symbol": dict})


# In[57]:


values_array = df4.values
print(values_array)


# In[58]:


weighted_x = (df4['x_coord'] * df4['element_symbol']).sum()
weighted_y = (df4['y_coord'] * df4['element_symbol']).sum()
weighted_z = (df4['z_coord'] * df4['element_symbol']).sum()


# In[59]:


total_mass = df4['element_symbol'].sum()


# In[60]:


# Calculate the center of mass
com_x = weighted_x / total_mass
com_y = weighted_y / total_mass
com_z = weighted_z / total_mass


# In[61]:


round(com_x,2)


# In[62]:


round(com_y,2)


# In[63]:


round(com_z,2)


# In[ ]:





# In[ ]:





# In[ ]:





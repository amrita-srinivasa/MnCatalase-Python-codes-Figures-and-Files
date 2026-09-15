#!/usr/bin/env python
# coding: utf-8

# In[37]:


from Bio.SeqUtils.ProtParam import ProteinAnalysis


# In[38]:


X = ProteinAnalysis(
"MVFQRIDRLAIELPKPKYADPNAAAAVQELLGGRFGEMSTLNNYLFQSFNFRQKKKLRPF"
"YELVASITAEEFGHVELVSNAINLCLTGSTHPGDPDAAPMKDAKDKRNTYHFIATAQTAF"
"PGDSMGKAWTGEYVFNSGNLILDLLHNFFLECGARTHKMRVYEMTDHPTAREMIGYLLVR"
"GGVHILAYAKAIEVATGVDVTKLLPIPKLDNRVFDEARKYEDQGVHRRLYTFSDRYYKEI"
"VRIWQGTHPSDGQPLEVVEGAPQGGAIPDLDEVPEEFAPGISAEDFFEIAKRLQRSAGL")


# In[39]:


X


# In[40]:


print(X.count_amino_acids())


# In[41]:


print("%0.2f" % X.molecular_weight())


# In[42]:


print("%0.2f" % X.aromaticity())


# In[43]:


print("%0.2f" % X.instability_index(),'\t',"%0.2f" % X.aromaticity())


# In[44]:


print("%0.2f" % X.isoelectric_point())


# In[45]:


sec_struc = X.secondary_structure_fraction()  # [helix, turn, sheet]

print("%0.2f" % sec_struc[0])
print("%0.2f" % sec_struc[1])
print("%0.2f" % sec_struc[2])


# In[46]:


epsilon_prot = X.molar_extinction_coefficient()  

print(epsilon_prot[0])
print(epsilon_prot[1])


# In[47]:


print("%0.2f" % X.gravy())


# In[48]:


print(X.secondary_structure_fraction())


# In[ ]:





# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Corrections over v1:
#1. <12 Ang
#2. Reporting unique residue num at PDB level
#3. Local density (atomsAtInterfaceLength/no of atoms in int file) - reported at chain pair and PDB levels
#4. Floating Precison fixed at 3 


# In[1]:


import pandas as pd
from biopandas.pdb import PandasPdb
import glob
import os


# In[2]:


path="/home/amrita/WD-Ferritin/pymol sessions and images/"
os.chdir(path)

f_cp = open("resultArch-chainpair.txt", "a+")
f_pdb = open("resultArch-pdb.txt", "a+")


# In[3]:


import tempfile, shutil


# In[4]:


#pdbCode = '1nfv'


lastCodeProcessed = ''
buriedSum = 0
countInterfaceAtoms = 0
count_zeroInt = 0
count_nonZeroInt = 0
count_PDB_AtomsAtInteractionLength = 0
count_ResidueNumber = 0
f_cp.write('Chain Pair \t buried surface area\tunique residue numbers\t Interface Atoms\tlocaldensity\n')
f_pdb.write('PDB Code\t Total buried surface area\tunique residue numbers\t Interface Atoms\t Zero Interactions pairs \t Non-zero interaction pairs \t Local Density Count\n')


# In[5]:


def euclidean(x1,y1,z1,x2,y2,z2):
    return ((x1-x2) ** 2 + (y1-y2) ** 2 + (z1-z2) ** 2) ** 0.5


# In[6]:


for intFile in sorted(glob.glob(filePattern)):
    print(intFile+'---'+lastCodeProcessed)
    #file="1sq3-a-ab.int"
    if(intFile[0:4]!=lastCodeProcessed):
        f_pdb.write(lastCodeProcessed +'\t'+'{0:.3f}'.format(buriedSum)+'\t'+str(count_ResidueNumber)+'\t'+str(countInterfaceAtoms)+'\t'+str(count_zeroInt)+'\t'+str(count_nonZeroInt)+'\t'+'{0:.3f}'.format(count_PDB_AtomsAtInteractionLength/(countInterfaceAtoms or not countInterfaceAtoms))+'\n')
        lastCodeProcessed=intFile[0:4]
        print('processing --'+lastCodeProcessed)
        countInterfaceAtoms = 0
        buriedSum = 0
        count_PDB_AtomsAtInteractionLength = 0
        count_zeroInt = 0
        count_nonZeroInt = 0
        count_ResidueNumber = 0

    tmp = tempfile.NamedTemporaryFile(delete=True, suffix='.pdb')
    if(os.path.isfile(path+intFile)):
        if(os.path.getsize(path+intFile) > 0):
            shutil.copy2(path+intFile, tmp.name)
            #print(tmp.name)
            ps = PandasPdb().read_pdb(tmp.name)
            df = ps.df['ATOM']
            countInterfaceAtoms += df.shape[0]
            buriedAtomicSurface = df['occupancy'].values.sum()-df['b_factor'].values.sum()
            
            count_AtomsAtInteractionLength = 0
            current =[int(v) for v in df.index.tolist()] 
            for i in current:
                for j in current[i:]:  
                    #print(df.loc[i].x_coord,df.loc[i].y_coord, df.loc[i].z_coord,df.loc[j].x_coord,df.loc[j].y_coord, df.loc[j].z_coord)
                    if(euclidean(df.loc[i].x_coord,df.loc[i].y_coord, df.loc[i].z_coord,df.loc[j].x_coord,df.loc[j].y_coord, df.loc[j].z_coord)<12):
                        count_AtomsAtInteractionLength += 1
            count_PDB_AtomsAtInteractionLength += count_AtomsAtInteractionLength

            localDensity = count_AtomsAtInteractionLength/df.shape[0]
            count_ResidueNumber += df['residue_number'].unique().shape[0]
            f_cp.write(intFile[0:9] + '\t'+'{0:.3f}'.format(buriedAtomicSurface)+'\t'+str(df['residue_number'].unique().shape[0]) +'\t'+str(df.shape[0]) +'\t' + '{0:.3f}'.format(localDensity)+'\n')
            buriedSum += buriedAtomicSurface
            count_nonZeroInt += 1
        else:
            count_zeroInt += 1
localDensity_PDB = count_PDB_AtomsAtInteractionLength/(countInterfaceAtoms or not countInterfaceAtoms)
f_pdb.write(lastCodeProcessed +'\t'+'{0:.3f}'.format(buriedSum)+'\t'+str(count_ResidueNumber)+'\t'+str(countInterfaceAtoms)+'\t'+str(count_zeroInt)+'\t'+str(count_nonZeroInt)+'\t'+'{0:.3f}'.format(localDensity_PDB)+'\n')


# In[7]:


f_cp.close()
f_pdb.close()


# In[ ]:





# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[111]:


# import pandas lib as pd
import pandas as pd
import os
import math

path = "/home/amrita/WD-Ferritin/pymol sessions and images"
os.chdir(path)


# read by default 1st sheet of an excel file
file= '1jku-b-be.int'


# In[112]:


def distance(x1, y1, z1, x2, y2, z2):
    return math.sqrt(
        (x1 - x2)**2 +
        (y1 - y2)**2 +
        (z1 - z2)**2
    )


# In[113]:


def find_closest_atom(file, x0, y0, z0):

    min_dist = float("inf")
    closest_atom = None
    
    # Example usage
    x0 = 0.35
    y0 = -21.1
    z0 = 32.22

    min_dist = float("inf")
    closest_atom = None
    
    with open(file, "r") as f:
        for line in f:

            if not line.startswith("ATOM"):
                continue

            cols = line.split()

            atom_num = cols[1]
            atom_name = cols[2]
            res_name = cols[3]
            chain = cols[4]
            res_num = cols[5]

            x = float(cols[6])
            y = float(cols[7])
            z = float(cols[8])

            d = distance(x0,y0,z0, x, y, z)

            if d < min_dist:
                min_dist = d
                closest_atom = {
                    "atom_num": atom_num,
                    "atom_name": atom_name,
                    "res_name": res_name,
                    "chain": chain,
                    "res_num": res_num,
                    "x": x,
                    "y": y,
                    "z": z
                }
    print(f"Minimum distance: {min_dist:.3f}")
    return min_dist, closest_atom
    


# In[114]:


x0 = 0.35
y0 = -21.1
z0 = 32.22

min_dist, closest_atom = find_closest_atom(file, x0, y0, z0)

print(f"Minimum distance: {min_dist:.3f}")
print(closest_atom)



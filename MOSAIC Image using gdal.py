#!/usr/bin/env python
# coding: utf-8

# In[22]:


from osgeo import gdal
import os
from matplotlib import pyplot as plt
import numpy as np


# In[23]:


band_1_dir = os.chdir(r'D:\Data for Process\Data\Liss3python\Band_1')


# In[24]:


sub_scenes = ['a.tif','b.tif','c.tif','d.tif','e.tif','f.tif','g.tif','h.tif','i.tif']


# In[25]:


list = []
for i in sub_scenes:
    k=gdal.Open(i)
    l=k.ReadAsArray()
    list.append(l)


# In[26]:


plt.figure(figsize=(10,10))
for i in range (1,10):
    plt.subplot(3,3,i)
    plt.imshow(list[i-9], cmap='gray')


# In[27]:


projection = k.GetProjection()
projection


# In[28]:


mosaic_band_1 = gdal.Warp('mosaiced_band_1.tif', sub_scenes, format='GTiff')


# In[29]:


oo=gdal.Open('mosaiced_band_1.tif')


# In[30]:


pp=oo.ReadAsArray()


# In[31]:


plt.imshow(pp, cmap='gray')


# MOSAIC BY ANOTHER METHOD

# In[32]:


def calculate_extents(sub_scenes):
    trf = sub_scenes.GetGeoTransform()
    left = trf[0]
    right = trf[0]+trf[1]*sub_scenes.RasterXSize
    top = trf[3]
    bottom = trf[3]+trf[5]*sub_scenes.RasterYSize
    return (left, right, bottom, top)


# In[ ]:





# In[33]:


Extents = []
for i in sub_scenes:
    data = gdal.Open(i)
    extent = calculate_extents(data)
    Extents.append(extent)


# In[34]:


Extents


# In[35]:


Extents = np.array(Extents)
Extents


# In[36]:


mosaic_left = np.min(Extents[:,0:2])
mosaic_right = np.max(Extents[:,0:2])
mosaic_top = np.max(Extents[:,2:])
mosaic_bottom = np.min(Extents[:,2:])


# In[37]:


print(mosaic_left, mosaic_right, mosaic_top, mosaic_bottom)


# In[38]:


import geopandas as gpd


# In[47]:


a='a.tif'
c=gdal.Open(a)
b=c.ReadAsArray()
c.GetGeoTransform()


# In[44]:


b


# In[51]:


c.RasterXSize, c.RasterYSize


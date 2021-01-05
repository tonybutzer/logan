#!/usr/bin/env python
# coding: utf-8

# In[1]:


#! cp /home/jupyter-harmony/opt/logan/00-notebooks/00-portal-scraping/AOI/tonyaoi.geojson project_aoi.geojson
get_ipython().system(' ls')


# In[2]:


aoi='project_aoi.geojson'


# In[3]:


import json
with open(aoi) as f:
  geo_data = json.load(f)
geo_data


# In[4]:


type (geo_data['features'][0]['geometry'])


# In[5]:


geo_data['features'][0]['geometry']['coordinates'][0]


# In[6]:


nw = geo_data['features'][0]['geometry']['coordinates'][0][3]


# In[7]:


nw


# In[8]:


se = geo_data['features'][0]['geometry']['coordinates'][0][1]


# In[9]:


se


# In[10]:


url='/vsicurl/http://rangeland.ntsg.umt.edu/data/rap/rap-vegetation-cover/v2'
file = 'vegetation-cover-v2-2019.tif'
band = ' -b 1 '
window = f' {nw[0]} {nw[1]}, {se[0]} {se[1]} '


# In[11]:


window


# In[12]:


cmd='gdal_translate -co compress=lzw -co tiled=yes -co bigtiff=yes '


# In[13]:


get_ipython().system(' mkdir -p TIF')


# In[14]:


out_bucket='dev-et-data'
out_prefix='logan/in/raw/range_grass'


# In[15]:


def _run_command(cmd, verbose=False):
    if verbose:
        print(cmd)
    result = os.system(cmd)
    if result != 0:
        raise Exception('command "%s" failed with code %d.' % (cmd, result))


# In[16]:


full_cmd = cmd + band + ' -projwin ' + window + url + '/' + file + ' TIF/' + file
full_cmd


# In[17]:


get_ipython().run_cell_magic('time', '', '! gdal_translate -co compress=lzw -co tiled=yes -co bigtiff=yes  -b 1  -projwin  -121.11328124999999 45.874712248904764, -115.04882812499999 38.634036452919226 /vsicurl/http://rangeland.ntsg.umt.edu/data/rap/rap-vegetation-cover/v2/vegetation-cover-v2-2019.tif TIF/vegetation-cover-v2-2019.tif')


# In[18]:


#!echo TIF/ >>.gitignore
get_ipython().system(' ls -lh TIF')


# In[19]:


get_ipython().system(' wget https://raw.githubusercontent.com/tonybutzer/etm/master/etmLib/etmLib/s3_func.py')


# In[20]:


from s3_func import s3_push_delete_local


# In[21]:


help(s3_push_delete_local)


# In[22]:


bucket = 'dev-et-data'
bucket_filepath = 'logan/in/raw/range_grass/vegetation-cover-v2-2019.tif'
local_file = 'TIF/vegetation-cover-v2-2019.tif'


# In[23]:


s3_push_delete_local(local_file,bucket,bucket_filepath)


# In[28]:


get_ipython().system('aws s3 ls --human s3://dev-et-data/logan/in/raw/range_grass/')


# In[30]:


get_ipython().system(' rio info s3://dev-et-data/logan/in/raw/range_grass/vegetation-cover-v2-2019.tif | python -m json.tool')


# In[31]:


import xarray as xr
tiff_name = 's3://dev-et-data/logan/in/raw/range_grass/vegetation-cover-v2-2019.tif'
da = xr.open_rasterio(tiff_name)


# In[32]:


da


# In[36]:


import hvplot.xarray
da_b1 = da.sel(band=1)
da_b1.hvplot.image(dynamic=False,rasterize=True,grid=True, invert=False, width=700, height=600, cmap='category20')


# In[37]:


da_b1.hvplot.image(dynamic=False,rasterize=True,grid=True, invert=False, width=700, height=600, cmap='magma')


# In[ ]:





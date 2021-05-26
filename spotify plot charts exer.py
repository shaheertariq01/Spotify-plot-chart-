#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[10]:


ss= pd.read_csv("spotify.csv", index_col='Date', parse_dates=True)
ss


# In[14]:


plt.figure(figsize=(12,6))
sns.lineplot(data=ss)


# In[16]:


sns.set_style('white')
plt.figure(figsize=(12,6))
sns.lineplot(data=ss)


# In[17]:


sns.set_style('whitegrid')
plt.figure(figsize=(12,6))
sns.lineplot(data=ss)


# In[ ]:





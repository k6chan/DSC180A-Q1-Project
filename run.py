#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
import json

from src.data.load_dataset import load_data


# In[2]:


def main(targets):
    if 'data' in targets:
        with open('config/config.json') as f:
            params = json.load(f)
        load_data(**params)

if __name__ == '__main__':
    targets = sys.argv[1:]
    main(targets)


# In[ ]:





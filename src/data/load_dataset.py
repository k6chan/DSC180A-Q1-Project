#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pickle
import json
import os


# In[2]:


# read data

def read_corpus(fp):
    '''
    Loads the raw pickle (pickled DataFrame) file of the NYT or 20News raw data.
    '''
    with open(fp, "rb") as f:
        data = pickle.load(f)
    return data


# In[3]:


def read_seedwords(fp):
    '''
    Loads the raw JSON file of the NYT or 20News raw data.
    '''
    with open(fp) as f:
        seedwords = json.load(f)
        return seedwords


# In[ ]:


def load_data(corpi,seedwords,outpath):
    '''
    Reads the raw pickle and JSON files and saves them in the output directory.
    
    :param: corpi: a list of corpuses to read
    :param: seedwords: a list of seedwords to read
    :param: outpath: the output directory
    '''
    for corpus in corpi:
        c = read_corpus(corpus)
        basename = os.path.basename(corpus).split('.')[0]
        c.to_csv(os.path.join(outpath, basename + ".csv"))
    for seedwords_file in seedwords:
        s = read_seedwords(seedwords_file)
        #raw JSON is unchanged as of now
        basename = os.path.basename(seedwords_file).split('.')[0]
        with open(os.path.join(outpath, basename + ".json"), 'w') as f:
            json.dump(s,f)
    return

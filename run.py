#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
import json
import re

from src.data.load_dataset import load_data
from src.models.ir_tf_idf import ir_tfidf
from src.models.word2vec import word2vec
from src.models.score_F1 import score_F1


# In[2]:


def main(targets):
    if 'test' in targets:
        with open('config/test_config.json') as f:
            params = json.load(f)
        load_data(**params)
    elif 'data' in targets:
        with open('config/config.json') as f:
            params = json.load(f)
        load_data(**params)
    
    for i, corpi in enumerate(params["corpi"]):
        filename = re.sub('\..*$','',params["corpi"][i]) + ".csv"
        fp_data = params["outpath"] + "/" + filename
        fp_seeds = params["outpath"] + "/" + params["seedwords"][i]
        #TFIDF
        tfidf_res = ir_tfidf(fp_data, fp_seeds)
        micro = score_F1(tfidf_res["label"], tfidf_res["prediction"], "micro")
        macro = score_F1(tfidf_res["label"], tfidf_res["prediction"], "macro")
        print("IR-TF-IDF Micro-F1 score for", params["corpi"][i], micro)
        print("IR-TF-IDF Macro-F1 score for", params["corpi"][i], macro)
        #Word2Vec
        word2vec_res = word2vec(fp_data, fp_seeds)
        micro = score_F1(word2vec_res["label"], word2vec_res["prediction"], "micro")
        macro = score_F1(word2vec_res["label"], word2vec_res["prediction"], "macro")
        print("Word2Vec Micro-F1 score for", params["corpi"][i], micro)
        print("Word2Vec Macro-F1 score for", params["corpi"][i], macro)

if __name__ == '__main__':
    targets = sys.argv[1:]
    main(targets)


# In[ ]:





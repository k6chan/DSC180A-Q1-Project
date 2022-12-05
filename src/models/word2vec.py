import pandas as pd
import sklearn.feature_extraction as fe
from gensim.models import Word2Vec
import string
import numpy as np
import json


def tokenize(sentence):
    '''
    Returns a tokenized version of the given sentence, excluding punctuation and stopwords
    '''
    punctuation = set(string.punctuation)
    stopwords = set(fe.text.ENGLISH_STOP_WORDS)
    tokens = [w for w in (''.join([c for c in sentence.lower() if c not in punctuation]).split()) if w not in stopwords]
    return tokens

def word2vec(data_fp, seeds_fp):
    '''
    Return a DataFrame of the input with predicted labels using Word2Vec
    
    :param: data: a directory to a DataFrame with a "sentence" attribute
    :param: seeds: a directory to a dictionary of labels (keys) with a list of seed words (values)
    '''
    data = pd.read_csv(data_fp)
    with open(seeds_fp) as f:
        seeds = json.load(f)
    
    #reverse seeds dictionary
    genres = {}
    for genre,seed_words in seeds.items():
        for seed_word in seed_words:
            genres[seed_word] = genre
            
    data_ind = data.reset_index()
    
    data_tokens = []
    for row in data_ind.iterrows():
        data_tokens.append(tokenize(row[1]["sentence"]))

    model = Word2Vec(data_tokens, vector_size=100, sg=1)
    
    def predict_w2v(sentence):
        similarities = []
        for label in seeds:
            words_1 = seeds[label]
            words_2 = tokenize(sentence)
            cosine_sim = model.wv.n_similarity(words_1,words_2)
            similarities.append((cosine_sim,label))
        return max(similarities, key=lambda item: item[0])[1]
            
    df = data_ind.assign(prediction=data_ind["sentence"].apply(predict_w2v))
    
    return df
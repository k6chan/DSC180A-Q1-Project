import pandas as pd
import sklearn.feature_extraction as fe


def ir_tfidf(data, seeds):
    '''
    Return a DataFrame of the input with predicted labels using IR-TF-IDF
    
    :param: data: a DataFrame with a "sentence" attribute
    :param: seeds: a dictionary of labels (keys) with a list of seed words (values)
    '''
    #reverse seeds dictionary
    genres = {}
    for genre,seed_words in seeds.items():
        for seed_word in seed_words:
            genres[seed_word] = genre
            
    data_ind = data.reset_index()
            
    model = fe.text.TfidfVectorizer(input="content", stop_words = {'english'})
    vector = model.fit_transform(data["sentence"])
    features = model.get_feature_names_out()
    
    def predict(ind):
        filtered = filter(lambda item: item[1] in genres, zip(vector[ind].toarray()[0].tolist(),features))
        prediction = max(filtered, key=lambda item: item[0])
        return genres[prediction[1]]
    
    df = data_ind.assign(prediction = data_ind["index"].apply(predict))
    return df

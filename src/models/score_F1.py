import sklearn.metrics as m


def score_F1(labels, predictions, averaging="micro"):
    '''
    Returns the micro F1 score given a list of labels and a list of predictions
    
    :param: labels: a list of labels
    :param: predictions: a list of predictions
    :param: averaging: type of averaging method to use
    '''
    score = m.f1_score(labels, predictions, average=averaging)
    return score

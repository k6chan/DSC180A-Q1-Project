import sklearn.metrics as m
import os


def score_F1(labels, predictions, outpath, averaging="micro"):
    '''
    Returns the micro F1 score given a list of labels and a list of predictions. Appends result to text file in outpath.
    
    :param: labels: a list of labels
    :param: predictions: a list of predictions
    :param: averaging: type of averaging method to use
    :param: outpath: filepath to append result to
    '''
    score = m.f1_score(labels, predictions, average=averaging)
    with open(os.path.join(outpath, "f1" + averaging + ".txt"), "a") as f:
        f.write(str(score) + "\n")
    return score

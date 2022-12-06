# DSC180A-Q1-Project

## Obtaining the raw data

Rename the following files and place in `data/raw`:

### New York Times

https://github.com/dheeraj7596/ConWea/tree/master/data/nyt/coarse

`df.pkl` --> `nyt_coarse.pkl`

`seedwords.json` --> `nyt_seedwords.json`

### 20News

https://github.com/dheeraj7596/ConWea/tree/master/data/20news/coarse

`df.pkl` --> `20News_coarse.pkl`

`seedwords_6.json` --> `20News_seedwords.json`

## Targets

* `test`: run models with test data. Output in `test/testoutput`.
* `data`: run models with raw data. Output in `data/out`.

## Expected Output

```IR-TF-IDF Micro-F1 score for nyt_coarse.pkl 0.6361585841936324
IR-TF-IDF Macro-F1 score for nyt_coarse.pkl 0.49765851868243194
Word2Vec Micro-F1 score for nyt_coarse.pkl 0.8135681443567276
Word2Vec Macro-F1 score for nyt_coarse.pkl 0.439528007393392
IR-TF-IDF Micro-F1 score for 20News_coarse.pkl 0.4474505723204995
IR-TF-IDF Macro-F1 score for 20News_coarse.pkl 0.3368200155328446
Word2Vec Micro-F1 score for 20News_coarse.pkl 0.6804315679938661
Word2Vec Macro-F1 score for 20News_coarse.pkl 0.45457716477084364

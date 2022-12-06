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

```
IR-TF-IDF Micro-F1 score for nyt_coarse.pkl 0.6396286978398542
IR-TF-IDF Macro-F1 score for nyt_coarse.pkl 0.5046148411972979
Word2Vec Micro-F1 score for nyt_coarse.pkl 0.8276221046239263
Word2Vec Macro-F1 score for nyt_coarse.pkl 0.4667683310931686
IR-TF-IDF Micro-F1 score for 20News_coarse.pkl 0.4760939810504409
IR-TF-IDF Macro-F1 score for 20News_coarse.pkl 0.3243792955989756
Word2Vec Micro-F1 score for 20News_coarse.pkl 0.6397940741552112
Word2Vec Macro-F1 score for 20News_coarse.pkl 0.42540999532068785
```

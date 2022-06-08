# twtr

twtr is a package used to process and normalize the text data as part of NLP. twtr can be applied to DataFrame or Series only. twtr will clean the text data by removing URLs, Twitter handles, special characters, stop words, and small words (<=3). In the final step, processed text data will be normalized using spacy's lemmatizer.

# Pre-requisites
spacy
en-core-web-sm

You may use pip to install them.

# Usage
```
import pandas as pd

tweet = ['@pro_player I was a great player', '@lcoal Michalle sang in 1940, really great','@mania Why! so great']
rank = [1,2,3]
sample = pd.DataFrame(list(zip(rank,tweet)),columns=['Rank','text'])

from twtr_package import twtr
print(twtr.process(sample, 'text'))

"""
Output: 
0                  great player
1    michalle sing really great
2                         great
Name: text, dtype: object
"""
```

#Sentiment Analysis: Biden Statements on Climate Change
#Tokenization

#Importing relevant packages 
import os
import pandas as pd
import nltk
import nltk.corpus
from nltk.tokenize import word_tokenize
from biden_statement_database import biden_climate_statements
from nltk.probability import FreqDist
from nltk.tokenize import blankline_tokenize
from nltk.util import bigrams, trigrams, ngrams
from nltk.stem import wordnet
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import string
import re

#Tokenizing the statements from the previously created dataframe

#This will create a new column in the dataframe, "Tokens", as well as a list containing all tokens from every Biden statement
all_tokens = []  # Create an empty list to store all tokens

for index, row in biden_climate_statements.iterrows():
    text = row['Text']
    tokens = word_tokenize(text)
    all_tokens.extend(tokens)  # Extend the list with tokens from each row
        
#Counting the number of times any given word is used in the statements
fdist = FreqDist()
for word in all_tokens:
    fdist[word.lower()]+=1
fdist

fdist_top10 = fdist.most_common(10)


#Getting rid of punctuation, numbers, and English stopwords

punctuation = re.compile(f"[{re.escape(string.punctuation)}]")
numbers = re.compile(r"\d+")

post_punctuation = []
for word in all_tokens:
    word_without_punct = punctuation.sub("", word)
    word_without_punct_and_numbers = numbers.sub("", word_without_punct)
    if len(word_without_punct_and_numbers) > 0:
        post_punctuation.append(word_without_punct_and_numbers)
        
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

post_processed = []
for word in post_punctuation:
    if word.lower() not in stop_words:
        lemmatized_word = lemmatizer.lemmatize(word)
        post_processed.append(lemmatized_word)

        
#Removing the stopwords directly from the Biden statements dataframe
# Remove stop words from the "Text" column
stop_words = set(stopwords.words('english'))
biden_climate_statements['Text'] = biden_climate_statements['Text'].apply(lambda text: ' '.join([word for word in text.split() if word.lower() not in stop_words]))



#Following along with Rob Mulla video

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import nltk
plt.style.use('ggplot')

tagged = nltk.pos_tag(post_processed)



# VADER Sentiment Scoring
from nltk.sentiment import SentimentIntensityAnalyzer
from tqdm.notebook import tqdm

sia = SentimentIntensityAnalyzer()

#Running polarity score on all tokens
for row in tqdm(post_processed):
    sia.polarity_scores(row)

res = {}
for i, row in tqdm(biden_climate_statements.iterrows(), total = len(biden_climate_statements)):
    text = row['Text']
    title = row['Title']
    res[title] = sia.polarity_scores(text)
    
vaders = pd.DataFrame(res).T
vaders = vaders.reset_index().rename(columns={'index': "Title"})
vaders = vaders.merge(biden_climate_statements, how ='left')



        




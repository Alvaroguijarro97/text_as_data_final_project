# import the dataset

import sqlite3

import pandas as pd


import re

# Connect to the database
conn = sqlite3.connect('data/us_pres_climate_speeches_more_climate.db')
cursor = conn.cursor() # Create a cursor object

# Select all data from the table
query = f'SELECT * FROM {'us_pres_climate_speeches_more_climate'};'
cursor.execute(query)

# create a DataFrame
df_speeches = pd.read_sql_query(query, conn)

# close connection
conn.close()


### Some adjusts
# Convert column names to lowercase
df_speeches.columns = [col.lower() for col in df_speeches.columns] 

# Create a map speaker/party
party_mapping = {
    'George W. Bush': 'Republican',
    'Barack Obama': 'Democratic',
    'Donald Trump': 'Republican',
    'Joe Biden': 'Democratic'
}

# Create a new column 'party' based on the mapping
df_speeches['party'] = df_speeches['speaker'].map(party_mapping)

# Convert the 'date' column to datetime
df_speeches['date'] = pd.to_datetime(df_speeches['date'], format='%d/%m/%Y')

## drops the end of every speech that contains " NOTE:."
df_speeches['text'] = df_speeches['text'].apply(lambda x: re.sub(r' NOTE: .*$', '', x))


### Tidy data
from nltk.corpus import stopwords

# get lowercase speeches
df_speeches['cleaned_speech'] = df_speeches['text'].str.lower()

# Remove special characters, numbers, and symbols
df_speeches['cleaned_speech'] = df_speeches['cleaned_speech'].replace(to_replace=r'[^a-zA-Z0-9\s]', value='', regex=True) # drop punctuation and special char
df_speeches['cleaned_speech'] = df_speeches['cleaned_speech'].replace(to_replace=r'\b\d+\b', value='', regex=True) # drop numbers

# Remove stop words
stop_words = set(stopwords.words('english')) # get the list of stopwords

def remove_stop_words(text): #define a function to remove stopwords
    words = text.split()
    filtered_words = [word for word in words if word not in stop_words] # compare each word with the list of stopwords
    return ' '.join(filtered_words)

df_speeches['cleaned_speech'] = df_speeches['cleaned_speech'].apply(remove_stop_words) # apply the function to each row

#drop some unnecessary columns
columns_to_drop = ["url", "title"]
df_speeches_cleanned = df_speeches.drop(columns=columns_to_drop)


### stemming and tokenization
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

# Stemming
stemmer = PorterStemmer()

# Define a function for stemming
def stem_text(text):
    stemmed_words = [stemmer.stem(word) for word in text.split()] # Split the text into words and apply stemming to each word
    return ' '.join(stemmed_words) # Join the stemmed words back into a sentence
    
# Apply the stem_text function to each cleaned speech
df_speeches_cleanned['cleaned_speech'] = df_speeches_cleanned['cleaned_speech'].apply(stem_text)



### Tokenization
# Define a function
def tokenize_text(text):
    return word_tokenize(text)

df_speeches_cleanned['tokens'] = df_speeches_cleanned['cleaned_speech'].apply(tokenize_text)  #apply the function

# import the dataset


import sqlite3
import pandas as pd

# Connect to the SQLite database
conn = sqlite3.connect('data/us_pres_climate_speeches_final.db')
cursor = conn.cursor() # Create a cursor object

# Select all data from the table
query = f'SELECT * FROM {'us_pres_climate_speeches_final'};'
cursor.execute(query)

# Fetch all the data and store it in a pandas DataFrame
df_speeches = pd.read_sql_query(query, conn)

conn.close()

# Convert column names to lowercase
df_speeches.columns = [col.lower() for col in df_speeches.columns] 

# Create a variable with party
party_mapping = {
    'George W. Bush': 'Republican',
    'Barack Obama': 'Democratic',
    'Donald Trump': 'Republican',
    'Joe Biden': 'Democratic'
}

# Create a new column 'party' based on the mapping
df_speeches['party'] = df_speeches['speaker'].map(party_mapping)

#
# Convert the 'date' column to datetime
df_speeches['date'] = pd.to_datetime(df_speeches['date'], format='%d/%m/%Y')

# Tidying data
from nltk.corpus import stopwords


# get lowercase tweets
df_speeches['cleaned_speech'] = df_speeches['text'].str.lower()

# Remove special characters, numbers, and symbols
df_speeches['cleaned_speech'] = df_speeches['cleaned_speech'].replace(to_replace=r'[^a-zA-Z0-9\s]', value='', regex=True) # drop punctuation and special char
df_speeches['cleaned_speech'] = df_speeches['cleaned_speech'].replace(to_replace=r'\b\d+\b', value='', regex=True) # drop numbers
#df_speeches['cleaned_speeches_with_SW'] = df_speeches['lowercase_speeches'].str.replace('[^\\w\\s]', '').replace(to_replace=r'\d', value='', regex=True)

# Remove stop words
stop_words = set(stopwords.words('english')) # get the list of stopwords

def remove_stop_words(text): #define a function to remove stopwords
    words = text.split()
    filtered_words = [word for word in words if word not in stop_words] # compare each word with the list of stopwords
    return ' '.join(filtered_words)

df_speeches['cleaned_speech'] = df_speeches['cleaned_speech'].apply(remove_stop_words) # apply the function to each row

#drop some unnecessary columns
columns_to_drop = ["url", "title"]
df = df_speeches.drop(columns=columns_to_drop)



# stemming and tokenization
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

# Lemmatization/Stemming
stemmer = PorterStemmer()

# Define a function for stemming
def stem_text(text):
    stemmed_words = [stemmer.stem(word) for word in text.split()] # Split the text into words and apply stemming to each word
    return ' '.join(stemmed_words) # Join the stemmed words back into a sentence
    
# Apply the stem_text function to each cleaned speech
df['stemmed_speech'] = df['cleaned_speech'].apply(stem_text)



# Tokenization
# Define a function
def tokenize_text(text):
    return word_tokenize(text)


df['tokens'] = df['stemmed_speech'].apply(tokenize_text)  #apply the function

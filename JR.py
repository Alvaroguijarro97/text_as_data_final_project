
#remove work thats using string replace

df_speeches_cleanned['cleaned_speech'] = df_speeches_cleanned['cleaned_speech'].str.replace('thats', '')



# get lowercase speeches
df_speeches['speech_JR'] = df_speeches['text'].str.lower()

# Remove special characters, numbers, and symbols
df_speeches['speech_JR'] = df_speeches['speech_JR'].replace(to_replace=r'[^a-zA-Z0-9\s]', value='', regex=True) # drop punctuation and special char
df_speeches['speech_JR'] = df_speeches['speech_JR'].replace(to_replace=r'\b\d+\b', value='', regex=True) # drop numbers


# Remove stop words
stop_words = set(stopwords.words('english')) # get the list of stopwords

def remove_stop_words(text): #define a function to remove stopwords
    words = text.split()
    filtered_words = [word for word in words if word not in stop_words] # compare each word with the list of stopwords
    return ' '.join(filtered_words)

df_speeches['speech_JR'] = df_speeches['speech_JR'].apply(remove_stop_words) # apply the function to each row

#add word thats to stop words

stop_words.add('thats')

#apply again

df_speeches['speech_JR'] = df_speeches['speech_JR'].apply(remove_stop_words) # apply the function to each row

#check variables

df_speeches.columns

#unique speakers

df_speeches['speaker'].unique()

#save the dataframe as db

import sqlite3

conn = sqlite3.connect('data/df_speeches_word.db')

df_speeches.to_sql('df_speeches_word', conn, if_exists='replace', index=False)

conn.close()

#load the dataframe

df_speeches = pd.read_csv('data/df_word_cloud.csv')

#wordcloud of biden

from wordcloud import WordCloud

# Create a WordCloud object

biden_wc = WordCloud(background_color="white", max_words=1000, contour_width=3, contour_color='steelblue')

# Generate a word cloud

biden_wc.generate(df_speeches[df_speeches['speaker'] == 'Joe Biden']['speech_JR'].str.cat(sep=" "))

#show the wordcloud

biden_wc.to_image()

#now do one image for all presidents. separate it by speaker



# Create a connection object using the connect function
conn = sqlite3.connect('df_speeches.db')

# Write the data to a sqlite table
df_speeches.to_sql('speeches_table', conn, if_exists='replace', index=False)

# Close the connection
conn.close()


from wordcloud import WordCloud
import matplotlib.pyplot as plt

# List of Presidents
presidents = ['George W. Bush', 'Barack Obama', 'Joe Biden']

# Create a figure to display the word clouds
fig, axes = plt.subplots(1, 3, figsize=(20, 10))

for i, president in enumerate(presidents):
    # Filter the DataFrame for each president
    text = df_speeches[df_speeches['speaker'] == president]['speech_JR'].str.cat(sep=" ")

    # Create a WordCloud object
    wordcloud = WordCloud(background_color="white", max_words=1000, contour_width=3, contour_color='steelblue')

    # Generate a word cloud
    wordcloud.generate(text)

    # Display the word cloud
    axes[i].imshow(wordcloud, interpolation='bilinear')
    axes[i].set_title(president, fontsize=40)
    axes[i].axis('off')

# Adjust layout
plt.tight_layout()
plt.show()


#save the wordcloud

fig.savefig('data/wordcloud.png', dpi=300)



from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
wordnet_m = {"N":wordnet.NOUN, "V":wordnet.VERB, "J":wordnet.ADJ, "R":wordnet.ADV}
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
import nltk

nltk.download('vader_lexicon')

def lemmat_pos_word(text):

    
    pos_tagger_text = nltk.pos_tag(text.split())
    
    return " ".join([lemmatizer.lemmatize(word, wordnet_m.get(pos[0],wordnet.NOUN)) for word,pos in pos_tagger_text])

from IPython.display import HTML

from nltk.sentiment.vader import SentimentIntensityAnalyzer
sid = SentimentIntensityAnalyzer()

from sklearn.feature_extraction.text import CountVectorizer

df_speeches['lemma_text_JR'] = df_speeches['speech_JR'].apply(lambda T : lemmat_pos_word(T))


df_speeches['scores'] = df_speeches['lemma_text_JR'].apply(lambda review: sid.polarity_scores(review))

df_speeches['compound']  = df_speeches['scores'].apply(lambda score_dict: score_dict['compound'])

df_speeches['Negative']  = df_speeches['scores'].apply(lambda score_dict: score_dict['neg'])

df_speeches['Neutral']  = df_speeches['scores'].apply(lambda score_dict: score_dict['neu'])

df_speeches['Positive']  = df_speeches['scores'].apply(lambda score_dict: score_dict['pos'])

df_speeches['number_of_words'] = df_speeches['speech_JR'].str.split().apply(lambda x: len(x))


#give me the total number of words for all the speeches in bush with count

df_speeches[df_speeches['speaker'] == 'George W. Bush']['number_of_words'].sum()

#now obama

df_speeches[df_speeches['speaker'] == 'Barack Obama']['number_of_words'].sum()

from collections import Counter

# Preprocess and count words
count = Counter()
for text in df_speeches['speech_JR'].values:
    # Convert to lowercase and split into words
    words = text.lower().split()
    count.update(words)


# Remove stopwords if needed (optional)
# from nltk.corpus import stopwords
# stop_words = set(stopwords.words('english'))
# count = Counter({word: freq for word, freq in count.items() if word not in stop_words})

# Get the top 10 most common words
top_10_words = count.most_common(10)

# Display the top 10 words
top_10_words

#erase the word thats and people from df_speeches

df_speeches['speech_JR'] = df_speeches['speech_JR'].str.replace('thats', '')

df_speeches['speech_JR'] = df_speeches['speech_JR'].str.replace('people', '')

df_speeches['speech_JR'] = df_speeches['speech_JR'].str.replace('going', '')



def text_ngrams(corpus, n, g):
    vec = CountVectorizer(ngram_range=(g, g)).fit(corpus)
    bag_of_words = vec.transform(corpus)
    sum_words = bag_of_words.sum(axis=0) 
    words_freq = [(word, sum_words[0, idx]) for word, idx in vec.vocabulary_.items()]
    words_freq =sorted(words_freq, key = lambda x: x[1], reverse=True)
    return words_freq[:n]


freq_word = count.most_common(20)

freq_word_plot1 = pd.Series( (v[0] for v in freq_word) )
freq_word_plot2 = pd.Series( (v[1] for v in freq_word) )


data_freq = pd.DataFrame({'Words':freq_word_plot1,'Count':freq_word_plot2})
data_freq = data_freq.sort_values('Count')


# Assuming you have the speeches in variables: bush_speeches, obama_speeches, biden_speeches

from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def text_ngrams(corpus, n, g):
    vec = CountVectorizer(ngram_range=(g, g), stop_words='english').fit(corpus)
    bag_of_words = vec.transform(corpus)
    sum_words = bag_of_words.sum(axis=0)
    words_freq = [(word, sum_words[0, idx]) for word, idx in vec.vocabulary_.items()]
    return sorted(words_freq, key=lambda x: x[1], reverse=True)[:n]


bush_speeches = df_speeches[df_speeches['speaker'] == 'George W. Bush']['speech_JR'].values
obama_speeches = df_speeches[df_speeches['speaker'] == 'Barack Obama']['speech_JR'].values
biden_speeches = df_speeches[df_speeches['speaker'] == 'Joe Biden']['speech_JR'].values

# Extracting top 20 words for each president
top_words_bush = text_ngrams(bush_speeches, 20, 1)
top_words_obama = text_ngrams(obama_speeches, 20, 1)
top_words_biden = text_ngrams(biden_speeches, 20, 1)

# Function to plot the data
def plot_top_words(words_freq, title):
    df = pd.DataFrame(words_freq, columns=['Words', 'Count'])
    plt.figure(figsize=(12, 6))
    sns.barplot(data=df, y='Words', x='Count')
    plt.title(title)
    plt.tight_layout()
    plt.show()

# Plotting for each president
plot_top_words(top_words_bush, 'Top 20 Frequent Words in Bush\'s Speeches')
plot_top_words(top_words_obama, 'Top 20 Frequent Words in Obama\'s Speeches')
plot_top_words(top_words_biden, 'Top 20 Frequent Words in Biden\'s Speeches')


# Convert each list to a DataFrame and add a 'President' column
df_bush = pd.DataFrame(top_words_bush, columns=['Words', 'Count'])
df_bush['President'] = 'Bush'

df_obama = pd.DataFrame(top_words_obama, columns=['Words', 'Count'])
df_obama['President'] = 'Obama'

df_biden = pd.DataFrame(top_words_biden, columns=['Words', 'Count'])
df_biden['President'] = 'Biden'

# Combine the DataFrames
combined_df = pd.concat([df_bush, df_obama, df_biden])


# Increase the plot size and font scale for better readability
plt.figure(figsize=(18, 10))  # Increased figure size
sns.set_context('notebook', font_scale=1.5)  # Increase font scale

# Plotting
sns.barplot(data=combined_df, y='Words', x='Count', hue='President')
plt.title('Top Frequent Words in Presidential Speeches')
plt.tight_layout()
plt.show()


from nrclex import NRCLex



def Review_emo(word):
    """
    Function to convert the raw data to utf-8 formate
    
    * convert to data Frame
    
    """
    
    word = str([cell.encode('utf-8') for cell in word])# to convert the text into utf-8 unicode
    str_text = NRCLex(word) 
    str_text = str_text.raw_emotion_scores
    str_text = pd.DataFrame(str_text,index=[0])
    str_text = pd.melt(str_text)
    str_text.columns = ('Emotions','Count')
    str_text = str_text.sort_values('Count')
    
    return str_text


rating_clean = Review_emo(df_speeches['lemma_text_JR'])


plt.figure(figsize=(10,6))
sns.set_style('darkgrid')
sns.set_context(context='notebook',font_scale=1.5)
sns.barplot(y='Emotions',x='Count',data=rating_clean[0:8],)
plt.title('Emotional affects in Speech');
plt.tight_layout()
plt.show()


from nrclex import NRCLex
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Assuming df_bush_speeches, df_obama_speeches, df_biden_speeches contain the processed speech data for each president

def Review_emo(text):
    # Ensure text is a single string
    if isinstance(text, (list, np.ndarray)):
        text = ' '.join(map(str, text))
    # Encode to UTF-8
    text = text.encode('utf-8').decode('utf-8')
    # Analyze the emotion content of the text
    str_text = NRCLex(text)
    emotion_scores = str_text.raw_emotion_scores
    # Convert to DataFrame for easier manipulation
    emotion_df = pd.DataFrame(list(emotion_scores.items()), columns=['Emotions', 'Count'])
    # Return sorted DataFrame
    return emotion_df.sort_values('Count', ascending=False)

# Analyze emotions in speeches by each speaker

df_bush_speeches = df_speeches[df_speeches['speaker'] == 'George W. Bush']['lemma_text_JR'].values

#give me the total number of words for all the speeches in bush with count








df_obama_speeches = df_speeches[df_speeches['speaker'] == 'Barack Obama']['lemma_text_JR'].values

df_biden_speeches = df_speeches[df_speeches['speaker'] == 'Joe Biden']['lemma_text_JR'].values

# Compute emotion scores for each president
emotions_bush = Review_emo(df_bush_speeches)
emotions_obama = Review_emo(df_obama_speeches)
emotions_biden = Review_emo(df_biden_speeches)

#give me the count of words for all the speeches in obama

df_obama_speeches = df_speeches[df_speeches['speaker'] == 'Barack Obama']['lemma_text_JR'].values

df_obama_speeches = str([cell.encode('utf-8') for cell in df_obama_speeches])

df_obama_speeches = NRCLex(df_obama_speeches)

df_obama_speeches = df_obama_speeches.raw_emotion_scores

df_obama_speeches = pd.DataFrame(df_obama_speeches,index=[0])

df_obama_speeches = pd.melt(df_obama_speeches)

df_obama_speeches.columns = ('Emotions','Count')

df_obama_speeches = df_obama_speeches.sort_values('Count')

df_obama_speeches

# Add a 'President' column to each DataFrame
emotions_bush['President'] = 'Bush'
emotions_obama['President'] = 'Obama'
emotions_biden['President'] = 'Biden'

# Combine the DataFrames
combined_emotions = pd.concat([emotions_bush, emotions_obama, emotions_biden])

# Plotting
plt.figure(figsize=(12, 8))
sns.set_style('darkgrid')
sns.set_context(context='notebook', font_scale=1.5)
sns.barplot(y='Emotions', x='Count', hue='President', data=combined_emotions)
plt.title('Emotional Affects in Presidential Speeches')
plt.tight_layout()
plt.show()




import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from nrclex import NRCLex

def Review_emo(text):
    # Ensure text is a single string and encode to UTF-8 if not already
    if isinstance(text, list):
        text = ' '.join(text)
    text = text.encode('utf-8').decode('utf-8')
    # Analyze the emotion content of the text
    str_text = NRCLex(text)
    emotion_scores = str_text.raw_emotion_scores
    # Convert to DataFrame for easier manipulation
    emotion_df = pd.DataFrame(list(emotion_scores.items()), columns=['Emotions', 'Count'])
    # Return sorted DataFrame
    return emotion_df.sort_values('Count', ascending=False)
# Analyze emotions in speeches by each speaker

bush_emotions = Review_emo(' '.join(df_speeches[df_speeches['speaker'] == 'George W. Bush']['lemma_text_JR']))
obama_emotions = Review_emo(' '.join(df_speeches[df_speeches['speaker'] == 'Barack Obama']['lemma_text_JR']))
biden_emotions = Review_emo(' '.join(df_speeches[df_speeches['speaker'] == 'Joe Biden']['lemma_text_JR']))

# Visualization for one of the speakers (example: Barack Obama)
plt.figure(figsize=(10, 6))
sns.set_style('darkgrid')
sns.set_context('notebook', font_scale=1.5)
sns.barplot(y='Emotions', x='Count', data=obama_emotions.head(8))
plt.title('Emotional Affects in Barack Obama\'s Speeches')
plt.tight_layout()
plt.show()

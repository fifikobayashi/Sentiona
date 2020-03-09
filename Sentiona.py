import tweepy
import numpy as np 
import pandas as pd 
import re  
import nltk 
nltk.download('stopwords')  
from nltk.corpus import stopwords 
from tweepy import OAuthHandler
 
#connection to twitter API
consumer_api_key = 'USE_YOUR_OWN'
consumer_api_secret = 'USE_YOUR_OWN' 
access_token = 'USE_YOUR_OWN'
access_token_secret ='USE_YOUR_OWN'
authorizer = OAuthHandler(consumer_api_key, consumer_api_secret)
authorizer.set_access_token(access_token, access_token_secret)

# tweet extraction
api = tweepy.API(authorizer ,timeout=15)

# initiates an empty array 
all_tweets = []

# asks user for the search term 
search_query = input("Enter a subject matter for analysis:  ")

# calls Cursor object with the following params
#    1. operation type
#    2. search query + exclusion of retweets for now
#    3. further filtering tweets by language
#    4. number of tweets to return
for tweet_object in tweepy.Cursor(api.search,q=search_query+" -filter:retweets",lang='en',result_type='recent').items(300):
    all_tweets.append(tweet_object.text)

# load twitter dataset
tweets = pd.read_csv("blah") # you'll need to download a decent sized data set or read directly from an existing source online
                             # e.g. https://raw.githubusercontent.com/kolaveridi/kaggle-Twitter-US-Airline-Sentiment-/master/Tweets.csv
 
# divide data into label and feature sets
foo = tweets.iloc[:, 10].values  
bar = tweets.iloc[:, 1].values
 
processed_tweets = []

# remove special chars/empty spaces from the training dataset
for tweet in range(0, len(foo)):  
    # remove all the special characters
    processed_tweet = re.sub(r'\W', ' ', str(foo[tweet]))
 
    # remove all single characters
    processed_tweet = re.sub(r'\s+[a-zA-Z]\s+', ' ', processed_tweet)
 
    # remove single characters from the start
    processed_tweet = re.sub(r'\^[a-zA-Z]\s+', ' ', processed_tweet) 
 
    # substituting multiple spaces with single space
    processed_tweet= re.sub(r'\s+', ' ', processed_tweet, flags=re.I)
 
    # removing prefixed 'b'
    processed_tweet = re.sub(r'^b\s+', '', processed_tweet)
 
    # converting to Lowercase
    processed_tweet = processed_tweet.lower()
 
    processed_tweets.append(processed_tweet)

# use the TFIDF scheme to convert text to numbers    
from sklearn.feature_extraction.text import TfidfVectorizer  
tfidfconverter = TfidfVectorizer(max_features=2000, min_df=5, max_df=0.7, stop_words=stopwords.words('english'))  
foo = tfidfconverter.fit_transform(processed_tweets).toarray()

# training sentimental analysis model
from sklearn.ensemble import RandomForestClassifier
text_classifier = RandomForestClassifier(n_estimators=100, random_state=0)  
text_classifier.fit(foo, bar)

# remove special chars/empty spaces from the scraped tweets
for tweet in all_tweets:
    # remove all the special characters
    processed_tweet = re.sub(r'\W', ' ', tweet)
 
    # remove all single characters
    processed_tweet = re.sub(r'\s+[a-zA-Z]\s+', ' ', processed_tweet)
 
    # remove single characters from the start
    processed_tweet = re.sub(r'\^[a-zA-Z]\s+', ' ', processed_tweet) 
 
    # substituting multiple spaces with single space
    processed_tweet= re.sub(r'\s+', ' ', processed_tweet, flags=re.I)
 
    # removing prefixed 'b'
    processed_tweet = re.sub(r'^b\s+', '', processed_tweet)
 
    # converting to Lowercase
    processed_tweet = processed_tweet.lower()
 
    sentiment = text_classifier.predict(tfidfconverter.transform([ processed_tweet]).toarray())
    
    # prints out the extracted tweets with the analysed sentiment
    print(processed_tweet ,'SENTIMENT-->', sentiment)
    
    # append the same line (typecasted to str) to a local file for subsequent counting
    writeStream = open("foobar.txt","a+")
    writeStream.write(str(sentiment))

writeStream.close()

# opens the local file
readStream = open("foobar.txt","r").read()

# initialise each sentiment param
positive = "['positive']"
negative = "['negative']"
neutral = "['neutral']"

# count occurrence of each sentiment
posCount = readStream.count(positive)
negCount = readStream.count(negative)
neuCount = readStream.count(neutral)

# print out a summary of sentiments
print('Summary on: ' + search_query)
print('Positive Sentiments: ' + str(posCount)) # had to typecast int to str since print() can't concat two types
print('Negative Sentiments: ' + str(negCount))
print('Neutral Sentiments: ' + str(neuCount))
print('***Analysis Complete***')

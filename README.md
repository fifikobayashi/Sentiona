# Sentiona (Beta)
Sentiment Analytics Framework

My first cut of a python-based Sentiment Analytics framework that canvases cryptotwitter sentiments towards a particular project/personality.

It runs on live twitter data via the Twitter API and uses an existing machine learning dataset to train the sentiment analysis model. 

This concept isn't new but it obviously would need a lot more training to be aware of nuances on cryptotwitter.

I've also set the retrieval to time out after 150 seconds to avoid spamming the twitter API.

![screenshot](https://raw.githubusercontent.com/fifikobayashi/Sentiona/master/%24HEX.png)

# Setup:

1. Apply to Twitter to become a Twitter Developer
https://developer.twitter.com/content/developer-twitter/en.html

2. Extract the API key, API secret key, Access token and Access token secret from your developer app page
https://developer.twitter.com/en/apps and update the following initialization parameters 
```
#connection to twitter API
consumer_api_key = 'USE_YOUR_OWN'
consumer_api_secret = 'USE_YOUR_OWN' 
access_token = 'USE_YOUR_OWN'
access_token_secret ='USE_YOUR_OWN'
```

3. Clone this repo
```
git clone https://github.com/fifikobayashi/Sentiona
cd Sentiona
```

4. install dependencies
```
pip3 install numpy
pip3 install pandas
pip3 install matplotlib
pip3 install seaborn
pip3 install nltk
pip3 install sklearn
```

5. update the dataset to be loaded in the code "tweets = pd.read_csv()" to point to your trained ML models
```
# load twitter dataset
tweets = pd.read_csv("https://....
```

6. To execute, just run 
```
python3 Sentiona.py
```

# Notes on dependencies:

- Dependencies (numpy, pandas, matplotlib, seaborn, nltk)

- Twitter API - you'll need your own access token and api key by applying for a developer account with Twitter

- Training Dataset - you can make your own or just point the code to an existing model e.g. https://raw.githubusercontent.com/kolaveridi/kaggle-Twitter-US-Airline-Sentiment-/master/Tweets.csv
The analysis is only as good as the training model you feed it.


# Built upon techniques and samples from the following projects/articles:

https://towardsdatascience.com/creating-the-twitter-sentiment-analysis-program-in-python-with-naive-bayes-classification-672e5589a7ed

https://github.com/g3n1uss/generating-reviews-discovering-sentiment

https://python.gotrained.com/scraping-tweets-sentiment-analysis/  


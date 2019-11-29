# Sentiona (Beta)
Sentiment Analytics Framework

My first cut of a python-based Sentiment Analytics framework that canvases cryptotwitter sentiments towards a particular project/personality.

It runs on live twitter data via the Twitter API and uses an existing machine learning dataset to train the sentiment analysis model. 

This concept isn't new but it obviously would need a lot more training to be aware of nuances on cryptotwitter.

I've also set the retrieval to time out after 15 seconds to avoid spamming the twitter API.

# Pre-requisites to running the code:

- Dependencies (numpy, pandas, matplotlib, seaborn, nltk)

- Twitter API - you'll need your own access token and api key by applying for a developer account with Twitter

- Training Dataset - you can make your own or just point the code to an existing model e.g. https://raw.githubusercontent.com/kolaveridi/kaggle-Twitter-US-Airline-Sentiment-/master/Tweets.csv
The analysis is only as good as the training model you feed it.


# Techniques utilised from the following projects:

https://towardsdatascience.com/creating-the-twitter-sentiment-analysis-program-in-python-with-naive-bayes-classification-672e5589a7ed

https://github.com/g3n1uss/generating-reviews-discovering-sentiment

https://python.gotrained.com/scraping-tweets-sentiment-analysis/  


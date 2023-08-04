import tweepy
from textblob import TextBlob

consumer_key = "YOUR_CONSUMER_KEY"
consumer_secret = "YOUR_CONSUMER_SECRET"
access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


search_query = "Python programming"
tweet_count = 100

tweets = tweepy.Cursor(api.search, q=search_query, lang="en").items(tweet_count)


positive = 0
neutral = 0
negative = 0

for tweet in tweets:
    analysis = TextBlob(tweet.text)
    polarity = analysis.sentiment.polarity
    
    if polarity > 0:
        positive += 1
    elif polarity < 0:
        negative += 1
    else:
        neutral += 1


total = positive + neutral + negative
print(f"Total tweets analyzed: {total}")
print(f"Positive tweets: {positive} ({(positive / total) * 100:.2f}%)")
print(f"Neutral tweets: {neutral} ({(neutral / total) * 100:.2f}%)")
print(f"Negative tweets: {negative} ({(negative / total) * 100:.2f}%)")

pos_tweets = [tweet for index, tweet in enumerate(data['Tweets']) if data['SA'][index]>0]
neu_tweets = [tweet for index, tweet in enumerate(data['Tweets']) if data['SA'][index]==0]
neg_tweets = [tweet for index, tweet in enumerate(data['Tweets']) if data['SA'][index]<0]
print(pos_tweets, neu_tweets, neg_tweets)
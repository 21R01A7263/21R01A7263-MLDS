data['SA'] = np.array([analyze_sentiment(tweet) for tweet in data['Tweets']])
display(data.head(10))
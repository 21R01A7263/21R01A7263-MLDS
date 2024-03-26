data = pd.DataFrame(data=[tweet.text for tweet in tweets],columns=['Tweets'])
display(data.head(5))

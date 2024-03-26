extractor = twitter_setup()
tweets = extractor.user_timeline(screen_name="Username of Twitter Account",count=200)
print("Number of tweets extracted: {}.\n".format(len(tweets)))
print("13 recent tweets:\n")
for tweet in tweets[:13]:
  print(tweet.text)
  print()

def twitter_setup():
  auth = tweepy.OAuthHandler("API Key", "API Secret")
  auth.set_access_token("Access Key", "Access Token")
  api=tweepy.API(auth)
  return api

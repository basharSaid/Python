
import tweepy

# Erstellen Variablen für jeden Schlüssel, jedes Geheimnis, Token
consumer_key = 'M9IDTmR8sz0bLszvnJGZUrZ2Y'
consumer_secret = 'iIZgJKWnyVJXBPtBEfj0WMC8iu05vKyUqCvFxzvc3hrNx6cpEu'
access_token = '950698147285782528-MTf3FjctNI6kWK3ZaAhvZymCj6zkRtW'
access_token_secret = 'ALh42aZznSjvMIkh1QPQ1sZbLDpFD6MbhJVLYFqQJilln'

# Richten OAuth ein und integrieren es mit der API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Schreibe Tweet, um zu Twitter-Account zu gelangen
tweet = 'Hi Everyone'
api.update_status(status=tweet)

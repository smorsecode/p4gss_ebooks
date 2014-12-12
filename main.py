import random, time, tweepy
from requests_oauthlib import OAuth1Session, OAuth2Session

def getQuote(used):
	quotes = []

	with open("sas.txt", 'r') as f:
		q = str.split(f.read(), '\n')

		for quote in q:
			if quote != "":

				quotes.append(quote)

	with open("flyingstaplers.txt", 'r') as f:
		q = str.split(f.read(), '\n')

		for quote in q:
			if quote != "":

				quotes.append(quote)

	with open("noxxels.txt", 'r') as f:
		q = str.split(f.read(), '\n')

		for quote in q:
			if quote != "":

				quotes.append(quote)

	with open("drunkspar.txt", 'r') as f:
		q = str.split(f.read(), '\n')

		for quote in q:
			if quote != "":

				quotes.append(quote)


	acceptable = False
	while not acceptable:
		index = random.randrange(0, len(quotes) - 1)
		print str(index) + " total: "+ str(len(quotes)) + " used " + str(len(used))
		quote = quotes[index]

		acceptable = True
		for q in used:
			if quote == q:
				acceptable = False
				break


	used.append(quote)
	return quote

def twitterInit():
	twitter = OAuth1Session(twitter_key, client_secret=twitter_secret, callback_uri="http://www.lycaon.me")
	twitter.fetch_request_token(twitter_request_token_url)
	authorization_url = twitter.authorization_url(twitter_authorization_base_url)
	print 'Please go here and authorize: ', authorization_url
	redirect_response = raw_input("Paste the full redirect URL here: ")
	twitter.parse_authorization_response(redirect_response)
	token = twitter.fetch_access_token(twitter_access_token_url)

	return token

############
#Initialize#
############
used = []

twitter_key = r'TWITTER_KEY'
twitter_secret = r'TWITTER_SECRET'

twitter_request_token_url = 'https://api.twitter.com/oauth/request_token'
twitter_authorization_base_url = 'https://api.twitter.com/oauth/authorize'
twitter_access_token_url = "https://api.twitter.com/oauth/access_token"

######
#Main#
######

twitterToken = twitterInit()
auth = tweepy.OAuthHandler(twitter_key, twitter_secret)
auth.set_access_token(twitterToken["oauth_token"], twitterToken["oauth_token_secret"])
twitter = tweepy.API(auth)

while True:

	if random.randrange(0, 100) == 0:
		used = []
	try:
		quote = getQuote(used)
		print quote
		twitter.update_status(quote)
	except tweepy.error.TweepError:
		pass
	else:
		time.sleep(random.randrange(3600, 18000))


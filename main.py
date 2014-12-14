import random, time, tweepy, urllib2
from requests_oauthlib import OAuth1Session, OAuth2Session
from PIL import Image, ImageFont, ImageDraw

def getQuote(used):
	quotes = []
	
	member = random.randint(0, 4)
	print member
	if member == 0:
	
		f = urllib2.urlopen("https://raw.githubusercontent.com/LycaonIsAWolf/p4gss_ebooks/master/sas.txt")
		q = str.split(f.read(), '\n')

		for quote in q:
			if quote != "":
			
				quotes.append(quote)
	elif member == 1:
		f = urllib2.urlopen("https://raw.githubusercontent.com/LycaonIsAWolf/p4gss_ebooks/master/flyingstaplers.txt", 'r')
		q = str.split(f.read(), '\n')

		for quote in q:
			if quote != "":
				quotes.append(quote)
	
	elif member == 2:
		f = urllib2.urlopen("https://raw.githubusercontent.com/LycaonIsAWolf/p4gss_ebooks/master/noxxels.txt", 'r')
		q = str.split(f.read(), '\n')

		for quote in q:
			if quote != "":

				quotes.append(quote)
	elif member == 3:
		f = urllib2.urlopen("https://raw.githubusercontent.com/LycaonIsAWolf/p4gss_ebooks/master/drunkspar.txt", 'r')
		q = str.split(f.read(), '\n')

		for quote in q:
			if quote != "":
				quotes.append(quote)

	elif member == 4:
		f = urllib2.urlopen("https://raw.githubusercontent.com/LycaonIsAWolf/p4gss_ebooks/master/lycaon.txt", 'r')
		q = str.split(f.read(), '\n')

		for quote in quotes:
		
			if quote != "" and quote != '\n':
				quotes.append(quote)

	acceptable = False
	while not acceptable:
		index = random.randrange(0, len(quotes) - 1)
		print str(index) + " total: "+ str(len(quotes)) + " used " + str(len(used))
		quote = quotes[index]

		acceptable = True
		for q in used:
			if quote == q or quote == "" or quote == "\n":
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

def separate(s):
	words = s.split(' ')

	mid = words[int(len(words)/2)]

	midpoint = words.index(mid)

	firstHalf = words[:midpoint]
	lastHalf = words[midpoint:]

	return [(''.join(firstHalf[i] + ' ' for i in range(len(firstHalf)))), (''.join(lastHalf[i] + ' ' for i in range(len(lastHalf)) ))]

############
#Initialize#
############
used = []

twitter_key = r'KEY'
twitter_secret = r'SECRET'

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

totalQuotes = 0

while True:

	if random.randrange(0, 100) == 0:
		used = []
	if(random.randint(0, 1) == 0):
		try:
			quote = getQuote(used)
			print quote
			twitter.update_status(quote)
		except tweepy.error.TweepError:
			pass
		else:
			sleepTime = random.randrange(3600, 18000)
			print sleepTime
			time.sleep(sleepTime)
	else:
		try:
			quote = getQuote(used)
			print quote + " (put on crab nebula)"

			crab = Image.open("crab_nebula.jpg")
			draw = ImageDraw.Draw(crab)
			font = ImageFont.truetype("alte_haas_grotesk.ttf", 100)

			totalPixelLength = len(quote) * 100

			if(totalPixelLength > crab.size[0]):
				quote = separate(quote)
				draw.text((300, 600), quote[0], font=font)
				draw.text((300, 700), quote[1], font=font)
				crab.save('quote.jpg')

			else:
				draw.text((300, 600), quote, font=font)
				crab.save('quote.jpg')
			
			twitter.update_with_media('quote.jpg')

		except tweepy.error.TweepError:
			pass
		else:
			sleepTime = random.randrange(3600, 18000)
			print sleepTime
			time.sleep(sleepTime)







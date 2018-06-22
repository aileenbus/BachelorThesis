import re

tweetsfile = open("2017_noretweet.txt", "r", encoding="utf-8")
mention = open("2017_mention.txt", "w", encoding="utf-8")

for tweet in tweetsfile.readlines():
	
	url_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
	tweet = re.sub(url_pattern, 'URL', tweet)
	
	mention_pattern = r'(?<=^|(?<=[^a-zA-Z0-9-_\.]))@([A-Za-z]+[A-Za-z0-9]+)'
	tweet = re.sub(mention_pattern, '@MENTION', tweet)

	mention.write(tweet)
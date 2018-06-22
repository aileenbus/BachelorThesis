tweetsfile = open("2017.txt", "r", encoding="utf-8")
noretweet = open("2017_noretweet.txt", "w", encoding="utf-8")

for tweet in tweetsfile.readlines():
	tweetsplit = tweet.split()
	if(tweetsplit[1][:3] != "RT"):
		noretweet.write(tweet)
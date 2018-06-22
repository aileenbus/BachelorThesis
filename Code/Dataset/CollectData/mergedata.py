tweetsfile1 = open("2016_mention.txt", "r", encoding="utf-8")
tweetsfile2 = open("2017_mention.txt", "r", encoding="utf-8")
tweetsfile3 = open("2018_mention.txt", "r", encoding="utf-8")
merged = open("mergedtweets.txt", "w", encoding="utf-8")

for tweet in tweetsfile1.readlines():
	merged.write(tweet)

for tweet in tweetsfile2.readlines():
	merged.write(tweet)

for tweet in tweetsfile3.readlines():
	merged.write(tweet)
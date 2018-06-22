from collections import defaultdict
import pickle

picklefile = open("dict.pickle", "rb")
countsfile = open("counts.txt", "w")
usersfile = open("userswithcutoff.txt", "w")


user_tweets = pickle.load(picklefile)

finaldict = {}

for key, value in user_tweets.items():
	if value <= 2000 and value >= 300:
		finaldict[key] = value

countslist = []
totalusers = 0
for key, value in finaldict.items():
	totalusers += 1
	countslist.append(value)
	userline = key + "\n"
	usersfile.write(userline)

countslist = sorted(countslist)

for item in countslist:
	itemstring = str(item) + "\n"
	countsfile.write(itemstring)


print("total users:", totalusers)




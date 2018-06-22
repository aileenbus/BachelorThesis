import pickle
from random import shuffle

picklefile = open("userlabels.pickle", "rb")
datafile = open("datawithcutoff.txt", "r", encoding="utf-8")

userlabels = pickle.load(picklefile)

tweetsperuser = {}

for line in datafile.readlines():
	splitline = line.split(",")
	userid = splitline[0]
	tweet = ",".join(splitline[1:])
	tweet = tweet.strip()

	if userid in tweetsperuser.keys():
		tweetsperuser[userid].append(tweet)
	else:
		tweetsperuser[userid] = [tweet]

print(len(tweetsperuser.keys()))

mergedtweetsperuser = {}

for key, value in tweetsperuser.items():
	merged = " TWEETDELIMITER ".join(value)
	merged = " TWEETDELIMITER " + merged + " TWEETDELIMITER "
	mergedtweetsperuser[key] = merged




devtraincutoff, devtestcutoff = 11795, 13269
devtrain, devtest, test = {}, {}, {}


shuffledkeys = list(mergedtweetsperuser.keys())
shuffle(shuffledkeys)

i = 0
for key in shuffledkeys:
	value = mergedtweetsperuser[key]
	i += 1
	if i < devtraincutoff: devtrain[key] = value
	elif i < devtestcutoff: devtest[key] = value
	else: test[key] = value

print("Dev train:", len(devtrain.keys()))
print("Dev test:", len(devtest.keys()))
print("Test:", len(test.keys()))

devtrainfile = open("devtrain.txt", "w", encoding="utf-8")
devtestfile = open("devtest.txt", "w", encoding="utf-8")
testfile = open("test.txt", "w", encoding="utf-8")

for key, value in devtrain.items():
	line = key + ", " + value + "\n"
	devtrainfile.write(line)

for key, value in devtest.items():
	line = key + ", " + value + "\n"
	devtestfile.write(line)

for key, value in test.items():
	line = key + ", " + value + "\n"
	testfile.write(line)








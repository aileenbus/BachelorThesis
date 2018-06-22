import re
import os
import json

def convert_bytes(num):
	"""
	this function will convert bytes to MB.... GB... etc
	"""
	for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
		if num < 1024.0:
			return "%3.1f %s" % (num, x)
		num /= 1024.0

users = open("merged.txt", "r")
out = open("output.txt", "w", encoding="utf-8")

userslist = []
tweetslist = []

year = input("Year: ")

for user in users.readlines():
	userslist.append(user[:-2])

userslist.sort()
userslist = set(userslist)

totalsize, progress, totalfound = 0, 0, 0

directory = os.fsencode(year)
for file in os.listdir(directory):
	filename = os.fsdecode(file)
	if filename.endswith(".out"):
		tweetsfilename = year + "/" + filename
		tweetslist = []
		tweetsfile = open(tweetsfilename, "r")

		statinfo = os.stat(tweetsfilename)
		filesize = statinfo.st_size
		totalsize += filesize

		for tweet in tweetsfile.readlines():
			tweetslist.append(tweet)

		found = 0
		for tweet in tweetslist:
			idstring = re.search('"user":{"id":[0-9]*,', tweet)
			idstring = idstring.group()[13:-1]
			if idstring in userslist:
				found += 1
				totalfound += 1
				parsed = json.loads(tweet)
				userid = parsed['user']['id_str']
				text = parsed['text']
				text = text.replace('\r\n', ' '); #replace all newline types
				text = text.replace('\n', ' ')
				text = text.replace('\r', ' ');
				text = text.replace('\n\r', ' ')
				newtweet = userid + ", " + text + "\n"

				out.write(newtweet)

		progress += 1
		print("Finished processing \"", filename, "\" | ", progress, " files processed totaling ", convert_bytes(totalsize), " | ", found, " tweets found in file | ", totalfound, " tweets found in total", sep="")
		continue
	else:
		continue
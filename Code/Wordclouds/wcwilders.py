from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

wilders = open("wilderstweets.txt").read()

stopwoorden = set(line.strip() for line in open('stopwoorden.txt'))

wilders.lower()
wordcloud_wilders = WordCloud(width=1600, height=800, background_color="white", max_words=2000, stopwords=stopwoorden)
wordcloud_wilders.generate(wilders)

wordcloud_wilders.to_file("wordcloudwilders.png")

plt.figure(figsize=(20,10), facecolor='k')
plt.axis("off")
plt.tight_layout(pad=0)
plt.imshow(wordcloud_wilders)
plt.show()
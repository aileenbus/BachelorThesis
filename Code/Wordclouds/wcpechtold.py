from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

pechtold = open("pechtoldtweets.txt").read()

stopwoorden = set(line.strip() for line in open('stopwoorden.txt'))

pechtold.lower()
wordcloud_pechtold = WordCloud(width=00, height=800, background_color="white", max_words=2000, stopwords=stopwoorden)
wordcloud_pechtold.generate(pechtold)

wordcloud_pechtold.to_file("wordcloudpechtold.png")

plt.figure(figsize=(20,10), facecolor='k')
plt.axis("off")
plt.tight_layout(pad=0)
plt.imshow(wordcloud_pechtold)
plt.show()
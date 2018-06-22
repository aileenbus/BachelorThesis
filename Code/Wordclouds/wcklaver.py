from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

klaver = open("klavertweets.txt").read()

stopwoorden = set(line.strip() for line in open('stopwoorden.txt'))

klaver.lower()
wordcloud_klaver = WordCloud(width=1600, height=800, background_color="white", max_words=2000, stopwords=stopwoorden)
wordcloud_klaver.generate(klaver)

wordcloud_klaver.to_file("wordcloudklaver.png")

plt.figure(figsize=(20,10), facecolor='k')
plt.axis("off")
plt.tight_layout(pad=0)
plt.imshow(wordcloud_klaver)
plt.show()
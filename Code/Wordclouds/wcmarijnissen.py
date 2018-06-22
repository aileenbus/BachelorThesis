from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

marijnissen = open("marijnissentweets.txt").read()

stopwoorden = set(line.strip() for line in open('stopwoorden.txt'))

marijnissen.lower()
wordcloud_marijnissen = WordCloud(width=1600, height=800, background_color="white", max_words=2000, stopwords=stopwoorden)
wordcloud_marijnissen.generate(marijnissen)

wordcloud_marijnissen.to_file("wordcloudmarijnissen.png")

plt.figure(figsize=(20,10), facecolor='k')
plt.axis("off")
plt.tight_layout(pad=0)
plt.imshow(wordcloud_marijnissen)
plt.show()
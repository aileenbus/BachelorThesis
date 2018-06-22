from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

buma = open("bumatweets.txt").read()

stopwoorden = set(line.strip() for line in open('stopwoorden.txt'))

buma.lower()
wordcloud_buma = WordCloud(width=1600, height=800, background_color="white", max_words=2000, stopwords=stopwoorden)
wordcloud_buma.generate(buma)

wordcloud_buma.to_file("wordcloudbuma.png")

plt.figure(figsize=(20,10), facecolor='k')
plt.axis("off")
plt.tight_layout(pad=0)
plt.imshow(wordcloud_buma)
plt.show()
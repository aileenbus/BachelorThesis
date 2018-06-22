from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

dijkhoff = open("dijkhofftweets.txt").read()

stopwoorden = set(line.strip() for line in open('stopwoorden.txt'))

dijkhoff.lower()
wordcloud_dijkhoff = WordCloud(width=1600, height=800, background_color="white", max_words=2000, stopwords=stopwoorden)
wordcloud_dijkhoff.generate(dijkhoff)

wordcloud_dijkhoff.to_file("wordclouddijkhoff.png")

plt.figure(figsize=(20,10), facecolor='k')
plt.axis("off")
plt.tight_layout(pad=0)
plt.imshow(wordcloud_dijkhoff)
plt.show()
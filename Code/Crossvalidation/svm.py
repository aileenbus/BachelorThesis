from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn import metrics
from sklearn.linear_model import SGDClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.dummy import DummyClassifier
from nltk.tokenize import TweetTokenizer
from nltk.stem.snowball import SnowballStemmer
from nltk.corpus import stopwords
import pickle

def compressData(datalist, length=0):
    if length == None:
        return datalist
    compressed = []
    count = 0
    for item in datalist:
        if count < length:
            compressed.append(item)
        count += 1
    return compressed

def tokenizer(x):
    tweettokenizer = TweetTokenizer()
    x = tweettokenizer.tokenize(x)
    return x

def main():
    devtraindatafile = open("devtraindata.pickle", "rb")
    devtrainlabelsfile = open("devtrainlabels.pickle", "rb")
    devtestdatafile = open("devtestdata.pickle", "rb")
    devtestlabelsfile = open("devtestlabels.pickle", "rb")

    devtraindata = pickle.load(devtraindatafile)
    devtrainlabels = pickle.load(devtrainlabelsfile)
    devtestdata = pickle.load(devtestdatafile)
    devtestlabels = pickle.load(devtestlabelsfile)

    traincutoff = None # none for entire dataset
    testcutoff = None
    devtraindata = compressData(devtraindata, traincutoff)
    devtrainlabels = compressData(devtrainlabels, traincutoff)
    devtestdata = compressData(devtestdata, testcutoff)
    devtestlabels = compressData(devtestlabels, testcutoff)

    vec = TfidfVectorizer(preprocessor=None, 
                          tokenizer=tokenizer,  
                          ngram_range=[1,3], 
                          analyzer='word', 
                          lowercase=True, 
                          strip_accents='unicode')

    sgd = SGDClassifier(n_jobs=-1, loss='hinge', class_weight='balanced')


    classifier = Pipeline( [('vec', vec), ('cls',  sgd)] )

    classifier.fit(devtraindata, devtrainlabels)
    predicted = classifier.predict(devtestdata)

    print(metrics.classification_report(devtestlabels, predicted))


if __name__ == '__main__':
    main()
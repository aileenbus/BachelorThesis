from sklearn.model_selection import KFold, StratifiedKFold
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn import metrics
from sklearn.linear_model import SGDClassifier, LogisticRegression
from sklearn.dummy import DummyClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.svm import LinearSVC
from nltk.tokenize import TweetTokenizer
from nltk.stem.snowball import SnowballStemmer
from nltk.corpus import stopwords
import numpy as np
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

def cf_matrix(Ytest, Yguess, encoder, export=False):
    """
    Prints the scikit confusion matrix and adds the labels the the matrix to make it more readable
    :param Ytest: Testing data labels
    :param Yguess: Predicted labels of testing data
    :param encoder: Encoder for labels
    :param export: Toggle for export using \t
    :return:
    """
    labels = encoder.classes_

    cf = confusion_matrix(Ytest, Yguess, labels=labels)
    cf_new = cf.tolist()
    print("")

    max_label = max(labels, key=len)
    max_chars = str(len(max_label) + 1)
    if not export:
        format_header = "{:>"+max_chars+"}"
        format_str = "{:"+max_chars+"}"
        for i in range(len(labels)):
            format_header += "{:>"+max_chars+"}"
            format_str += "{:"+max_chars+"}"

    elif export:
        format_header = "{}\t"
        format_str = "{}\t"
        for i in range(len(labels)):
            format_header += "{}\t"
            format_str += "{}\t"

    for i in range(len(cf_new)):
        cf_new[i].insert(0, labels[i])
    print(format_header.format("", *labels))
    for row in cf_new:
        print(format_str.format(*row))
    print("")


def crossval(model, X, Y, le, cv=10):
    """
    Do Crossval ML
    :param model: sklearn model
    :param X:
    :param Y:
    :param le: Label Encoder
    :param cv: Number of folds
    :return:
    """
    print("> Starting {} fold Cross-Validation".format(cv))
    X = np.array(X)
    Y = np.array(Y)
    kf = StratifiedKFold(n_splits=cv)
    classification_reports = []
    gold = []
    predict = []
    count = 1
    for train_index, test_index in kf.split(X, Y):
        print("\r> Training and predicting fold {} out of {}".format(count, cv), end='')
        # Set X_train, X_test, Y_train and Y_test
        Xtrain, Xtest = X[train_index], X[test_index]
        Ytrain, Ytest = Y[train_index], Y[test_index]

        # Train the model
        model.fit(Xtrain, Ytrain)

        # Predict Xtest
        Ypred = model.predict(Xtest)

        # Evaluation
        classification_reports.append(classification_report(Ytest, Ypred, le.classes_))
        gold += list(Ytest)
        predict += list(Ypred)

        count +=1
    print('\n', end='')
    # Final Evaluation
    # getAvgClassificationReport(classification_reports)
    print(classification_report(gold, predict, labels=le.classes_))
    cf_matrix(gold, predict, le)

    return model


def main():
    devtraindatafile = open("cvdevtraindata.pickle", "rb")
    devtrainlabelsfile = open("cvdevtrainlabels.pickle", "rb")
    testdatafile = open("cvtestdata.pickle", "rb")
    testlabelsfile = open("cvtestlabels.pickle", "rb")

    devtraindata = pickle.load(devtraindatafile) # 90% of the data
    devtrainlabels = pickle.load(devtrainlabelsfile)
    testdata = pickle.load(testdatafile)  # 10% of the data
    testlabels = pickle.load(testlabelsfile)

    traincutoff = 2000 # none for entire dataset
    #testcutoff = None
    
    X = compressData(devtraindata, traincutoff)
    y = compressData(devtrainlabels, traincutoff)

    # Encode Labels
    le = LabelEncoder()
    le.fit(y)
    
    #testdata = compressData(testdata, testcutoff)
    #testlabels = compressData(testlabels, testcutoff)

    vec = TfidfVectorizer(preprocessor=None, 
                          tokenizer=tokenizer,  
                          ngram_range=[1,1], 
                          analyzer='word', 
                          lowercase=True, 
                          strip_accents='unicode')

    sgd = SGDClassifier(n_jobs=-1, loss='hinge', class_weight='balanced', random_state=50)
    linearsvc = LinearSVC(class_weight='balanced')
    bas = DummyClassifier(strategy='stratified', random_state=48)

    classifier = Pipeline( [('vec', vec), ('cls',  sgd)] )

    # cross validation
    crossval(classifier, X, y, le, cv=10)


if __name__ == '__main__':
    main()
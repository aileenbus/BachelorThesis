# # Bachelor scriptie

In het kader van de afstudeeropdracht in de Bachelor Informatiekunde van
Rijksuniversiteit Groningen is deze scriptie geschreven.

In deze scriptie wordt onderzocht of er te voorspellen valt of een gebruiker op
Twitter een bepaalde politieke leider volgt. In de programmeertaal Python met de
Scikit-Learn module wordt door middel van 10-fold cross validatie en n-grammen
gekeken naar de f1-score van zes groepen van in totaal 14.742 unieke volgers van
zes verschillende politici.
Uit dit onderzoek komt naar voren dat met een baseline van 26% en een hoogste
score van 56% met het LinearSVC algoritme en 49% met het SGD-Classifier algoritme,
men met deze dataset niet kan voorspellen middels tweets of een gebruiker
op Twitter een bepaalde politieke leider volgt. De groepen met meer volgers scoren
veel hoger dan politici met minder volgers. Daarnaast scoren specifiekere groepen
volgers ook veel hoger dan algemenere groepen volgers.
Een volgend onderzoek zou deze score kunnen verbeteren door een betere balans
aan te brengen in de dataset, specifieker te selecteren op volgers (profielinformatie)
of door betere preprocessing tools te gebruiken.

## Uitleg

Om de code te kunnen gebruiken is de Twitterdata nodig die verzameld is voor de scriptie.
Helaas zijn deze bestanden te groot voor Github.

### Prerequisites

Python 3


## Built With

* [Scikit-Learn](http://scikit-learn.org/) - Module voor machine learning in Python
* [Nederlands Twitter Corpus](http://www.let.rug.nl/gosse/Ngrams/) - Rijksuniversiteit Groningen
* [NLTK](http://www.nltk.org/api/nltk.tokenize.html) - Tokenize package


## Authors

Aileen Bus
a.bus.1@student.rug.nl

## Acknowledgments

* Joël Coster
* Reinard van Dalen
* Stijn Eikelboom

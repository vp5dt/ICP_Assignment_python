# Importing Required Libraries
import urllib.request
from bs4 import BeautifulSoup
from nltk.corpus import wordnet as wordnet
from nltk.tokenize import word_tokenize, sent_tokenize, wordpunct_tokenize
from nltk.stem import LancasterStemmer, SnowballStemmer, WordNetLemmatizer
from nltk import pos_tag, ne_chunk, ngrams
import numpy
from bs4 import BeautifulSoup
from bs4.element import Comment



def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True


def text_from_html(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)
    return u" ".join(t.strip() for t in visible_texts)

html = urllib.request.urlopen('https://en.wikipedia.org/wiki/Python_(programming_language)').read()

html=text_from_html(html)

# Saving to a Text File
with open('Output.txt', 'w') as text_file:
    text_file.write(str(html.encode("utf-8")))

# Reading from a Text File
with open('Output.txt', 'r') as text_file:
    read_data = text_file.read()

# Tokenization
"""Sentence Tokenization"""
sentTok = sent_tokenize(html)
print("Sentence Tokenization : \n", sentTok)

"""Word Tokenization"""
tokens = word_tokenize(html)
print ("Word Tokenization : \n", tokens)

# Stemming
# 1 -> LancasterStemmer
tokStem = LancasterStemmer()
print("Lancaster Stemming : \n")
for tok in tokens:
    print(tokStem.stem(str(tok)))

# 2 -> SnowBallStemmer
snowStem = SnowballStemmer('english')
print("SnowBall Stemming : \n")
for tok in tokens:
    print(snowStem.stem(str(tok)))


# POS
print("Part of Speech Tagging :\n", pos_tag(tokens))

# Lemmatization
lemmatizer = WordNetLemmatizer()
print("Lemmatization :\n")
for tok in tokens:
    print(lemmatizer.lemmatize(str(tok)))

# Trigram
print("TRIGRAMS")
new_trigrams = []
c = 2
while c < len(tokens) - 2:
  new_trigrams.append((tokens[c], tokens[c+1], tokens[c+2]))
  c += 1
print(new_trigrams)




# Named Entity Recognition
print("Named Entity Recognition : \n", ne_chunk(pos_tag(wordpunct_tokenize(str(tokens)))))
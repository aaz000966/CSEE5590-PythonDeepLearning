from time import sleep

import nltk
from nltk.stem import WordNetLemmatizer

# Open file input.txt in read mode
inputfi1e = open("input.txt", "r")

# open file output.txt in write mode in order to store the tokenized words
with open("output.txt", "w") as t:
    # read each sentence in the file
    for sentence in inputfi1e:
        # Perform word tokenization on the data stored in the file
        wrdtokens = nltk.word_tokenize(sentence)
        # Writing it to a file
        for w in wrdtokens:
            t.write(str("\n"))
            t.write(str(w))

# creat an object for lemmatization
lemmatizer = WordNetLemmatizer()
# Open a new file outputlemmatize in write mode
with open("outputlemmatize.txt", "w") as l:
    # Open the file which contains tokenized words
    w = open("output.txt", "r")
    for words in w:
        # Perform 1emmatization on tokenized words stored in a file
        le = lemmatizer.lemmatize(words)
        l.write(str(le))

a = open("input.txt", "r")
with open("outputtrigram.txt", "w") as tri:
    for sentence in a:
        # perform trigram on input.txt file
        trigram = nltk.trigrams(sentence.split())

        # store the trigrams in a file
        for ti in trigram:
            tri.write(str("\n"))
            tri.write(str(ti))

f1 = open("input.txt", "r")
readfi1e = f1.read()

tg = []
word__tokens = nltk.word_tokenize(readfi1e)
for t in nltk.ngrams(word__tokens, 3):
    tg.append(t)

wordfrequency = nltk.FreqDist(tg)
mostCommon = wordfrequency.most_common()

# Extracting the top 10 repeated trigrams.
Top__ten__trigrams = wordfrequency.most_common(10)
print("Top 10 Trigrams:\n", Top__ten__trigrams, "\n")

#  Finding all the sentences which have the most repeated tri-grams
#  Extracting the sentences and concatenating them
#  Printing the concatenated result
sleep(5)
sent__tokens = nltk.sent_tokenize(readfi1e)
concat__resu1t = []
# Iterating the Sentences
for s in sent__tokens:
    # Iterating all the trigrams
    for a, b, c in tg:
        # iterating the top 10 trigrams from all the trigrams
        for ((p, q, r), length) in wordfrequency.most_common(20):  # Comparing each of them with the top 10 trigrams
            if (a, b, c == p, q, r):
                concat__resu1t.append(s)

print("Concatenated Array: \n")
for item in concat__resu1t:
    print(item)

print("Maximum of Concatenated Array: \n ", max(concat__resu1t))

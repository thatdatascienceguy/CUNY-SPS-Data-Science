# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 23:01:10 2018

@author: jonboy1987
"""
import pandas as pd
import nltk
import re
import enchant
import matplotlib.pyplot as plt

""" 1. Corpus of interest
json jeopardy data which contains information on over 200k+ jeopardy questions
Data: https://www.reddit.com/r/datasets/comments/1uyd0t/200000_jeopardy_questions_in_a_json_file/
Download: https://drive.google.com/file/d/0BwT5wj_P7BKXb2hfM3d2RHU1ckE/view
"""

# read the json data
jeopardy = pd.read_json("JEOPARDY_QUESTIONS1.json")
# Extract only the questions that were asked
questions = jeopardy.question

# preview questions:
print "Example Questions:"
for i in range(10):
    print questions[i]

print
""" 2. How many unique words are in the dataset?"""

d = enchant.Dict("en_US")
# join the list of strings into one
corpus = " ".join(questions)
tokens = nltk.word_tokenize(corpus) # tokenize the string

# normalize the words and sort them
words = [w.lower() for w in tokens]
n_words = len(words) # total number of words
print "Number of words in corpus: ", n_words

# doing a preview of words shows that there are some entries not even words but
# numbers or just special characters.
# let's simply keep just words no numbers, no special characters

words_only = [w for w in words if re.search(r"^[a-z]{1,}[^\W|\d]+$",w)]
# filter out even more for words not in the english dictionary using d.check()
# running d.check() first will consider words like '5' or '.' 
words_only = [w for w in words_only if d.check(w)]
n_unique_words = len(set(words_only))
print "Number of unique words: ", n_unique_words

""" 3. Using the most common words, how many unique represent half of the total words
in the corpus? """

fdist = nltk.FreqDist(words_only) # frequency distribution
large_freq = 0
for freq in fdist:
    if fdist[freq] > (n_words / 2): # if greater than half the total words
        large_freq = large_freq + 1
print "Number of unique words that occur more than half of the total words in corpus: ", large_freq

""" 4. Identify the 200 highest frequency words in this corpus """
most_freq_200 = fdist.most_common(200) # 200 most frequent words sorted by count
for word, frequency in most_freq_200: # iterate and print
    print word, frequency


""" 5. Create a graph that shows the relative frequency of these 200 words. """

# compute the relative frequency and round it to 4 decimal places
frequency = [x[1] for x in most_freq_200] # frequencies of words
rel_frequency = [round(float(x)/n_words, 4) for x in frequency]
plt.loglog(rel_frequency, frequency)
plt.xlabel("Frequency of Words in Jeopardy Questions")
plt.ylabel("Relative Frequency of Words")
plt.title("Zipf Plot For 200 Most Common Words")
plt.show()

""" 6. Does the observed relative frequency of these words follow Zipf’s law? Explain.

The relative frequency does follow Zip'f law somewhat in that the 2nd best word about 
70% more than the first, the third one occurs about 66% than the first. The least words
mostly remain constant. """

""" 7. In what ways do you think the frequency of the words in this corpus differ from “all words in all corpora.”

The frequency of words in this corpus does slighly differ in all words in all corpora.
other corpora depending on context and setting may differ and have a different frequency distribution and may have
not for example 'the' as the most common word.
"""

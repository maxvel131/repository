#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      legolas
#
# Created:     03.04.2015
# Copyright:   (c) legolas 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import random
from urllib import urlopen
import sys

WORD_URL = "http://learncodetheheardway.org/words.txt"
WORDS = []

PHRASES = {
    "class Salmon(Fish):":
        "Make a class named Salmon that is-a Fish.",
    "class Salmon(object):\n\tdef __init__(self, Mary)":
        "class Salmon has-a __init__ that takes self and Mary parameters.",
    "class Salmon(object):\n\tdef Mary(self, Joe)":
        "class Salmon has-a function named Mary that takes self and Joe parameters.",
    "foo = Salmon()":
        "Set foo to an instance of class Salmon.",
    "foo.Mary(Joe)":
        "From Mary get the Joe function, and call it with parameters self, Joe.",
    "foo.Joe = 'Joe2'":
        "From Joe get the Mary attribute and set it to 'Joe2'."
}

# do they want to drill phrases first
PHRASE_FIRST = False
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True

# load up the words from the website

for word in urlopen(WORD_URL).readlines():
    WORDS.append(word.strip())

def convert(snippet, phrase):
    class_names = [w.capitalize() for w in
                   random.sample(WORDS, snippet.count("Salmon"))]
    other_names = random.sample(WORDS, snippet.count("Mary"))
    results = []
    param_names = []

    for i in range(0, snippet.count("Mary")):
        param_count = random.randint(1,3)
        param_names.append(', '.join(random.sample(WORDS, param_count)))

    for sentence in snippet, phrase:
        result = sentence[:]

        # fake class names

        for word in class_names:
            result = result.replace("Salmon", word, 1)

    # fake other names
        for word in other_names:
            result = result.replace("Mary", word, 1)

    # fake parameter list
        for word in param_names:
            result = result.replace("Joe", word, 1)

        results.append(result)

    return results

# keep going until they hit CTRL-D

try:
    while True:
        snippets = PHRASES.keys()
        random.shuffle(snippets)

        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                question, answer = answer, question

            print question

            raw_input('> ')
            print "ANSWER:  %s\n\n" % answer

except EOFError:
    print "\nBye"












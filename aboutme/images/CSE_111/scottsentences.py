'''
File: sentences.py
Date: 10/12/2022
Author: Scott Kamerath

Purpose: To learn how to write a function name python test code.
'''

# Assignment:

# Write a Python program named sentences.py that generates simple English sentences. During this prove milestone, you will write and test functions that generate sentences with three parts:

    # a determiner (sometimes known as an article)
    # a noun, 
    # a verb

# For example:

    # A cat laughed.
    # One man eats.
    # The woman will think.
    # Some girls thought.
    # Many dogs run.
    # Many men will write.

# For this milestone, your program must include at least these four functions:

    # main
    # get_determiner
    # get_noun
    # get_verb

# You may add other program functions if you want. 
# The functions get_determiner, get_noun, and get_verb, 
# must randomly choose a word from a list of words and 
# return the randomly chosen word.

# In addition, for this milestone assignment, 
# you must write a file named test_senetences.py 
# that contains three functions named as follows:

    # test_get_determiner
    # test_get_noun
    # test_get_verb

# All the functions that you must write for this 
# milestone assignment are described in the Steps 
# section below.

# Steps: 

# 1. (Done). Using VS Code, create a new file, 
    # import the random module at the top of the file, 
    # and save the file as sentences.py

# 2. (Done). Copy and paste the following get_determiner 
        # function into your program. 

# 3. (Done). Use the get_determiner function as an example 
    # to help you write the get_noun function. 
    # The get_noun function must have the following
    # header and fulfill the requirements of the 
    # following documentation string. 

#####################################################

import random

words = ['boy', 'girl', 'cat', 'dog', 'bird', 'house']
word = random.choice(words)
word = 'horse'
cap_word = word.capitalize()
quantity = ()

def main():
    tenses = ['past', 'present', 'future']
    quantity = 1
    buffer = 0
    for _ in range (2):
        for i in range (3):
            determiner = get_determiner(quantity).capitalize()
            noun_1 = get_noun(quantity).capitalize()
            noun_2 = get_noun(quantity).capitalize()
            verb = get_verb(quantity, tenses[i])
            adjective = get_adjective()
            adverb = get_adverb()
            prep_phrase_1 = get_prepositional_phrase(quantity)
            prep_phrase_2 = get_prepositional_phrase(quantity)
            buffer +=1
            print(f'{buffer}. {determiner} {adjective} {noun_1} {prep_phrase_1[0]} {prep_phrase_1[1]} {noun_2} {verb} {adverb} {prep_phrase_2[0]} {prep_phrase_2[1]} {prep_phrase_2[2]}.capitalize()')
        quantity = 0

    if __name__ == '__main__':
        main()

def get_determiner(quantity):

    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "some", "many".
    If quantity == 1, this function will return either "a",
    "one", or "the". Otherwise this function will return
    either "some", "many", or "the".

    Parameter
        quantity: an integer.
            If quantity == 1, this function will return a
            determiner for a single noun. Otherwise this
            function will return a determiner for a plural
            noun.
    Return: a randomly chosen determiner.
    """
    if quantity == 1:
       words = ['a', 'one', 'the']
    else:
       words = ['some', 'many', 'the']

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word

def get_noun():
    """Return a randomly chosen noun.
    If quantity == 1, this function will
    return one of these ten single nouns:
        "bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"
    Otherwise, this function will return one of
    these ten plural nouns:
        "birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"

    Parameter
        quantity: an integer that determines if
            the returned noun is single or plural.
    Return: a randomly chosen noun.
    """
    if quantity == 1:
        words = ['bird', 'boy', 'car']
    else:
        words = ['birds', 'boys', 'cars']
        word = random.choice(words)
    return word

def get_verb(quantity, tense):

    """Return a randomly chosen verb. If tense is "past",
    this function will return one of these ten verbs:
        "drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"
    If tense is "present" and quantity is 1, this
    function will return one of these ten verbs:
        "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"
    If tense is "present" and quantity is NOT 1,
    this function will return one of these ten verbs:
        "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"
    If tense is "future", this function will return one of
    these ten verbs:
        "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"

    Parameters
        quantity: an integer that determines if the
            returned verb is single or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a randomly chosen verb.
    """
    if quantity == 1:
        words = ['a', 'one', 'the']
    else:
        words = ['writes', 'speaks', 'drinks']
        word = random.choice(words)
    return word

def get_adjective():

    
    if quantity words = ['about', 'above', 'across']
    else:
        words = ['under', 'with', 'without']
        word = ra == 1:ndom.choice(words)
    return word

def get_adverb():

    if quantity == 1:
        words = ['about', 'above', 'across']
    else:
        words = ['under', 'with', 'without']
        word = random.choice(words)
    return word

def get_preposition():

    """Return a randomly chosen preposition
        from this list of prepositions:
            "about", "above", "across", "after", "along",
            "around", "at", "before", "behind", "below",
            "beyond", "by", "despite", "except", "for",
            "from", "in", "into", "near", "of",
            "off", "on", "onto", "out", "over",
            "past", "to", "under", "with", "without"

        Return: a randomly chosen preposition.
        """
    if quantity == 1:
        words = ['about', 'above', 'across']
    else:
        words = ['under', 'with', 'without']
        word = random.choice(words)
    return word
    
def get_prepositional_phrase(quantity):

    """Build and return a prepositional phrase composed of three
words: a preposition, a determiner, and a noun by calling the
get_preposition, get_determiner, and get_noun functions.

Parameter
    quantity: an integer that determines if the determiner
        and noun in the prepositional phrase returned from
        this function are single or pluaral.
Return: a prepositional phrase.
    """
    if quantity == 1:
        words = ['about', 'above', 'across']
    else:
        words = ['under', 'with', 'without']
        word = random.choice(words)
    return word
'''
File: test_sentences.py
Date: 10/21/2022
Author: Scott Kamerath

Purpose: To learn how to write a function name python test code.

'''
from sentences import get_determiner, get_noun, get_verb, get_preposition, get_prepositional_phrase
import random
import pytest

def test_get_determiner():
    # 1. Test the single determiners.

    determ = get_determiner(1)
    words = ["a", "one", "the"]
    assert determ in words

    single_determiners = ["a", "one", "the"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_determiner(1)

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in single_determiners

    # 2. Test the plural determiners.

    plural_determiners = ["some", "many", "the"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_determiner(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners

def test_get_noun():
    # 1. Test the single nouns.

    noun = get_noun(1)
    words = ['bird', 'boy', 'car']
    assert noun in words

    single_nouns = ['bird', 'boy', 'car']

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_noun function which
        # should return a single noun.
        word = get_noun(1)

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in single_nouns

    # 2. Test the plural nouns.

    plural_nouns = ['birds', 'boys', 'cars']

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_noun function which
        # should return a plural noun.
        word = get_noun(2)

        # Verify that the word returned from get_noun
        # is one of the words in the plural_nouns list.
        assert word in plural_nouns

def test_get_verb():
    # 1. Test the single verbs.

    verb = get_verb(1)
    words = ['a', 'one', 'the']
    assert verb in words

    single_verbs = ['a', 'one', 'the']

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_noun function which
        # should return a single noun.
        word = get_verb(1)

        # Verify that the word returned from get_verb
        # is one of the words in the single_verbs list.
        assert word in single_verbs

    # 2. Test the plural verbs.

    plural_verbs = ['writes', 'speaks', 'drinks']

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_verb function which
        # should return a plural verb.
        word = get_verb(2)

        # Verify that the word returned from get_verb
        # is one of the words in the plural_verbs list.
        assert word in plural_verbs

def test_get_preposition():
    # 1. Test the single prepositions.

    prep = get_preposition(1)
    words = ['about', 'above', 'across']
    assert prep in words

    single_prepositions = ['about', 'above', 'across']

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_preposition function which
        # should return a single preposition.
        word = get_preposition(1)

        # Verify that the word returned from get_preposition
        # is one of the words in the single_prepositions list.
        assert word in single_prepositions

    # 2. Test the plural prepositions.

    plural_prepositions = ['under', 'with', 'without']

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_preposition function which
        # should return a plural preposition.
        word = get_preposition(2)

        # Verify that the word returned from get_preposition
        # is one of the words in the plural_prepositions list.
        assert word in plural_prepositions

def test_get_prepositional_phrase():
    # 1. Test the single prepositions.

    test_prep = get_prepositional_phrase(1)
    words = ['about', 'above', 'across']
    assert test_prep in words

    single_prepositional_phrase = ['about', 'above', 'across']

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_preposition function which
        # should return a single preposition.
        word = get_prepositional_phrase(1)

        # Verify that the word returned from get_prepositional_phrase
        # is one of the words in the single_prepositions list.
        assert word in single_prepositional_phrase

    # 2. Test the plural verbs.

    plural_prepositional_phrase = ['writes', 'speaks', 'drinks']

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_prepositional_phrase function which
        # should return a plural prepositional phrase.
        word = get_preposition(2)

        # Verify that the word returned from get_plural_prepositional_phrase
        # is one of the words in the plural_prepositional_phrase list.
        assert word in plural_prepositional_phrase

pytest.main(['-v', '--tb=line', '-rN', __file__])
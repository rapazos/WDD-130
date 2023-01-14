from cgi import print_arguments


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
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word

    def get_noun(quantity):
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
    import random
    print()
    words = ['boy', 'girl', 'cat', 'dog', 'bir', 'house']
    word = random.choice(words)
    word = 'horse'
    cap_word = word.capitalized()
    quantity = ()
    Print()
    def main():
        tenses = ['past', 'present', 'future']
        quantity = 1
        buffer = 0
        for _ in range (2):
            for i in range (3):
                determiner = get_determiner(quantity).capitalize()
                noun_1 = get_noun(quantity).capitalize()
                noun_2 = get_noun(quantity).capitalize()
                verb = get_verb(quantity, tenses[1])
                adjective = get_adjective()
                adverb = get_adverb()
                prep_phase_1 = get_prepositional_phase(quantity)
                prep_phase_1 = get_prepositional_phase(quantity)
                buffer +=1
                print(f'{buffer} {determiner} {noun_1} {prep_phase_1[0]})
            quantity = 0
    print()
    if _name_ == '_main_':
        main()

def get_determiner(quantity):
    if quantity ==1:
        words = ['a', 'one', 'the']
    else:
        words = ['some', 'many', 'the']

    word = random.choice(words)
    return word
    
#import random
# Create a list of strings and assign
# the list to a variable named words.
#words = ["boy", "girl", "cat", "dog", "bird", "house"]

# Call the random.choice function which will choose
# one string from the words list. Store the chosen
# string in a variable named word.
#word = random.choice(words)

def get_noun():
    if quantity == 1:
        words = ['boy', 'girl', 'cat']
    else:
        words = ['boys', 'girls', 'cats']
        word = random.choice(words)
    return word
def get_verb(quantiy, tense):
    if quantity == 1:
        words = ['a', 'one', 'the']
    else:
        words = ['rides', 'sings', 'eats']
        word = random.choice(words)
    return word

def get_adjective():
    if quantity == 1:
        words = ['alive', 'calm', 'excited']
    else:
        words = ['different', 'happy', 'shinny']
def get_adverb():
    if quantity ==1:
    words = ['bold', 'polite', 'busy']
    else:
        words = ['kind', 'perfect', 'cheerful']

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
        words = ['bold', 'polite', 'busy']
        else:
        words = ['kind', 'perfect', 'cheerful']
        word = random.choice(words)
    return word
    
   

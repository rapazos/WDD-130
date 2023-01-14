from random import uniform, choice

def main():
    
    numbers = [16.2, 75.1, 52.3]
    print("")
    print(numbers)

    append_random_numbers(numbers)
    print("")
    print(numbers)

    append_random_numbers(numbers, 7)
    print("")
    print(numbers)

    words = ["encouraging", "pumped", "sneaky", "point", "tedious", "whirl", "spot", "cup", "mint", "tacit", "abundant", "work"]
    print("")
    print(words)

    append_random_words(words)
    print("")
    print(words)

    append_random_words(words, 3)
    print("")
    print(words)
    print("")


def append_random_numbers(numbers_list:list, quantity:int = 1):
    
    for _ in range(quantity):
        random_number = round(uniform(1,100),1)
        numbers_list.append(random_number)

def append_random_words(words_list:list, quantity:int = 1):

    for _ in range(quantity):
        list_of_words = ["pour", "yoke", "partner", "quack", "truculent", "bolt", "receptive", "silly", "appear", "broken", "prefer", "shave"]
        random_word = choice(list_of_words)
        words_list.append(random_word)


if __name__ == "__main__":
    main()
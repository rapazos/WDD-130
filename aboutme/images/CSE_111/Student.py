import csv

def read_dict(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
# The column headings and indexes.
I_NUMBER_INDEX = 0
NAME_INDEX = 1
# Read the contents of a CSV file named students.csv
# into a dictionary named students_dict. Use the I-Number
# as the key in the dictionary.
students_dict = read_dict("students.csv", I_NUMBER_INDEX)

# Get an I-Number from the user.
inumber = input("Please enter an I-Number (xx-xxx-xxxx): ")

# The I-Numbers are stored in the CSV file as digits only (without
# any dashes), so we remove all dashes from the user's input.
inumber = inumber.replace("-", "")

# Determine if the user input is formatted correctly.
if not inumber.isdigit():
        print("Invalid character in I-Number")
else:
    if len(inumber) < 9:
        print("Invalid I-Number: too few digits")
    elif len(inumber) > 9:
        print("Invalid I-Number: too many digits")
    else:
        # The user input is a valid I-Number. Find
        # the I-Number in the list of I-Numbers.
        if inumber not in students_dict:
            print("No such student")
        else:
            # Retrieve the student name that corresponds
            # to the I-Number that the user entered.
            value = students_dict[inumber]
            name = value[NAME_INDEX]

            # Print the student name.
            print(name)
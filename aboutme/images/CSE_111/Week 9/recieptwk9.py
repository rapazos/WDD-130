"""In receipt.py, write a function named read_dictionary that will open a CSV file for reading and use a csv.reader to read each row and populate
 a compound dictionary with the contents of the products.csv file. The read_dictionary function must have this header and documentation string:"""

main
read_dictionary
#
import csv

def main ():
    # Index of the product number column in the products.csv.
    PRODUCT_INDEX = 2

    # Read the contents of products.csv and the request.csv                     # CONTINUE ON 34.55 IN VIDE0
    # into compound dictionary called grocery_dict
    grocery_dict = read_dict("products.csv", PRODUCT_INDEX = 2 )

    print(grocery_dict)

def read_dictionary(filename, key_column_index):
    
    """
    Read the contents of a CSV file into a compound
    dictionary then return to the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """


    """
    Open the request.csv file in VS Code and examine it. Notice that each row contains only two values, a product number and a quantity. 
    Notice also that product number D083 appears twice in the file. It appears twice because the customer who created the order in the 
    request.csv file added four yogurts to his order and then later added three more yogurts to his order. Because product numbers may 
    appear multiple times in the request.csv file, your program must not read the contents of request.csv into a dictionary.
"""

"""
In your receipt.py program, write another function named main that does the following:
Calls the read_dictionary function and stores the compound dictionary in a variable named products_dict.
Prints the products_dict.
Opens the request.csv file for reading.
Skips the first line of the request.csv file because the first line contains column headings.
Uses a loop that reads and processes each row from the request.csv file. Within the body of the loop, your program must do the following for each row:
Use the requested product number to find the corresponding item in the products_dict.
Print the product name, requested quantity, and product price.
"""

"""
At the bottom of your receipt.py file, add a call to the main function. Be certain to protect the call to main with an if statement
as taught in the prepare content for lesson 5.
"""
# create empty dict to store data from csv file
dictionary = {}


# Open the CSV file for reading and store a reference
# to the opened file in a variable named csv_file.
with open(filename, "rt") as csv_file:

# Use the csv module to create a reader object
# that will read from the opened CSV file.
reader = csv.reader(csv_file)

# The first row of the CSV file contains column
# headings and not data, so this statement skips
# the first row of the CSV file.
next(reader)

# Read the rows in the CSV file one row at a time.
# The reader object returns each row as a list.
for row_list in reader:

# If the current row is not blank, add the
# data from the current to the dictionary.
if len(row_list) != 0:

# From the current row, retrieve the data
# from the column that contains the key.
key = row_list[key_column_index]

# Store the data from the current
# row into the dictionary.
dictionary[key] = row_list

# Return the dictionary.
return dictionary


# Call main to start this program.
if __name__ == "__main__":
    main()

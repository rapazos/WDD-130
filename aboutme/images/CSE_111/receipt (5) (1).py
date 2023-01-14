import csv
# Import the datetime class from the datetime
# module so that it can be used in this program.
from datetime import datetime

def main():
    # Index of the product number column
    # in the products.csv file.
    KEY_INDEX = 0
    print('Save Mart')
    print('')

    # Read the contents of the products.csv into a
    # compound dictionary named products_dict. Use
    # the product numbers as the keys in the dictionary.
    try:

        products_dict = read_dict("products.csv", KEY_INDEX)

    
    except FileNotFoundError as not_found_err:
        print(not_found_err)
        print('Please choose a different file.')

    except PermissionError as perm_err:
        print(perm_err)
        print('You don\'t have permission to access that file.')  

    # Open a file named request.csv and store a reference
    # to the opened file in a variable named request_file.
    try: 
        with open("request.csv", "rt") as request_file:

            # Use the csv module to create a reader
            # object that will read from the opened file.
            reader = csv.reader(request_file)

            # The first row of the CSV file contains column
            # headings and not data about a order requests,
            # so this statement skips the first row of the
            # CSV file.
            next(reader)

            items = 0
            sub = 0
            QTY_INDEX = 1
            NAME_INDEX = 1
            PRICE_INDEX = 2

            # Read each row in the CSV file one at a time.
            # The reader object returns each row as a list.
            for row_list in reader:

                # For the current row, retrieve the
                # values in columns 0, and 1
                Key = row_list[KEY_INDEX]
                Qty = row_list[QTY_INDEX]
                # Find the key in the dictionary and
                # retrieve the corresponding value, which is a list.
                value = products_dict[Key]

                # Retrieve the products name and
                # price from the list.
                name = value[NAME_INDEX]
                price = value[PRICE_INDEX]

                # Print the product order infomation.
                print(f"{name}: {Qty} @ {price}")
                items += int(Qty)
                sub += (float(price) * float(Qty))
        print('')
        print(f'Number of Items: {items}')
        print(f'Subtotal: {str(round(sub,2))}')
        tax = .06
        saleTax = sub * tax
        print(f'Sales Tax: {str(round(saleTax,2))}')
        total = sub + saleTax
        print(f'Total: {str(round(total,2))}')
        print('')
        print('Thank you for shopping at Save Mart!')

        # Call the now() method to get the current
        # date and time as a datetime object from
        # the computer's operating system.
        current_date_and_time = datetime.now()

        print(f"{current_date_and_time:%a %b %d %H:%M:%S %Y}")
    
    except FileNotFoundError as not_found_err:
        print(not_found_err)
        print('Please choose a different file.')

    except KeyError as key_err:
        print(type(key_err).__name__, key_err)
        print('Key is wrong.')


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
    # Create an empty dictionary that will
    # store the data from the CSV file.
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

# If this file is executed like this:
# > python program.py
# then call the main function. However, if this file is simply
# imported (e.g. into a test file), then skip the call to main.
if __name__ == "__main__":
    main()
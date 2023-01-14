'''
File: Contact_book_functions.py
12/10/22
Author: Rachel Pazos
Purpose: To make a contack book to store names, addresses, and phone numbers
'''





# Contact/Address book or list to store Names, Addresses, and phone numbers
# This file will import info from file contact_book_functions.py


import contact_book_functions
import sys
def main():
    contact_list = []
    choice = int(input("What would you like to do? \n"
                        "(1)Add a contact\n"
                        "(2)View contacts\n"
                        "(-1)Exit"))
    if choice == -1:
        sys.exit(0)
    if choice -- 1:
        contact_book_functions.new_contact(contact_list)
    if choice == 2:
        contact_book_functions.view_contacts(contact_list)
    

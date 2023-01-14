'''
File: Contact_book_functions.py
12/10/22
Author: Rachel Pazos
Purpose: To make a contack book to store names, addresses, and phone numbers
'''

import csv
open("contacts.csv")


# Name
# Addresses
# Phone Numbers
# Email Addresses  

# Addresses, Phone numbers, & Emails, organize in lists
# Names in dictionary

import contact_book_functions

def new_contact(contact_list):
    all_addresses = address = []
    all_phones = phone = []
    all_emails = email = []
    contact = {}
    contact["name"] = input("enter name: ")
    
    address = input("enter address: ")
    all_addresses.append(address)
    contact["address(es)"] = address
        
    phone = input("enter phone number: ")
    phone.append(phone)
    contact["phone number(s)"] = phone

    email = input("Enter email: ")
    email.append(email)
    contact["email(s)"] = email
    contact_list.append(contact)


def view_contacts(contact_list):
    if len(contact_list) == 0:
        print("There aren no contacts.")
    else:
        for i in range(len(contact_list)):
            print(i+1, contact_list[i])


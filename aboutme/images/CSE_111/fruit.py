"""
1. Open a new blank file in VS Code and save it as fruit.py
2. Copy and paste this code at the top of your fruit program:
def main():
    # Create and print a list named fruit.
    fruit_list = ["pear", "banana", "apple", "mango"]
    print(f"original: {fruit_list}")
3. Add code to reverse and print fruit_list.
4. Add code to append "orange" to the end of fruit_list and print the list.
5. Add code to find where "apple" is located in fruit_list and insert "cherry" before "apple" in the list and print the list.
6. Add code to remove "banana" from fruit_list and print the list.
7. Add code to pop the last element from fruit_list and print the popped element and the list.
8. Add code to sort and print fruit_list.
9. Add code to clear and print fruit_list.
10.At the bottom of your program write a call to the main function.
"""

def main():
    try:
       #Create and print a list named fruit_list.
        fruit_list = ["pear", "banana", "apple", "mango"]
        print(f"original: {fruit_list}")
        
        #Reverse and print the fruit_list list.
        fruit_list.reverse()
        print(f"reversed: {fruit_list}")
       
        #Add code to append "orange" to the end of fruit_list and print the list.
        fruit_list.apprnd("orange")
        print(f"append orange: {fruit_list}")

        # Find location of "apple" in fruit_list then insert
        #"cherry" before "apple" then print list then print list
        index = fruit_list.index("apple")
        fruit_list.insert(index, "cherry")
        print(f"insert cherry: {fruit_list}")

        # Remove "banana"from fruit_list and print
        fruit_list.remove("banana")
        print(f"remove banana: {fruit_list}")

        # Add code to pop last element from list  and print the popped element and list.
        last = fruit_list.pop()
        print(f"pop {last}: {fruit_list}")

        # Add code to sort and print list
        fruit_list.sort()
        print(f"sorted: {fruit_list}")

        # Add code to clear and print list
        fruit_list.clear()
        print(f"cleared: {fruit_list}")

        # At bottom of program write call to main function
    except IndexError as index_error:
        print(type(index_error).__name__, index_error, sep = ": ")

if __name__=="__main__"():
    main()
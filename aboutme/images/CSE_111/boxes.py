# Import the math module so we can call math.ceil function.
import math

# Get two numbers 
num_items = int(input(f'enter the number of items: '))
items_per_box = int(input(f'Enter the number of items per box: '))

# Figure out the number of boxes, divide & then call math.ceil
num_boxes = math.ceil(num_items / items_per_box)

print(f'for {num_intems:} items, packing {items_per_box}')
f' items in each box, you will need {num_boxes} boxes'
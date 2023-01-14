"""
The size of a car tire in the United States is represented with three numbers like this: 205/60R15. The first number
is the width of the tire in millimeters. The second number is the aspect ratio. The third number is the diameter in 
inches of the wheel that the tire fits. The volume of space inside a tire can be approximated with this formula:

v = 
π * w ** 2 * a * (w * a + 2,540 + d) / 10,000,000,000
v is the volume in liters,
π is the constant PI, which is the ratio of the circumference of a circle divided by its diameter (use math.pi),
w is the width of the tire in millimeters,
a is the aspect ratio of the tire, and
d is the diameter of the wheel in inches.
"""

# Import math module to use math.Pi
# Get the width of the tire
# Get the aspect ratio of the tire
# Get the diameter of the wheel in inches


W = input('Enter the width of the tire: ')
AR = input('Enter the aspect ratio of tire: ')
D = input('Enter diameter of the tire: ')

 # Compute area of the tires
import math
print(math.pi)

Volume = math.pi * W**2 * AR * (W * AR + 2540 * D) / 10000000000
print('volume')

#import datetime

from datetime import datetime
current_date = datetime.now()
print ('Today is:' + str(current_date))
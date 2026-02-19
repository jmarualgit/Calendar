import Calendar
import os

path = ".//Files"

for i, item in enumerate(os.listdir(path)):
   print(str(i + 1) + ": " + item)

calendar = input("Type calendar # to open and press enter\n")

# set calendar as input
calendar = os.listdir(path)[int(calendar) - 1]
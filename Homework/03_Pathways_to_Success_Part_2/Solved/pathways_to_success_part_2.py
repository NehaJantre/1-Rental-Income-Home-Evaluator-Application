"""Pathways to Success Part 2."""
# Import the csv library
import csv
from pathlib import Path

# Create a path to the csv file called `quarterly_data.csv`
csvpath = Path("quarterly_data.csv")

# Open the csv path, read the data, and print each row
with open(csvpath) as csvfile:
    data = csv.reader(csvfile)
    for row in data:
        print(row)

"""Extension.

Create a variable above the `for` loop named `Counter`
and set it equal to zero. Then, every time a new row
is read within the `for` loop, add a value of 1 to
this variable.
"""

csvpath = Path("quarterly_data.csv")
counter = 0
with open(csvpath) as csvfile:
    data = csv.reader(csvfile)
    for row in data:
        # For every new row, add one to `counter`
        counter = counter + 1

        # Print the row counter and then the row
        print("row counter ", counter)
        print(row)

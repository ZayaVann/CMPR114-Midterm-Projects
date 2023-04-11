#########################################################################
# Program: Midterm Project 3 Part a
# Programmer: Isaiah Vann
# Class: CMPR 114 Spring 2023
# Instructor: Durendal Huynh
# Date: 4/10/2023
#########################################################################

# Project #3 (based on Chapter 7 Lists and Tuples)
# Create a 1-D list with the numbers 20-30 and get the sum and average of the numbers.
#

# Initializing a list for numbers
numlist = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29 , 30]

list_total = 0
count = 0

for num in numlist:
    # Accumulating total value of numbers list
    list_total += num
    count += 1 # count accumulation

# Calculating the average of numbers list
list_avg = list_total / count

print(f"The Sum of the list is: {list_total}.")
print(f'The Avgerage of the list is: {list_avg}.')
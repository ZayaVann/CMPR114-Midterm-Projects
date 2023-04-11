#########################################################################
# Program: Midterm Project 3 Part d
# Programmer: Isaiah Vann
# Class: CMPR 114 Spring 2023
# Instructor: Durendal Huynh
# Date: 4/10/2023
#########################################################################

# Project #3 (based on Chapter 7 Lists and Tuples)
# Create a list of 5 random names and using a for loop print the names in console
#

# Random list of names
names_list = ['John', 'Davy', 'Roger', 'Esmerelda', 'Rebecca']

count = 1# loop counter
for name in names_list:
    # Displaying name in each index
    print(f'Names {count}: ' + name)
    count += 1
print()
#########################################################################
# Program: Midterm Project 2 Part a
# Programmer: Isaiah Vann
# Class: CMPR 114 Spring 2023
# Instructor: Durendal Huynh
# Date: 4/10/2023
#########################################################################

# Project #2 (based on Chapter 6 Files and Exceptions)
# Write a program that will read the coffee text file 
# (please download from module 8 midterm). 
# Display the entire file on the console.

def main():
    """ Main Function """

    # ---Calling Functions---
# Reading the Coffe Text File
    ReadCoffee()

def ReadCoffee():
    """ Read Coffee File. Display Contents. """
    # Opening a file to READ
    outNameFile = open('Coffee.txt', 'r')

    # Reading from the file and setting value
    readNameFile = outNameFile.read()

    # Closing file
    outNameFile.close()

    # Printing contents read from file
    print("\nDisplaying User Data: \n" + readNameFile)

# Call the main function
if __name__ == '__main__':
    main()
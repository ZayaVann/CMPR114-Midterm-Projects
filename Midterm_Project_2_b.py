#########################################################################
# Program: Midterm Project 2 Part b
# Programmer: Isaiah Vann
# Class: CMPR 114 Spring 2023
# Instructor: Durendal Huynh
# Date: 4/10/2023
#########################################################################

# Project #2 (based on Chapter 6 Files and Exceptions)
# Write a program that will write to the coffee text file. 
# Ask user to enter their favorite coffee brand, 
# with the prod number 99-8888, and price $9.88.  
# Verify by reading the file content.

def main():
    """ Main Function """

    # ---Calling Functions---
# Writing to Coffee Text File
    WriteCoffee()
    print()
# Reading the Coffee Text File
    ReadCoffee()

def WriteCoffee():
    """ Write to Coffee File. """
    # Get Coffee Details
    fav_coffee = input("Enter your favorite coffee brand: ")
    prod_num = (input("Enter the prod number (i.e. 99-8888): "))
    price = float(input("Enter the price: $"))
    
    # Opening a file to WRITE
    outNameFile = open('Coffee.txt', 'w')

    # Writing values to a file
    outNameFile.write('Coffee Written: ' + fav_coffee + '\n')
    outNameFile.write('Prod Number: ' + prod_num + '\n')
    outNameFile.write('Price: $' + str(price) + '\n')

    # Closing file
    outNameFile.close()

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
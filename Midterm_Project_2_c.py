#########################################################################
# Program: Midterm Project 2 Part c
# Programmer: Isaiah Vann
# Class: CMPR 114 Spring 2023
# Instructor: Durendal Huynh
# Date: 4/10/2023
#########################################################################

# Project #2 (based on Chapter 6 Files and Exceptions)
# Create a text file that contains your expenses for last month in the following categories: 
# Rent
# Gas
# Food
# Clothing
# Car payment

# Write a program to prompt user for each of the 5 categories and write to this text file. 
# You may create and or format text file anyway you wish. 
# Then read and print the content of the file

def main():
    """ Main Function """

    # ---Calling Functions---
# Writing to Expenses Text File
    WriteExpenses()
    print()
# Reading the Expenses Text File
    ReadExpenses()

def WriteExpenses():
    """ Write Expenses to Expenses File. """
    # Get Expenses Details
    print("___Entering Expenses from last month___")
    rent = float(input("Enter the rent payment: $"))
    gas = float(input("Enter the gas payment: $"))
    food = float(input("Enter the food payment: $"))
    clothing = float(input("Enter the clothing payment: $"))
    car = float(input("Enter the car payment: $"))
    
    # Opening a file to WRITE
    outNameFile = open('Expenses.txt', 'w')

    # Writing values to a file
    outNameFile.write('___Entering Expenses from last month___\n')
    outNameFile.write('Rent Payment: $' + str(rent) + '\n')
    outNameFile.write('Gas Payment: $' + str(gas) + '\n')
    outNameFile.write('Food Payment: $' + str(food) + '\n')
    outNameFile.write('Clothing Payment: $' + str(clothing) + '\n')
    outNameFile.write('Car Payment: $' + str(car) + '\n')

    # Closing file
    outNameFile.close()

def ReadExpenses():
    """ Read Expenses File. Display Contents. """
    # Opening a file to READ
    outNameFile = open('Expenses.txt', 'r')

    # Reading from the file and setting value
    readNameFile = outNameFile.read()

    # Closing file
    outNameFile.close()

    # Printing contents read from file
    print("\nDisplaying your expenses for last month: \n" + readNameFile)

# Call the main function
if __name__ == '__main__':
    main()
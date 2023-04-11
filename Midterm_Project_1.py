#########################################################################
# Program: Midterm Project 1
# Programmer: Isaiah Vann
# Class: CMPR 114 Spring 2023
# Instructor: Durendal Huynh
# Date: 4/10/2023
#########################################################################

# Project #1 (based on Chapter 5 functions) for the program below be sure to use functions.
# 

def main():
    """ Main Function """
    # Nutrition variables
    fat = 0
    carbs = 0
    fat_calories = 0
    carb_calories = 0

    # ---Calling Functions---
# Getting Grams of Fat
    fat = GetFatGrams()
# Getting Grams of Carbs
    carbs = GetCarbGrams()
# Setting value of calories from fat
    fat_calories = CalcFromFat(fat)
# Setting value of calories from carbs
    carb_calories = CalcFromCarbs(carbs)
# Displaying Nutrition Information
    ShowNutritionVal(fat_calories, carb_calories)

def GetFatGrams():
    """ User Input for Fat Grams """
    grams_of_fat = int(input("Enter the amount of grams of fat: "))
    return (grams_of_fat)

def GetCarbGrams():
    """ User Input for Carbohydrate Grams """
    grams_of_carbs = int(input("Enter the amount of grams of carbs: "))
    return (grams_of_carbs)

def CalcFromFat(fat):
    """ Calculate # of calories that result from fat """
    calories_from_fat = (fat * 9)
    return (calories_from_fat)

def CalcFromCarbs(carbs):
    """ Calculate # of calories that result from carbs """
    calories_from_carbs = (carbs * 4)
    return (calories_from_carbs)

def ShowNutritionVal(fat_cals, carb_cals):
    """ Displaying calories for nutrient """
    print(f'The amount of of calories from the grams of fat is: {fat_cals}')
    print(f'The amount of of calories from the grams of carbs is: {carb_cals}')

# Call the main function
if __name__ == '__main__':
    main()
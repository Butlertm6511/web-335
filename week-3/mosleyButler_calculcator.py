"""
    Title:methods_ex1.py
    Author: Professor Krasso
    Date: 11 August 2022
    Modified By:TiaNiecia Mosley Butler
    Description: Code that teaches how to create functions in Python.

"""

""""
Defining function for function adding, subtracting, dividing, and multipling.
Function takes two parameter for numbers and preforms arithmetic operation to get total.

"""  

def add_function(num1, num2):
    total_A= num1 + num2
    return total_A


def subtract_function(num3, num4):
    total_S= num3 - num4
    return total_S

def divide_function(num5, num6):
    total_D= num5 / num6
    return total_D

def multiply_function(num7, num8):
    total_M= num7 * num8
    return total_M

#Created variables to test functions

num1 = 6
num2 = 2
num3 = 7
num4 = 5
num5 = 9
num6 = 3
num7 = 2
num8 = 2



total_A= add_function(num1,num2)
total_S = subtract_function(num3, num4)
total_D = divide_function(num5, num6)
total_M = multiply_function(num7, num8)


#Create string and storing it in the output variable.
output=f'{num1} + {num2} is {total_A}\n{num3} - {num4} is {total_S}\n{num5} / {num6} is {total_D}\n{num7} * {num8} is {total_M}'

#Printing out of the string.
print(output)
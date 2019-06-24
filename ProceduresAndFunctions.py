'''
Created on Jun 23, 2019

@author: karl
'''

#Procedures are used to combine a sequence of repeatable tasks into one task

#Define a procedure using the following code
def example():
    print("example")

#You can add lines of code within a procedure that will be executed when it is called
def printLines():
    print("Hello")
    print("World")
    print("!")
 
#This is an example of how to call a procedure   
printLines()

#Functions are similar to procedures but they include a return value
def getName():
    print("What is your name")
    return(input("Name: "))

#Since the function, getName, has a return statement its value will be used where it is called
name = getName()
print("Your name is " + name)

#A way to make procedures and functions more versatile using parameters
#Parameters are used when calling procedures or functions to change their behavior
def addNumbers(num1, num2):
    return(num1 + num2)

#When calling a procedure or functions, include the parameters in the parentheses separated by commas
print(addNumbers(4, 5))


'''
Created on Jun 23, 2019

@author: karl
'''

#Classes are blueprints used to make objects in your program

#Create a class using the following code
class Rectangle():  #This class contains to variables to represent the length and width of a rectangle
    width = 0
    length = 0
    
#This blueprint can now be used to create an instance of the rectangle object in our code
myRectangle1 = Rectangle()

#This rectangle object contains instances of the variables within the class that can be accessed and changed
myRectangle1.length = 5
myRectangle1.width = 10

#Since a class is only a blueprint for an object, I can use it to create another instance of a rectangle and set its dimensions
myRectangle2 = Rectangle()
myRectangle2.length = 2
myRectangle2.width = 4

#Since myRectangle1 and myRectangle2 are different instances of the same class, their dimensions are contained individually with both objects
print("myRectangle1 Dimensions: " + str(myRectangle1.length) + ", " + str(myRectangle1.width))
print("myRectangle2 Dimensions: " + str(myRectangle2.length) + ", " + str(myRectangle2.width))

#Constructors can be used in classes to make perform a set of actions when a class is instantiated
class Student():
    name = ""
    grade = 0
    
    def __init__(self, name="N/A", grade=0):    #This is the definition of the constructor for this class. It is taking parameters self, which is the object being instantiated, name, and grade
        print("New student created")
        #The next two lines use the parameters to set the value of variables within the class
        self.name = name
        self.grade = grade

#Since Student has a constructor, parameters in the constructor are used in the instantiation of a class
myStudent1 = Student("Billy", 9)    #We do not need to include self in the instantiation because self is referring to the object being created
myStudent2 = Student("Bob", 10)
myStudent3 = Student()              #The parameters in the constructor included default values that would be used if they weren't set when the class is instantiated

print(myStudent1.name + " is in grade " + str(myStudent1.grade))
print(myStudent2.name + " is in grade " + str(myStudent2.grade))
print(myStudent3.name + " is in grade " + str(myStudent3.grade))
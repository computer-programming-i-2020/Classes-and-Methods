'''
Created on Jun 23, 2019

@author: karl
'''

#Methods are like functions, except they are contained within a class

class Rectangle():
    width = 0
    length = 0
    
    def __init__(self, width, length):
        self.width = width
        self.length = length
        
    def getArea(self):  #This is an example of a method in a class. This method can be called by the program using an instance of the class
        return(self.width * self.length)
    
myRectangle = Rectangle(2, 4)

#Calling a method is the same as calling a function except you have to use the path of the object created to reach the method
print(myRectangle.getArea())
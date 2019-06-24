'''
Created on Jun 23, 2019

@author: karl
'''

#Programs use a method called main to execute code that they don't want executed if it is imported into another program
def main():
    #None of this code will run if imported
    print("This program is running")
    myTriangle = Triangle(5, 10)
    myTriangle.getArea()

#This class will be created in a program that imports this program
class Triangle():
    width = 0
    length = 0
    
    def __init__(self, width, length):
        self.width = width
        self.length = length
        
    def getArea(self):
        return(self.width * self.length / 2)
    
#This next if statement will check if the programming running matches the name of the program where main is defines and run if it does.
if __name__ == "__main__":
    main()
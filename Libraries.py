'''
Created on Jun 23, 2019

@author: karl
'''

#Libraries are collections of functions and classes that can be imported into a program

#Here is an example of importing a library
import Classes          #Importing this program will execute all of the code contained in it
import MainMethod       #Since this program was contained in a main method, it will import classes and functions but it won't run the code in its main method
import tkinter as tk    #Using the keyword, "as", we have the option to give an imported library an abbreviated name to easily refer to it later
import PackageExample   #You can also import a package, which contains multiple files
from PackageExample import LibrariesUsingPackages2 #Since the package is imported, you can import files contained within the package

#Since we have imported these libraries, we can access classes they created
myStudent = Classes.Student("Joe", 11)
myTriangle = MainMethod.Triangle(2, 4)

print(myStudent.name)
print(myTriangle.getArea())

#When we imported classes, it created instances of objects that we can access
print(Classes.myStudent1.name)

#We imported a package and file contained within
PackageExample.LibrariesUsingPackages2.packageMethod()
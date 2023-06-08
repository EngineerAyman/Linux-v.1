'''
*********************************************
 * Author:          AYMAN HARRAZ
 * Creation Data:   17 MAY, 2023
 * Version:         v1.0
 ********************************************
Lab 7 session 2 
Write a python code that ask the user to open a new txt file and write on it

''' 


# Enter your Full_Name 
myName=input ("Hello,Please Enter your Name : " )
# Enter your Age
Age=input ("Hello,Please Enter your Age : " )
# Enter your Faculty
Faculty=input ("Hello,Please Enter your Faculty : " )


file_1= open("Ayman.txt","a+")
file_1.write("My Name is :" + (myName)+ "\n")
file_1.write("My Age is : " + (Age)+ "\n")
file_1.write("My Faculty is : " + (Faculty)+ "\n")

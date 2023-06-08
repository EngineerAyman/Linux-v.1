'''
*********************************************
 * Author:          AYMAN HARRAZ
 * Creation Data:   10 MAY, 2023
 * Version:         v1.0
 ********************************************
Lab 5 session 2 
Write a python code that ask the user to enter list 
and check a random number exist or not
'''
list = input ("Please Enter 5 Numbers : ").split(',')

a = input (" Please Enter your number :")


if a in list :

    print ("The Number is Exist")

else:

    print ("The Number not Exist")


'''
*********************************************
 * Author:          AYMAN HARRAZ
 * Creation Data:   10 MAY, 2023
 * Version:         v1.0
 ********************************************
Lab 6 session 2 
Write a python code that ask the user to test 2 fun
''' 

print("Please Enter Number 1 for Lower fun fun  or  Number 2 for is Lower fun  : ")

Choose_Num = (int) (input("Please choose Number of fun : "))

if Choose_Num == 1 :
   # Lower fun
    print ("Converts a string into lower case")
    txt = "Hello my FRIENDS"
    x = txt.lower()
    print(x)

elif Choose_Num == 2 :
   # is Lower fun
    print ("Returns True if all characters in the string are lower case")
    txt = "hello world!"
    x = txt.islower()
    print(x)
else:
	print ("No Fun ")
'''
*********************************************
 * Author:          AYMAN HARRAZ
 * Creation Data:   10 MAY, 2023
 * Version:         v1.0
 ********************************************
Lab 7 session 2 
Write a python code that ask the user to implement and test 4 fun
''' 
def SET_BIT(x,bit):
	x = x | (1 << bit)
	return x
	
def CLR_BIT(x,bit):
	x = x & (~(1 << bit))
	return x
    
  	
def GET_BIT(x,bit):
	x = x & (1 << bit)
	return x
	
def TOG_BIT(x,bit):
    x = x ^ (1 << bit)
    return x

a = (int) (input("Please Enter The Number "))
print(SET_BIT(a,1))
print(CLR_BIT(a,1))
print(GET_BIT(a,1))
print(TOG_BIT(a,1))
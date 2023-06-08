'''
*********************************************
 * Author:          AYMAN HARRAZ
 * Creation Data:   17 MAY, 2023
 * Version:         v1.0
 ********************************************
Lab 8 session 2 
Write a python code that make a Calc using file Handling

''' 
def ADD (n1,n2):
    return n1+n2

def SUB (n1,n2):
    return n1-n2

def MUL (n1,n2):
    return n1*n2

def DIV (n1,n2):
 if n2==0:
    print("invalid input")
    return n1/n2
 
n1 = (float) (input("Please Enter Number 1 : "))
n2 = (float) (input("Please Enter Number 2 : "))

operation = (input("Please Choose operation : "))

f1 =open ("Calc.text" ,"a+")
f1.write(str(n1)+operation+str(n2))
if operation == '+':
    print(ADD(n1,n2))
    f1.write("="+str(ADD(n1,n2))+"\n")
if operation == '-':
    print(SUB(n1,n2))
    f1.write("="+str(SUB(n1,n2))+"\n")
if operation == '*':
    print(MUL(n1,n2))
    f1.write("="+str(MUL(n1,n2))+"\n")
if operation == '/':
    print(DIV(n1,n2))
    f1.write("="+str(DIV(n1,n2))+"\n")



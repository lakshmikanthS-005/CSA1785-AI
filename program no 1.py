# Program make a simple calculator
def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y
print("SELECT THE OPERATION YOU WANT:")
print("1:ADDITION")
print("2:SUBTRACTION")
print("3:MULTIPLICATION")
print("4:DIVISION")
while True:
    operation=input("ENTER THE OPERATION YOU WANT(a/s/m/d):")
    if operation in ('a','s','m','d'):
        num1=float(input("ENTER THE FIRST NUMBER:"))
        num2=float(input("ENTER THE SECOND NUMBER:"))
        if operation=='a':
            print(num1,"+",num2,"=",add(num1,num2))
        elif operation=='s':
            print(num1,"-",num2,"=",subtract(num1,num2))
        elif operation=='m':
            print(num1,"*",num2,"=",multiply(num1,num2))
        elif operation=='d':
            print(num1,"/",num2,"=",divide(num1,num2))
        break
    else:
        print("( invalid input )")
        print("enter yout choice 1.continue(yes)  2.discontinue(no):")
        option=input("choice:")
        if option==("yes"):
            print("program continues....")
        elif option==("no"):
            print("program discontinues...")
            break
 output:           
   SELECT THE OPERATION YOU WANT:
1:ADDITION
2:SUBTRACTION
3:MULTIPLICATION
4:DIVISION
ENTER THE OPERATION YOU WANT(a/s/m/d):5
( invalid input )
enter yout choice 1.continue(yes)  2.discontinue(no):
choice:yes
program continues....
ENTER THE OPERATION YOU WANT(a/s/m/d):5
( invalid input )
enter yout choice 1.continue(yes)  2.discontinue(no):
choice:no
program discontinues...
        

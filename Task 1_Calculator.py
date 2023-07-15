#This is a simple calculator using functions

#DEFINING THE FUNCTIONS 
def add():
    num1=eval(input("Enter num1"))
    num2=eval(input("Enter num2"))
    print('SUM IS:',num1+num2)

def subtract():
    num1=eval(input("Enter num1"))
    num2=eval(input("Enter num2"))
    print('DIFFERENCE IS:',num1-num2)

def pdt():
    num1=eval(input("Enter num1"))
    num2=eval(input("Enter num2"))
    print('PRODUCT IS:',num1*num2)

def remainder():
    num1=eval(input("Enter num1"))
    num2=eval(input("Enter num2"))
    print('REMAINDER IS:',num1%num2)

def divide():
    num1=eval(input("Enter num1"))
    num2=eval(input("Enter num2"))
    print('QUOTIENT IS:',num1/num2)

def floor():
    num1=eval(input("Enter num1"))
    num2=eval(input("Enter num2"))
    print('FLOOR VALUE IS:',num1//num2)

def square_root():
    num1=eval(input("Enter num1"))
    num2=eval(input("Enter num2"))
    print('SQUARE ROOT IS:',num1**(1/2))

def power():
    num1=eval(input("Enter num1"))
    num2=eval(input("Enter num2"))
    print('POWER IS:',num1**num2)

while True:
    choice=int(input('Enter a number of your choice:\n[1-add,2-Subtract,3-Product,4-Remainder,5-Divide,6-Floor division,7-Square root,8-Find power]'))
    if choice==1:
            add()
    elif choice==2:
            subtract()
    elif choice==3:
            pdt()
    elif choice==4:
            remainder()
    elif choice==5:
            divide()
    elif choice==6:
            floor()
    elif choice==7:
            square_root()
    elif choice==8:
            power()
    else:
        print('INVALID CHOICE! TRY AGAIN')
    ask=input('Would you like to try again?\nY/N:')
    if ask=='y' or ask=='Y':
        continue
    else:
        print('Thank you for using our application!!')
        break

        
















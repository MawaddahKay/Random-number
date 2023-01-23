Author: Mawaddah Kay
#calculate the two numbers

# This function addition of the two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y

# user input the number
while True:
    try:
        number1 = float(input("Input  the number:"))     
        number2 = float(input('Input the second number:'))
        x = input("select the operator (+,-,*,/): ")  
    except ValueError:
        print("Please enter the correct value")
        continue

    try:
    #calculate the total of 2 number
        if x == '+':
            print(number1,'+',number2,'=',add(number1,number2))
        elif x == '-':
            print(number1,'-',number2,'=',subtract(number1,number2))
        elif x == '*':
            print(number1,'*',number2,'=',multiply(number1,number2))
        elif x =='/':
            print(number1,'/',number2,'=',divide(number1,number2))
        
    except ZeroDivisionError:
        print("Cannot devide by zero")
    except TypeErro:
        print("You past")

# check if user wants another calculation
    # break the while loop if answer is no
    next_calculation = input("Do you want to calculate again? (yes/no): ")
    if next_calculation == "no":
        break
    else:
        print("please choose the correct operator(+, -, *,/)")
    
           

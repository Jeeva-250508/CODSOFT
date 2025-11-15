def addition(a,b):
    return a+b
def subtraction(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a,b):
    if b!=0:
        return a/b
    else:
        return("zero division is not possible")

num1=int(input("Enter number 1:"))
num2=int(input("Enter number 2:"))
print('''Available operations are:
                    1.ADDITION
                    2.SUBTRACTION
                    3.MULTIPLICATION
                    4.DIVISION''')

Try_again="y"
while Try_again.lower()=="y":
    choice=int(input("Enter a choice 1-4:"))
    if choice==1:
        print("The sum of two number",num1,"and",num2,"is",addition(num1,num2))
    elif choice==2:
        print("The difference of two number",num1,"and",num2,"is",subtraction(num1,num2))
    elif choice==3:
        print("The product of two number",num1,"and",num2,"is",multiplication(num1,num2))
    elif choice==4:
        print("The division of two number",num1,"and",num2,"is",division(num1,num2))
    else:
        print("Try again")
    Try_again=input("Do you want to do again(y/n):")

    
        

  


## Advance Calculator 

# Feauture 

# 1. Give user choice that what 
# he want to do ( mult, add , sub etc )

# 2. Fuction for each thing 
# And Advance option as well ( further one )


greeting = print("Welcome to Ulimate Calculator")

def options():
    
    print("What do you want to Do Today ?\n ")
    print("""Choose From This List:\n 1.Addition\n 2.Substraction\n 3.Division\n 4.Multiplication\n 5.Exit""")
options()
choice = (int(input("Enter Your Choice: ")))

def addition(a,b):
    print(f"Here is Your Addition of Number:{a+b}")
    print("================")
    options()

def subsction(a,b):
    print(f"Subtraction of these Number are:{a-b} ")
    print("================")
    options()


def division(a,b):
    print(f"Here is divison of Your Number: {a*b}")
    print("================")
    options()

def multipication(a,b):
    print(f"Here is Your Product :{a*b}")
    print("================")
    options()

if choice == 1:
    a = int(input("Enter You Number: "))
    b = int(input("Enter You Number: "))
    addition(a,b)

elif choice == 2 :
    a = int(input("Enter You Number: "))
    b = int(input("Enter You Number: "))
    subsction(a,b)
elif choice == 3 :
    a = int(input("Enter You Number: "))
    b = int(input("Enter You Number: "))
    division(a,b)
elif choice == 4 :
    a = int(input("Enter You Number: "))
    b = int(input("Enter You Number: "))
    multipication(a,b)
else:
    print("Thankyou For Using our Services")


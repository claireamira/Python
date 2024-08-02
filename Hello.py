print("Choose an operation")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Modulus")

choice =int(input("Select an operation"))

num1 = int(input("Enter first number "))
num2 = int(input("Enter second number "))

if choice == 1 :
    print("Answer: ", num1+num2)
elif choice == 2:
    print("Answer: ", num1-num2)
elif choice == 3:
    print("Answer: ", num1*num2)
elif choice == 4:
    print("Answer: ", num1%num2)
elif choice ==5:
    print("Answer: ", num1%num2)
else:
    print("Enter a valid choice")





age= 23
gender= 'female'

if age>18 and gender== 'female':
    print("Allowed")
else:
    print("Not allowed.") 


#Prompt user to enter grade 

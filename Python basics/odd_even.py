# To find number odd or even

number = input("Enter the number to test: \n");

def checkOddEven(number):
    if (number % 2 == 0):
        print("The number is even")
    else:
        print("The number is odd")

checkOddEven(int(number))
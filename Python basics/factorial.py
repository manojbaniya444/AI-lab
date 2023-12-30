# to calculate the factorial

def factorial(number):
    if number == 0 or number == 1:
        return 1
    return number * factorial(number - 1)

number = input("Enter the number to calculate factorial: ")
fact = factorial(int(number))
print("The factorial is: ", fact)
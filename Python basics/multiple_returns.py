num1 = input("Enter the number 1")
num2 = input("Enter the number 2")

def performOperation(a,b):
    sum = a + b
    sub = a - b
    mul = a * b
    div = a / b

    return sum, sub , mul, div
    

a,b,c,d = performOperation(int(num1), int(num2))    

print("sum: ",a)
print("Difference: ", b)
print("Multiply: ",c)
print("Division: ",d)
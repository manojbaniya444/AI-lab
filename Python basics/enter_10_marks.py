marks = [] 

def enterMarks():
    for i in range(10):
     markEntered = input("Enter the mark:")
     marks.append(markEntered)

enterMarks()
print(marks)
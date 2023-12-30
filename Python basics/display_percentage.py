# To check the grade based on the provided marks

mark = input("Enter the marks you obtained: \n")

def checkGrade(markObtained):
    if (markObtained >=80):
        print("You got grade Distinction.")
    elif (markObtained >=65 and markObtained < 80):
        print("You got grade First division")
    elif (markObtained >=55 and markObtained < 65):
        print("You got grade Ssecond Division.")
    elif (markObtained >=40 and markObtained < 55):
        print("You got grade Third division")
    elif (markObtained < 40):
        print("You Fail")

checkGrade(int(mark))
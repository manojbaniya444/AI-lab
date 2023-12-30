# To swap cases: uppercase to lowercase and lowercase to uppercase
     
entered_string = input("Enter the string you want to swap cases.")

def swap_cases(string):
    swapped = []
    # swap logic goes here
    for character in string:
        # we will get True if the character is uppercase
        if character.isupper():
            swapped.append(character.lower())
        else:
            swapped.append(character.upper())
    return swapped

swapped = swap_cases(entered_string)
print("Before swapping: \n", entered_string)
print("After swapping: \n", swapped)
sentence = input("Enter the sentence to count the number: \n")

dictionary = {}

for character in sentence:
    if character not in dictionary:
        dictionary[character] = 1
    else:
        dictionary[character] = dictionary[character] + 1

print(dictionary)

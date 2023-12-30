sentence = input("Enter the sentence: \n")

def countWords(sentence):
    count = sentence.split()
    return len(count)

print(countWords(sentence))
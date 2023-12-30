dictionary = {
    "A": 5,
    "B": 10,
    "C": 20
}

def accumulateValue(dict):
    accumulator = 0
    for key in dict:
        accumulator = accumulator + dictionary[key]
    return accumulator

result = accumulateValue(dictionary)
print("The sum of value in dictionary is: ", result)
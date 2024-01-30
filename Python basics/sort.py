list = [5,4,11,13,51]

def sort(list):
    for i in range(len(list)):
        for j in range(i + 1, len(list)):
            if (list[i] > list[j]):
                temp = list[i]
                list[i] = list[j]
                list[j] = temp
    return list

print(sort(list))
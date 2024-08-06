list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

def list_difference(list1, list2):
    return [item for item in list1 if item not in list2]

print(list_difference(list1, list2))  # -> [1, 2]

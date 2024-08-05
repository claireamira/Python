def get_frequency(elements):
    frequency = {}
    for element in elements:
        if element in frequency:
            frequency[element] += 1
        else:
            frequency[element] = 1
    return frequency

# Sample Data
list1 = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

# Get the frequency of elements
print(get_frequency(list1))  # -> {1: 1, 2: 2, 3: 3, 4: 4}

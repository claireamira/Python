def unique_elements(input_list):
    encountered_elements = set()
    result_list = [encountered_elements.add(element) or element for element in input_list if element not in encountered_elements]
    return result_list

list = [1, 2, 2, 3, 4, 4, 5, 1, 6, 7, 8, 7, 9, 6, 10]

new_list = unique_elements(list)
print(new_list)

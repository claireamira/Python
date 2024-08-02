def letter_counter(input_string):
    lower_string = input_string.lower()
    count = {}

    for char in lower_string:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1

    return count

input_string = "Evangeline"
result = letter_counter(input_string)
print(result)

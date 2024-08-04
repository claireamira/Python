def count_matching_strings(strings):
    count = 0
    for string in strings:
        if len(string) >= 2 and string[0] == string[-1]:
            count += 1
    return count

list = ['abc', 'xyz', 'aba', '1221']

result = count_matching_strings (list)
print(result)

def second_smallest(numbers):
   
    first_min = second_min = float('inf')

    for num in numbers:
        if num < first_min:
            second_min = first_min
            first_min = num
        elif first_min < num < second_min:
            second_min = num

    return second_min if second_min != float('inf') else None

list1 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

print(second_smallest(list1)) 


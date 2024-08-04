def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def all_primes(numbers):
    for num in numbers:
        if not is_prime(num):
            return False
    return True

list1 = [0, 3, 4, 7, 9]
list2 = [3, 5, 7, 13]
list3 = [1, 5, 3]

print(all_primes(list1))  
print(all_primes(list2))  
print(all_primes(list3)) 

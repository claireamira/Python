def check_palindrome(user_string):
   
    lower_string = user_string.lower()

    is_palindrome = (lower_string == lower_string[::-1])

    return is_palindrome

user_string = input("Enter a string to check if it's a palindrome: ")

if check_palindrome(user_string):
    print(f"'{user_string}' is a palindrome.")
else:
    print(f"'{user_string}' is not a palindrome.")

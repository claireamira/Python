my_number = int(input("Enter the number for which you want the multiplication table: "))

my_multiple = int(input("Enter the number of multiples: "))

print(f"\nMultiplication table for {my_number} up to {my_multiple} multiples:\n")

for i in range(1, my_multiple + 1):
    result = my_number * i
    print(f"{my_number} x {i} = {result}")




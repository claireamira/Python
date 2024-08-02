def power(base, exponent):
    if exponent == 0:
        return 1
    elif exponent ==1:
        return base
    else:
        return base * power(base, exponent - 1)

result = power(2, 3)
print(result)

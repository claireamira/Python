def fibonacci (n):
    f = [0,1]

    for i in range(2, n):
        f.append(f[i-1] + f[i-2])

    return f    
print(fibonacci(9))   
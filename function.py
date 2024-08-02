def drawTable(n):
    for i in range(n):
        for k in range (n):
            if i == 0:
                print(k, " ", end="")
            else:
                print(k*i, " ", end="")
        print("\n")    

drawTable(10)

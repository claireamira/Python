#myList =["Ford", "Suzuki", "Volkswagen", "Hyundai", "Mazda"]


#Looping through
#for i in range(len(myList)):
 #   print(i)
  #  print(myList[i])


#write a function to get the sum of numbers in a list    
numbers = [20, 30, 40, 50]


def getSum(numbers):
   
    total = 0
    for element in numbers:
        total += element
    return total

result = getSum(numbers)
print(result)

  #write a function that takes a list as the parameter and gets the maximum number in the list

def getMax(numbers):

    maximum= numbers[0]
    for element in numbers:
        if element > maximum:
           maximum= element
        
    return maximum

print(getMax(numbers))

#write a function to get the second largest number in a list
def getSecondLargest(numbers):
    max = 0
    second_max= 0
    for n in numbers:
        if n> max:
            prev_max= max
            max = n
            second_max = prev_max 
            
    return second_max

print(getSecondLargest(numbers))                    
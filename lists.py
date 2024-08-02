myList =["Ford", "Suzuki", "Volkswagen", "Hyundai", "Mazda"]

#access a list item
print(myList[3])

#update list
myList[4]= "Toyota"

#get the length
print(len(myList))

#add item to the list
myList.append("Land Rover")
print(myList)

myList.insert(1, "Isuzu")
print(myList)

list2=["Cat", "Vitz"]

myList.extend(list2)
print(myList)

#remove Items in a list
myList.pop()
print(myList)

myList.remove("Cat")
print(myList)

myList.clear()

# Sorting a list
numbers=[20,34, 14, 58, 22]
names=["mary" ,"Jane", "John", "Peter", "Abel"]
names.sort()
numbers.sort()

print(numbers)

#creating a tuple
fruits=("Apple", "Orange", "Banana", "Grape", "Pineapple", "Coconut")

#Accessing elements
print(fruits[0])

#Length of tuple
print(len(fruits))

print(type(fruits))

#slicing
print(fruits[2:]) #from index 2 to the last
print(fruits[1:4]) #From index 1 excluding index 4

if "Apple" in fruits:
    print("Available")

#Manipulating tuple by changing it to a list
fruits_list= list(fruits)
print(fruits_list)
fruits_list[1]="Citrus"
fruits= tuple(fruits_list)
print(fruits)

#Adding tuples
cars = ("Mazda", "Nissan")
combined_tuple = fruits + cars
print(combined_tuple)

cars = cars + ("Ford",)
print(cars)

#To delete tuple
#del cars

#Destructuring Tuples
car1, *car2= cars

print(car1)
print(car2)

#Looping though a tuple
for car in cars:
    print(car, end="-") #Specify how to separate the elements of a tuple.

#Using a while loop
i= 0
while i<len(cars):
    print(cars[i])
    i +=1

#Change into a dictionary
user = [("name","Jane"),("Age", 56),("county", "Meru"), ("Proffesion", "Teacher")]    

dictionary = {t[0]: t[1] for t in user}
print (dictionary)

#Alternative
user_dict = dict(user)
print(user_dict)

#Alternative
user2_dict = {}
for tup in user:
    user2_dict[tup[0] = tup[1]]

print(user2_dict)    
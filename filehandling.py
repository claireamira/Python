f = open("example.txt", "r") #Mode read, write, append etc

print(f.read(5)) # Reads the first five characters

print(f.readline(5)) #Reads the first 5 lines

for line in f.readlines(): #Returns a list of each line in the file so that we can loop through the lines. 
    print(line)

f.write("This is a python program on file handling.") #Clearly this is to write to the file.

f.close() #Obviously to close the file. 

#example utilization
f= open("example.txt", "r")

name= input("Enter Name: ")

content = f.read()

if name in content:
    print(f"{name} is in class today")
else:
    print(f"{name} is not in class today")    

#Removing or deleting files
import os

os.remove("example.txt")
os.mkdir("Myfolder") #Make a directory
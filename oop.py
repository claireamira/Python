class Car:
    def __init__(self, color, price, mileage):
        self.color = color
        self.price = price
        self.mileage = mileage

    def __str__(self):
        return f"color- {self.color} Price- {self.price} Mileage- {self.mileage}"    
    
    def calculateCurrentPrice(self):
        currentPrice = self.price * 1000/self.mileage
        return currentPrice

    def printColor(self):
        print(f"The color is {self.color}")

    def increasePrice(self, increase):
        self.price = self.price * (100 + increase)/100        

car1 = Car("Blue", 200000, 5000)
car2 = Car("Green", 700000, 3000)        

print(car1.color)
print(car1)

car1.colo = "Silver"

#class Person:
 #   def __init__(self, name, age, school, country, profession):
 #       self.name = name
  #      self.age = age
   #     self.school = school
    #    self.country = country
     #   self. profession = profession

        

#person1 = Person("Jane", 34, "Zindua", "Tanzania", "Teacher")

#print(person1)

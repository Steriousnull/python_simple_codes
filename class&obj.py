class Human:
    Name = None
    Age = None
    Weight = None
    Height = None

    def Sleep(self):
        print(self.Name + " is sleeping")

    def age(self):
        print(self.Name + " is "+ str (self.Age) + " years old.")


person = Human()

person.Name = "rolex"
person.Age = 45
person.Weight = 50
person.Height = 170


print(person.Name)
print(person.Age)
print(person.Weight)
print(person.Height)


person2 = Human()

person2.Name = "leo"
person2.Age = 55
person2.Weight = 65
person2.Height = 165


person.Sleep()
person.age()

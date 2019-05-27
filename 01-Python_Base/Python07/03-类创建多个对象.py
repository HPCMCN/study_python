class Dog:

    def eat(self):
        print("吃草")


dog1 = Dog()
dog1.eat()

dog2 = Dog()
dog2.eat()

dog1.name = "旺财"
dog2.name = "来福"

dog1.age = 10

print(dog1.name)
print(dog2.name)
class Dog:

    def __init__(self, color, breed, age):
        self.color = color
        self.breed = breed
        self.age = age

    def introduce(self):
        return self.color, self.breed, self.age


moses = Dog('tan', 'mutt', 8)
print(moses.color, moses.breed, moses.age)

zizi = Dog('white', 'mutt', 15)
print(zizi.color, zizi.breed, zizi.age)

print('-' * 10)

print(Dog.introduce(moses))
print(moses.introduce())
print(id(Dog.introduce(moses)) == id(moses.introduce()))

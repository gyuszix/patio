class Dog:
    def __init__(self, color, breed, age):
        self.color = color
        self.breed = breed
        self.age = age

    def introduce(self):
        return self.color, self.breed, self.age


class Employee:

    raise_amount = 1.1

    def __init__(self, name, gender, title, salary):
        self.name = name
        self.gender = gender
        self.title = title
        self.salary = salary

    def introduce(self):
        return "this employee's name is {} and he is an {} while his compensation is {}. Salary increase" \
               " for next year is {}".format(self.name, self.title, self.salary, int(self.salary * self.raise_amount))


moses = Dog('tan', 'mutt', 8)
zizi = Dog('white', 'mutt', 15)

john_doe = Employee('John Doe', 'male', 'analyst', 60000)
jane_doe = Employee("Jane Doe", 'female', 'associate', 75000)

print(john_doe.introduce())

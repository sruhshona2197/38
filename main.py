
# 83. Method Overloading Style
class Math:
    def add(self, a, b, c=0):
        return a + b + c

m = Math()
print(m.add(1, 2))
print(m.add(1, 2, 3))


# 84. Car Speed
class Car:
    def __init__(self):
        self.speed = 0

    def accelerate(self):
        self.speed += 10

c = Car()
c.accelerate()
print(c.speed)


# 85. Online Store
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Cart:
    def __init__(self):
        self.items = []

    def add(self, product):
        self.items.append(product)

    def total(self):
        return sum(i.price for i in self.items)

c = Cart()
c.add(Product("Phone", 500))
c.add(Product("Mouse", 50))
print(c.total())


# 86. Student Average
class Student:
    def __init__(self, marks):
        self.marks = marks

    def average(self):
        return sum(self.marks) / len(self.marks)

s = Student([90, 80, 100])
print(s.average())

# abs() function. This return the absolute value of a number.

age = -18
print(abs(age)) #The result will be 18.

def numbers(number): #othe way to do it def numbers(number). And add the 5
    if number is not abs(number):
        return False
    return True

result = numbers(5)
print(result)

#this is repr(). This return a string representation of an object one that's meant to be unambiguius and usable for debugging or development.

name = 'Carlos'
print(repr(name))

class Dog:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Dog('{self.name}')"

my_dog = Dog('Brandon')

print(repr(my_dog))




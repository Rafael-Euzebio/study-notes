# Object Oriented Programming
Object Oriented Programming is a [[Univesp Programming Paradigm]] based on [[Univesp Objects]].   
The objects contain *data*, that stores information about the object and *code*, also known as *methods*, that perform actions in the objects

```py
class Car():
    def __init__(self, color, brand, model):
        self.color = color
        self.brand = brand
        self.model = model
    
    def repaint(self, color):
        self.color = color

myCar = Car("White", "Toyota", "AE86")

print("I have a", myCar.color, myCar.brand, myCar.model)
myCar.repaint("Black")
print("I have a", myCar.color, myCar.brand, myCar.model)
```

```
I have a White Toyota AE86
I have a Black Toyota AE86
```

The above codeblock defines a [[Univesp Classes]] `Car()` with 3 data fields and one method

An object of that class must have these 3 data fields specified, and one of these fields can be changed by the `repaint` method


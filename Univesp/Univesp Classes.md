# Classes
Classes are [[CS50x Structures]] which allows the declaration of methods as members of the structures.

A class is an abstraction of a [[Univesp Objects]]. A class has *fields*, which specifies what information it can contain and methods that can change the value of these fields. But the information itself is unknown, until that class is instanced as an *object*

```py
class Car():
    def __init__(self, color, brand, model):
        self.color = color
        self.brand = brand
        self.model = model
    
    def repaint(self, color):
        self.color = color

```

The above codeblock creates a class `Car()` with 3 data fields:

- `color`
- `brand`
- `model`

And one method
- `repaint`

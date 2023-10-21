# Objects
An object is an instance of a [[Univesp Classes]]. While an class is an *abstraction*, an object is *concrete*.  
That means an object has information stored in it that describes that object

```py
class Car():
    def __init__(self, color, brand, model):
        self.color = color
        self.brand = brand
        self.model = model
    
    def repaint(self, color):
        self.color = color


    def printCar(self):
        print("I have a", self.color, self.brand, self.model)

myCar = Car("White", "Toyota", "AE86")


myCar.printCar()
myCar.repaint("Black")
myCar.printCar()
```
```
I have a White Toyota AE86
I have a Black Toyota AE86
```

The above codeblock creates a class `Car` and an object `myCar`, with the properties `White`, `Toyota` and `AE86`, prints it and then changes one of the properties to `Black`


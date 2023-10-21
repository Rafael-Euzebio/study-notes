# Methods
Methods are [[CS50x Functions]] inside [[Univesp Objects]] that changes the properties of said object
These methods can be called by referencing them through the object, instead of passing the object as an argument to a function


## `this` and `self`
A method can act on its own object by a keyword `self` or `this`, which references the object itself, and then access the fields of that object

### Example

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

With a *procedural programming language* like C a `struct` `Car` cannot store functions. We need to declare a `repaint` function separately and pass a pointer to the object as an argument

```c
#include <stdio.h>
#include <string.h>

typedef struct Car {
    char color [10];
    char brand [10];
    char model [10];
} Car;

void repaint(Car * car, char new_color[10]);

int main(void)
{
    Car myCar;
    strcpy(myCar.color, "White");
    strcpy(myCar.brand, "Toyota");
    strcpy(myCar.model, "AE86");

    printf("I have a %s %s %s\n", myCar.color, myCar.brand, myCar.model);
    repaint(&myCar, "Black");
    printf("I have a %s %s %s\n", myCar.color, myCar.brand, myCar.model);
}

void repaint(Car * car, char new_color[10])
{
    strcpy(car -> color, new_color);
}
```

```
I have a White Toyota AE86
I have a Black Toyota AE86
```


#### Advantages
The advantage of *Object Oriented* approach is that the same method can exist in other classes, e.g, a `Motobike` class, and be reused  
In procedural programming the `repaint` function takes strictly a `Car` structure as argument, and a second function would have to be declared for other structures

# Classes
Classes are [[CS50x Structures]] which allows the declaration of methods as members of the structures.

A class is an abstraction of a [[Univesp Objects]]. A class has *fields*, which specifies what information it can contain and [Univesp Methods] that can change the value of these fields. But the information itself is unknown, until that class is instanced as an *object*

```java
class Car {
    public Car(String color, String brand, String model) {
        this.color = color;
        this.brand = brand;
        this.model = model;
    }

    public void startCar() {
        this.speed = 100;
    }

    public int getSpeed() {
        return this.speed;
    }

    public String color; 
    public String brand;
    public String model;
    private int speed = 0;
}
```

The above codeblock creates a class `Car()` with 4 data fields:

- `color`
    - string
- `brand`
    - string
- `model`
    - string
- `speed`
    - integer

And two [[Univesp Methods]]
- `startCar()`
- `getSpeed()`

Which can directly change and return the `speed` field in an object of that class

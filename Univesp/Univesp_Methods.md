# Methods
Methods are [Functions](../CS50x/Week-1_C/CS50x_Functions.md) inside [Objects](./Univesp_Objects.md). They can interact with other objects or with the properties of its own object. A method is the *behavior* of an object.
These methods can be called by referencing them through the object, instead of passing the object as an argument to a function

A method is either a [Getters](./Univesp_Getters.md), [Setters](./Univesp_Setters.md) or a [Constructors](./Univesp_Constructors.md)

## `this` and `self`
A method can act on its own object by a keyword `self` or `this`, which references the object itself, and then access the fields of that object

## Example

```java
class Car {
    public Car(String color, String brand, String model) {
        this.color = color;
        this.brand = brand;
        this.model = model;
    }

    public void setSpeed(int speed) {
        this.speed = speed;
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

The above codeblock creates 3 methods
- A constructor
- A public setter
- A public gett/ser

A method may or may not be [Static](./Univesp_Static.md)
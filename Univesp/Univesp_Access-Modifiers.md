# Access Modifiers
Access modifiers are keywords in *Object Oriented Programming Languages* that define which objects are allowed to access certain fields/methods of other objects

Access modifiers are important to create proper [Encapsulation](./Univesp_Encapsulation.md)

## Types of access modifiers
Generally speaking there are three main access modifiers
- `public`
    - Any object can access that field/method
- `private`
    - Only that object can access that field
- `protected`
    - That object and objects in subclasses of that object can access that field

### Example
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

The above codeblock defines a class `Car`, with:
    - 3 `public` fields
    - 1 `private` field
    - 3 `public` methods

Public fields can be modified by other objects through `object.publicField = (value)`, like `myCar.color = "Black"`  
But private fields can only be changed `myCar` itself, through its own *methods*
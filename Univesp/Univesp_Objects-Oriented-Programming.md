# Object Oriented Programming
Object Oriented Programming is a [Programming Paradigm](./Univesp_Programming-Paradigm.md) based on [Objects](./Univesp_Objects.md).   
The objects contain *data*, that stores information about the object and *code*, also known as *methods*, that perform actions in the objects

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

```java
public static void main(String[] args) {
    Car myCar = new Car("White", "Toyota", "AE86"); 

    System.out.println(myCar.getSpeed());

    myCar.setSpeed(100);

    System.out.println(myCar.getSpeed());
}    
```
The above codeblock defines a [Classes](./Univesp_Classes.md) `Car()` with 4 data fields and 3 methods (one of them being a `constructor`)

- `color`
    - Specified when creating the object myCar(`color`, `brand`, model)
- `brand`
    - Specified when creating the object myCar(`color`, `brand`, model)
- `model`
    - Specified when creating the object myCar(`color`, `brand`, model)
- `speed`
    - Can be returned from the `getSpeed` method
    - Can be changed from the `setSpeed` method
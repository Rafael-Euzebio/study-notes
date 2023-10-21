# Setters
A `setter` is a *method* inside an object that changes the value of a property

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

    private String color; 
    private String brand;
    private String model;
    private int speed = 0;
}
```

In the above codeblock the `setSpeed()` method is a *setter*, since it changes the current speed of a car object.

```java
public static void main(String[] args) {
    Car myCar = new Car("White", "Toyota", "AE86");

    System.out.println("Speed: " + myCar.getSpeed());
    myCar.setSpeed(100);
    System.out.println("Speed: " + myCar.getSpeed());
}
```
`0`


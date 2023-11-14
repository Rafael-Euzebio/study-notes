# Getters
A `getter` is a *method* inside an object that returns the value of field in that object

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

In the above codeblock the `getSpeed()` method is a getter, since it returns the current speed of a car object.

```java
public static void main(String[] args) {
    Car myCar = new Car("White", "Toyota", "AE86");

    System.out.println(myCar.getSpeed());
}
```
`0`


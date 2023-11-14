# Objects
An object is an instance of a [Classes](./Univesp_Classes.md). While an class is an *abstraction*, an object is *concrete*.  
That means an object has information stored in it that describes that object
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

The above codeblock creates a class `Car` and an object `myCar`, with the properties `White`, `Toyota` and `AE86`, prints it and then changes one of the properties to ``


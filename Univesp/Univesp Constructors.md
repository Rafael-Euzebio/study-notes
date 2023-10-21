# Constructor
A constructor is a method that initializes an object. It can change the properties of an object when it is created using the arguments, so the programmer doesn't necessarily has to use `setter` methods

## Example

```java


class Main {
    public static void main(String[] args) {
        Car myCar = new Car("White", "Toyota", "AE86"); 
    }
}

class Car {
    public Car(String color, String brand, String model) {
        this.color = color;
        this.brand = brand;
        this.model = model;
    }
}
```

The above codeblock creates a `Car` class and a `Car` method. The method is a constructor (and that's why it has the same name). It attributes the arguments passed in `Car myCar = new Car(arguments)` to the object



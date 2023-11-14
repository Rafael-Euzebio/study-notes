# Static
`static` is a keyword used when declaring [Methods](./Univesp_Methods.md) or [Properties](./Univesp_Properties.md)

## Static Properties
A static property is a property that has the same value for all objects of a class. Declaring a static property is a way to manage memory efficiently if a property will always be the same for all objects  
Instead of creating a copy of that property in every object, the property resides *in the class*, and the objects only has a reference to it.  
A static property can be changed and retrieved even if no object of that class has been created yet

### Example
```java
class Car {

    public Car(String color, String brand, String model) {
        this.color = color;
        this.brand = brand;
        this.model = model;
    }

    public String getColor() {
        return this.color;
    }

    public String getBrand() {
        return this.brand;
    }

    public String getModel() {
        return this.model;
    }
    
    private static color;
    private brand;
    private model
}

```

The above codeblcok creates a `Car` class with a `static` property `color`. Once a value is assigned to `color` all objects of that class will have the same value

```java

class Main {
    public static void main(String[] args) {
        Car myCar = new Car("White", "Toyota", "AE86");    

        System.out.println("I have a " + myCar.getColor() + " " + myCar.getBrand() + " " + myCar.getModel());

        Car neighborsCar = new Car("Yellow", "Mazda", "RX7");

        System.out.println("My neighbor has a " + neighborsCar.getColor() + " " + neighborsCar.getBrand() + " " + neighborsCar.getModel());
        System.out.println("I have a " + myCar.getColor() + " " + myCar.getBrand() + " " + myCar.getModel());

    }
}
```

```
I have a White Toyota AE86
My neighbor has a Yellow Mazda RX7
I have a Yellow Toyota AE86
```

#### Acessing properties statically
Even though acessing static properties with `object.property` works, static properties must be acessed through the class with `Class.property`

## Static Methods
To complement *static properties* there are *static methods*.  
Static methods perform actions in the class, they can be called even if an object of that class has not been created yet  
Static methods can only change or return static properties

### Example

```java

class Car {

    public Car(String brand, String model) {
        this.brand = brand;
        this.model = model;
    }

    public static String getColor() {
        return Car.color;
    }

    public static void setColor(String color) {
        Car.color = color;
    }

    private static String color;
    ....
}
```

The constructor in the above codeblock does not set a `color`. Instead we have a static method that does that.

This allows us to set a color for all Cars before we even create a car object

```java

class Main {
    public static void main(String[] args) {
        Car.setColor("White");

        Car myCar = new Car("Toyota", "AE86");
        Car neighborCar = new Car("Mazda", "RX7");
        System.out.println("I have a " + Car.getColor() + " " + myCar.getBrand() + " " + myCar.getModel());
        System.out.println("My neighbor has a " + Car.getColor() + " " + neighborCar.getBrand() + " " + neighborCar.getModel());


    }
}
```

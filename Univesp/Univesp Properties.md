# Properties
Properties are [[CS50x variables]] inside [[Univesp Objects]]. A property describe a characteristic of an object

## Example

```java 
class Car {

    public Car(String color, String brand, String model) {
        this.color = color; 
        this.brand = brand;
        this.model = model;
    }
    private String color;
    private String brand;
    private String model;
}
```

The above codeblock creates a class `Car` with 3 properties, `color`, `brand` and `model`

A property may or may not be [[Univesp Static]]


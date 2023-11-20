# Properties
Properties are [Variables](../CS50x/Week-1_C/CS50x_Variables.md) inside [Objects](./Univesp_Objects.md). A property describe a characteristic of an object

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

A property may or may not be [Static](./Univesp_Static.md)
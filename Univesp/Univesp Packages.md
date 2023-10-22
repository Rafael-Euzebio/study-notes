# Packages
Packages are related [[Univesp Classes]] grouped in a single directory.  
Packages are used to organize our project structure and keep related classes grouped and separated from different classes

## Example
a `Car` class can be kept inside a `./vehicles/earth` folder along with `Motobike`. Separated from them there might be `Plane` and `Helycopter` in `./vehicles/air`.

Each class inside a package must have in the first line the name of the package it resides in

```java
package vehicles.earth;

public class Car{
    String color;
    String brand;
    String model;

    ....
}
```

and then it can be imported in the main program by

```java
import vehicles.earth.*;
```
To import all classes

```java
import vehicles.eart.Car;
```

To import a single class

# Java
Java is an [Objects Oriented](./Univesp_Objects-Oriented-Programming.md) [Programming Language](../CS50x/Week-1_C/CS50x_Programming-Language.md)  

Different than other *OOP* programming languages, Java works solely with *Classes* and *Objects*, and does not allow code outside of these

## Example
```java
class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World");
    }    
}
```
```
Hello, World
```

### Syntax
Every java program has at least one class which matches the `filename`, in the above example it is `HelloWorld`
```java
class HelloWorld {
    ...
}
```

Inside that class is the `main` [Methods](./Univesp_Methods.md), which is the first to be executed
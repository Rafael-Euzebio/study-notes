# Encapsulation
Encapsulation is a [Objects Oriented Programming](./Univesp_Objects-Oriented-Programming.md) concept which consists of hiding the properties and implementation of an object through [Methods](./Univesp_Methods.md)
The properties of an object can, essentially, be hid from the programmer as long as it does what it is expected to do

## Example
Given an object `myCar` with 4 properties:
- color
- brand
- model
- speed

These properties can be changed or returned through `myCar.(property)`  
But this is considered a bad practice in *Object Oriented Programming*. Instead we should:  
- Make other objects unable to access the properties of `myCar` by using the [Access Modifiers](./Univesp_Access-Modifiers) `private`
- Change and return the properties through [Getters](./Univesp_Getters.md) and [Setters](./Univesp_Setters.md) methods
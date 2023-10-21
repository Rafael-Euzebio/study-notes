# Abstraction
Abstraction is a [[Univesp Objects Oriented Programming]] concept  
It consists of removing information that is not required to work with an objects

## Example
A class `Car` could have the following properties:
- Color
- Brand
- Model
- Rim size
- Automatic Transmition? (`Boolean`)
- Eletric? (`Boolean`) 
....

But if our code only makes use of the first three properties, all the others are useless. We can abstract our `Car` class to only contain:
- Color
- Brand
- Model

A class with only these 3 properties is the abstraction of a `Car`
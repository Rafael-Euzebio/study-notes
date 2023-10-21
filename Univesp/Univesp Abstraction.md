# Abstraction
Abstraction is a [[Univesp Object Oriented Programming]] concept  
It consists of removing information that is not required to work with an [[Univesp Objects]]

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

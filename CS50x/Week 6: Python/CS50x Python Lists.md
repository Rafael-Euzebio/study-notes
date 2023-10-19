# Python Lists
A list in python is a sequence of items and a [[CS50x Python Sequences Types]].

## Example
`numbers = [1, 2, 3, 4, 5]`  

We can easily add an element to the end of the list:  
`numbers.append(6)`

## Lists vs Arrays
Lists are declared in the exact same way as `arrays` in other languages, but a list is *different* than an array, especially when compared to a `C` array (which can also be used in Python)

- C arrays can only hold items of the same type
    - Acessing an item in a C array is done by *pointer arithmetics*, multiplying the index of the item to be acessed by the size of a single item. Items of different types would also be of different size
- C arrays cannot change in size. If an array must be resized, than a new (bigger) array  must be declared, the old values must be copied to it, and the new item must be inserted
- Python Lists use a lot more space than C arrays

Python's lists are refered to as [[SF Dynamic Arrays]]



# Arrays
An array is basically a sequence of many values of the same type stored in the same variable.
In C arrays are a Derived Data Types
Its type is the same of the value's type stored inside it.

## Declaring and accessing arrays
An array is declared using *[]* after the variable's name, followed by its elements between *{}*
To access its values you have to specify the value's position **starting on 0**.

### Example
```C
#include <stdio.h>

int main(void){
    int integer_array[] = {1, 2};
    printf("%d\n", integer_array[1]);
}
```
**output**
> 2
> this is an array

#### Explaining Example
1. an array of integers is declared, with 2 values, 1 and 2
2. print the value at position 1 in the integer_array. That prints 2.

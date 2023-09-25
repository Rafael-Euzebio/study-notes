# Void
Void is a [[C Data Types|data type]] in C, it is used to specify that no value is present. It represents nothing. 
Its used mainly with functions, indicating they don't return any value or don't take any arguments.

## Example
```C
#include <stdio.h>

void print(void){
    printf("function called");
}

int main(void){
    print();
}
```

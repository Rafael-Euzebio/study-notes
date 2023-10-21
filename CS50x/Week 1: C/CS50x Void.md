# Void
Void is a [[CS50x C Data Types]] in C, it is used to specify that no value is present. It represents nothing. 
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

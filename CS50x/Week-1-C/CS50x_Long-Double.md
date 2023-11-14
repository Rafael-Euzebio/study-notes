# Long Double
Long double is a data type used to store decimal numbers, with **floating points**.

- Size (bytes): At least 10, usually 12 or 16
- Format specifier: %Lf

## Precision
Long double precision is up to 19 digits (**but can vary depending on the system's architecture)

## Example
```C
#include <stdio.h>

int main(void){
    int a = 1;
    int b = 3;
    int c = a/b;

    printf("%.20Lf", c);
}
```
**Output**
> 0.33333333333333331483


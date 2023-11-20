# Memory Address
A memory address is a reference to an specific location of a computer's memory, where data can be stored.

## Example
In C a memory address can be referenced through the `&` operator before the variable

```c
#include <stdio.h>

int main(void)
{
    int  n = 50;
    printf("%p\n", &n);
}
```

The above codeblock outputs a [Hexadecimal](./CS50x_Hexadecimal.md) code which is the location address of `n`  
The format specifier `%p` specifies a [Pointer](./CS50x_Pointer.md)

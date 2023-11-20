# Pointers
A pointer is an object that stores the memory address of a value.  
In C a pointer is a [Derived Data Types](../Week-2_Arrays/CS50x_Derived-Data-Types.md), and its type is the type of the entity they are pointing to.

## Example
```c
#include <stdio.h>

int main(void)
{
    int  n = 50;
    int *p = &n;
    printf("%p\n", &p);
}
```

In the above codeblock `*p` creates a pointer to the `n` variable, the `&` operator must be specified to access `n`'s address, and the `*` operator must be specified to store `p` as a pointer.  
The `*` operator is also used to "go-to" that specific address, using `printf("%i\n", *p)` would print `n` value instead  
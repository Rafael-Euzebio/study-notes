# Variable Lifetime
Variable lifetime refers to the parts of a program where it is safe to access a variable's memory address, before it is freed to give space to another variable.   


## Example
```c
#include <stdio.h>

int *sum(int a);

int main(void)
{
    int x = 2;
    int *y = sum(x);
    printf("%p\n", y);
    printf("%i\n", *y);
    return 0;
}

int *sum(int a)
{
    int y = 3;
    y = y + a;
    printf("%i\n", y);
    return &y;
}
```

When compiling this program, some compilers might throw a **warning**
```
warning: address of stack memory associated with local variable 'y' returned [-Wreturn-stack-address]
    return &y;
            ^
1 warning generated.
```

That is because `y` is a [[Local Variable]], which has its lifetime limited to its scope, in this case the function `sum`. That address is freed and will be eventually used for another variable.

Printing the contents of that address might output the value of `y`, null or garbage values.  
Any meaningful value from an address of a variable outside of its lifetime is purely coincidental and shouldn't be considered by the programmer as reliable.

## Management and Safety
Variable Lifetime is directly related to [[Memory Management]] and [[Memory Safety]], since memory is a finite resource, variables must be allocated, used and then destroyer when they're no longer needed to give space to the next. Its up to the programmer to know when it is safe to access those memory addresses and when its not.  


## Lifetime and Scope Differences
Variable lifetime and [[Scope]] are very related but they are not the same thing. Scope is the part of a program where a variable can be referenced by its name. Lifetime is the part of a program where a variable's memory address is safe for reading.  

A variable's lifetime might still be active but the program might be out of its scope, in this case its memory address can still be safely acessed through a pointer.

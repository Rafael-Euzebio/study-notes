# Local Variable
Local variables are [Variables](../Week-1_C/CS50x_Variables.md) that has its [Lifetime](./CS50x_Lifetime.md) and [Scope](./CS50x_Scope.md) limited to a block of code or a function.
A local variable may or may not be a [Static Variable](./CS50x_Static-Variable.md)


## Example
```c
#include <stdio.h>

int main(void)
{
    int array[3] = {0, 1, 2, 3};

    for(int i = 0; i < 3; i++)
    {
        /// i is acessible
        printf("%i\n", array[i]);
    }
    /// i is not acessible!!!
}
```

## Memory Location
A local variable is stored in the [Memory Stack](./CS50x_Memory-Stack.md), in the higher addresses, and it's managed by [Automatic Memory Allocation](./CS50x_Automatic-Memory-Allocation.md)
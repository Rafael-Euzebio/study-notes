# Automatic Memory Allocation
Automatic Memory Allocation is a [Memory Management](./CS50x_Memory-Management.md) process that allocates memory for a [Local Variable](./CS50x_Local-Variable.md).

### Example
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
A variable allocated automatically has its contents stored in the [Memory Stack](./CS50x_Memory-Stack.md) memory, where its contents are freed right after the program leaves its scope.  
The  

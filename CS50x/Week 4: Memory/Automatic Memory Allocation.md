# Automatic Memory Allocation
Automatic Memory Allocation is a [[Memory Management]] process that allocates memory for a [[Local Variable]].

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
A variable allocated automatically has its contents stored in the [[Memory Stack]] memory, where its contents are freed right after the program leaves its scope.  
The  

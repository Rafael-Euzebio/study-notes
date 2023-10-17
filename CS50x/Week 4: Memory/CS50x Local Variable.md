# Local Variable
Local variables are [[CS50x Variables]] that has its [[CS50x Lifetime]] and [[CS50x Scope]] limited to a block of code or a function.
A local variable may or may not be a [[CS50x Static Variable]]


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
A local variable is stored in the [[CS50x Memory Stack]], in the higher addresses, and it's managed by [[CS50x Automatic Memory Allocation]]

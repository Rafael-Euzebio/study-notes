# Global Variable
Global variables are [[CS50x Variables]] that have global [[CS50x Scope]], hence they can be referenced in any part of the program. Their [[CS50x Lifetime]] is the runtime of the program.

## C
In C global variables can be referenced cross-files if it's declared with the keyword `extern`, unless the keyword `static` is used. A static global variable can only be referenced within that same file

## Example

```c
#include <stdio.h>

extern int MAX = 10; //Can be referenced in other files
static int MIN = 1; //Can not be referenced in other files

int main(void)
{
    int array[10];

    for (int i = 0; i < MAX; i++){
        array[i] = i;
        printf("%i\n", array[i]);
    }
    return 0;
}
```

Output
```
0
1
2
3
4
5
6
7
8
9
```

## Memory Location
A global variable is stored in the [[CS50x Data Segment]]

# Procedural Programming
Procedural programming is a [[Univesp Programming Paradigm]] which refers to the ability to wrap instructions in separate code blocks, aka *procedures*  
This is done through *procedures calls*

A common name for *procedures* is `functions`

## Example

```c
#include <stdio.h>

int sum(int a, int b);

int main(void)
{
    int a = 1;
    int b = 2;

    int c = sum(a, b);

    printf("%i\n", c)
}

int sum(int a, int b)
{
    int sum = a + b;

    return sum;
}
```

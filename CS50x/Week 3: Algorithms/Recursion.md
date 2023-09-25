# Recursion
Recursion is a method of solving a problem by solving smaller versions of the same problem. That works by using [[Functions]] that call themselves

## Pseudocode
Suppose we need to code a program that prints the following pyramid
```
#
##
###
####
```
That's a pyramid of height 4. How do we build **recursively** a pyramid of height 4?  
Building a pyramid of height 3!  
But how do we build a pyramid of height 3?  
Building a pyramid of height 2...  
And when we reach 1, we print `#`'s equivalent to the current height.  

## C code
```c
#include <stdio.h>
#include <cs50.h>

void draw(int n);

int main(void)
{
    int height = get_int("Height: ");
    draw(height);
}

void draw(int n)
{
    if (n <= 0){
        return;
    }
    draw(n - 1);

    for (int i = 0; i < n; i++)
    {
        printf("#");
    }
    printf("\n");
}
```

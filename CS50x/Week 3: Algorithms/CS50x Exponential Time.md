# Exponential Time
In Big O Notation, an Exponential Time Complexity means the [[CS50x Time Complexity]] of an algorithm grows exponentially according to the input $n$
That means with each addition to $n$ the growth rate doubles up, for this reason algorithms with exponential time complexity shouldn't be used with big inputs.

It is specified as $(2^n)$

Exponential Time Complexity is particularly true with recursive algorithms.

## Example
The following code implements the *Tower of Hanoi* puzzle, printing how to move the disks to solve it through the use of recursion

```c
#include <stdio.h>

void tower(int n, char source, char destination, char auxiliary);
int main(void)
{
    int n;
    printf("How many disks: ");
    scanf("%d", &n);
    tower(n, 'A', 'C', 'B');
}

void tower(int n, char source, char destination, char auxiliary)
{
    if (n == 1)
    {
        printf("Move disk 1 from %c to %c\n", source, destination);
    }
    else
    {
        tower(n - 1, source, auxiliary, destination);
        printf("Move disk %d from %c to %c\n", n, source, destination);
        tower(n-1, auxiliary, destination, source);
    }
}

```
It performs 7 actions if the input is 3.  
15 if input 4.  
31 if input is 5.  
....

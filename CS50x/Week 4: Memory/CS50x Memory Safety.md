# Memory Safety
Memory Safety describes if a language takes measures to avoid bugs and security vulnerabilities by managing access to a [[CS50x Memory Address]]

## Memory-Unsafe Languages
A language is said to be memory unsafe when it allows unchecked access to memory addresses and arbitrary *pointer arithmetics*, where variables might not have been initialized or already expired.  

### Example
```c
#include <stdio.h>

int* bar();
int main(void)
{
    int *b = bar();
    printf("%i", *b);
}

int* bar()
{
    int a = 10;
    return &a; /// <--- Don't do that!
}
```

The above codeblock:  
- defines a function `bar` which return the address of a variable that only exisits within the Scope of that function
- print out the contents of that memory address. It might print `10`, nothing or garbage  

The fact that C allows you to access a memory address that is no longer allocated for the program is considered *unsafe* and any meaningful value returned from a variable outside of its scope is purely a coincidence.

Memory safety is directly associated with [[CS50x Lifetime]]  

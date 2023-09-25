# Scope
The scope of a variable is the part of the program where said variable can be referenced by its name.  
Scopes allows a programmer to use the same name for different variables as long as they have separate scopes. 
Scope is usually defined through a function or a block, written with, in most languages written with `{}`

## Example
```c
#include <stdio.h>

int sum(int a);

int x = 1;

int main(void)
{
    int z = 2;
    printf("%i\n", x + sum(z));
    return 0;
}

int sum(int a)
{
    int y = 3;
    return a + y;
}
```

The above codeblock contains 3 variables and 2 different scopes, *local* and *global*, therefore they are called [[Local Variable]] and [[Global Variable]]

- `x` is a *global variable*, since it is declared outside of any function, and can be acessed from within any block. 
- `z` and `y` are local variables, declared within their own functions, and their scope are within their respective functions.
    - z is passed to `y`'s function through an *argument*, that creates a copy of `z`, named `a`, which lives within the function `sum` scope

## Lifetime and Scope Differences
[[Lifetime]] and scope are very related but they are not the same thing. Scope is the part of a program where a variable can be referenced by its name. Lifetime is the part of a program where a variable's memory address is safe for reading.  


# C
C is a general-purpose programming language to write [[CS50x Source Code]]. It's widely adopted, used in computers that range from microcontrollers to supercomputers.

## Relations to other languages
Many languages have borrowed directly or indirectly from C, like C++ C#, Javascript, Java, Python etc....

## Syntax
```c
#include <stdio.h>

int main(void)
{
    int a = 1;
    int b = 2;
    inc c = a + b;
    printf("%i\n", c);
    printf("Hello, world\n");
}
```

The codeblock above is simple but shows the important aspects of C syntax;

- `#include <stdio.h>` 
    - imports the library `stdio.h` (Standard Input and Output). It contains some of the most used C functions, like `printf`  
- `int main(void)` 
    - Defines a function `main`, which every C program contains. 
        - `int` is the return value. Not necessary in the main function, But it's a good practice to add to `return 0` on success and `return 1` on failure
        - `main` name of the function
        - `void` arguments taken by the function

- `int (variable) = (value)`
    - Assings a value to a variable
- `printf`
    - Prints in the terminal the argument given to it
    - `printf` might take special arguments like `%i` to print the value of an `integer` variable and `\n` to print a new line


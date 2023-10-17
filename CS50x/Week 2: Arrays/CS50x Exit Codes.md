# Exit Codes
Exit codes are codes returned by a program, sometimes by [[CS50x Functions]], that indicate whether said program ran successfully or failed.
The kind of error is indicated by the exit code. Some may are standard, which allow the user to know the error through a quick search, others are specific, and only who designed the program know what they mean.

## Examples
```c
#include <stdio.h>
#include <cs50.h>

int main(int argc, string argv[])
{
    if (argc != 2){
        printf("Missing command-line argument\n");
        return 1;
    }
    else{
        printf("hello, %s\n", argv[1]);
        return 0;
    }
}
```
The above code takes 2 'command-line arguments', if more or less than that are given it returns an `exit code 1`.

A common exit code found on the web is `404`, which means `Page not found`.

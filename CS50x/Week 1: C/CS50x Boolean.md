# Boolean
Boolean is a [[CS50x C Data Types]] that can hold one of two values, *true* or *false*, also represented as 0 or 1.

## In C
In C boolean is not a built in data type. Instead integer numbers, 0 and 1, are used to identify if a value is *true* or *false* To use it the library *stdbool.h* has to be imported.

## stdbool.h
stdbool.h defines alias, for bool keywords.
- *true* is an alias for 1
- *false* is an alias for 0


### Example
```C
#include <stdio.h>
#include <stdbool.h>

int main(void){
    bool a = true;
    bool b = false;

    printf("a: %d\n", a);
    printf("b: %d\n", b);
}
```

**Output**
> a: 1
> b: 0

#### Explaining the example
Since bool is actually **just int values (0's for false and 1's true)**, bool can only be printed with the Format Identifier *%d*, which result in the numbers being printed.






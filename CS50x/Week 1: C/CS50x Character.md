# Character
Character is a [[Primitive Data Types|Primitive Data Type]] which can store only a single character. It's the most basic data type in C.
- Size (bytes): 1
- Format Specifier: %c or *%s (with arrays)*

## Example
```C
#include <stdio.h>

int main(void){
    char a = 'A';
    char b = 66;

    printf("%c\n", a);
    printf("%c\n", b);
}
```

**Output**
> A
> B

### Explaning Example
1. char variable a is declared as 'A'.
2. char variable b is declared as 66.
3. char a is printed, showing uppercase A as expected.
4. char b is printed, showing uppercase B.
        - When printing a char declared as a number, C converts that number to the equivalent ASCII symbol through [[CS50x Character Encoding]]. In this case 66 is uppercase B. 
        - If the user declares to use the Format Specifier *%d* (for integer numbers) when printing a char, it will be converted to the equivalent number in ASCII.


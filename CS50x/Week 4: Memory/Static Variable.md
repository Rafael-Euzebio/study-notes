# Static Variable
A static variable is a variable stored in the static memory, the variable and its contents exists as long as the program is running, instead of being freed after the program leaves its scope.

## Declaration
In C a [[Static Variable]] can be declared using the keyword `static`.  
That variable will exist as long as the program is running.

```c
#include <stdio.h>

int counter();
int main(void)
{
    int *count;
    for (int i = 0; i <= 3; i++) {
        count = counter();
        printf("%p\n", count);
        printf("%i\n", *count);
    }
    return 0;
}

int counter()
{
    static int count = 0;
    return ++count;
}

```
Output:
```
1
2
3
4
```

If the keyword `static` wasn't used the output would be the number `1` four times.

## Lifetime and Scope
A static variable has limited scope but their lifetime lasts as long as the program runs. That means they can be refereced by their name only inside their scope, but their memory address and its contents can be safely acessed in any part of the program.
```c
#include <stdio.h>

int *counter();
int main(void)
{
    int *address = counter();
    for (int i = 0; i <= 3; i++) {
        printf("%p\n", address);
        printf("%i\n", *address);
    }
    return 0;
}

int *counter()
{
    static int count = 0;
    count++;
    return &count;
}
```
Output
```
0x563f40125034
1
0x563f40125034
2
0x563f40125034
3

```

In the above codeblock the `*counter()` function returns the address of a variable `count` declared and incremented inside of it. Said variable can't be directly referenced outside of that function, but it's address can be safely returned, printed and analyzed, since `static` variable's lifetime lasts as long as the program is running.

## Memory Location
A static variable is located in the [[BSS Segment]] or [[Data Segment]], depending on wether or not it is initialized

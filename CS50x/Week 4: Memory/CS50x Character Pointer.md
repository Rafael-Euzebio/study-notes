# Character Pointer
In C a Character Pointer is a [[CS50x Pointer]] which points to the address of the first element of an [[CS50x Arrays]] of chars, or, often called [[CS50x Strings]]

## Strings
There are many ways to build strings in C, the most known are:
```c
int main(void)
{
    char string1[] = {'H', 'e', 'l', 'l', 'o', '\0'};
    char string2[] = "World";
}
```
Both strings are stored sequentially in the memory, ending with a `\0` (Nul Character) (in the second method the Nul Character is added automatically).  
But `string1` and `string2` does not store the whole array, instead they just store a pointer to the address of the first `char` in that array.

This can be explicitly expressed as:
```c
int main(void)
{
    char *string = "Bye";
}
```

The `*` operator is a pointer, which stores in the `string` variable the address of the first char.

```c
    printf("%p", string);
```
would output the hexadecimal memory address of the char `B`  

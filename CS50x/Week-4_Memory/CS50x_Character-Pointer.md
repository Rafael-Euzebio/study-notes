# Character Pointer
In C a Character Pointer is a [Pointer](./CS50x_Pointer.md) which points to the address of the first element of an [Arrays](../Week-2_Arrays/CS50x_Arrays.md) of chars, or, often called [Strings](../Week-2_Arrays/CS50x_Strings.md)

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
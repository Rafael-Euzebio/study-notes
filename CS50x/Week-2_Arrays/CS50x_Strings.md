# String
An string is, in many languages, a data type. In C a string is an [Arrays](./CS50x_Arrays.md) of [Character](../Week-1_C/CS50x_Character.md).
An string is usually identified by `"` (double quotes) surrounding it, though it can be declared with multiple `chars`

## The Nul Character
Every string ends with a `null` character, expressed as `\0`. **It must be explicitly inserted when using a static array and single-quoted chars.**

### Example
```C
    char array[3] = {'H', 'I', '!', '\0'}; //needs the null char
    char string[] = "HI!"; //does not need the null char
```
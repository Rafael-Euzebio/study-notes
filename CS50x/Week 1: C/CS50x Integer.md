# Integer
Integer is a [[Primitive Data Types|Primitive Data Type]] used to store real numbers. It cannot store decimal values.

- Size (bytes):  At least 2, usually 4 (system dependent)
- Format specifier: %d or %i

## Example
A integer variable is declared as below:

```C
int a = 10;
int b = -50;

printf("a: %d\n", a);
printf("b: %d\n", b);
```

**Output**
> a: 10 
> b: -50

### Limitations
The range of numbers an integer can store is limited and it's system dependent

- If a number out of this range has to be stored, a [[CS50x Long Integer]] can be used.

- If that range is larger than the necessary, a [[Short Integer]] can be used.

***Important: Integer's range is system dependent***

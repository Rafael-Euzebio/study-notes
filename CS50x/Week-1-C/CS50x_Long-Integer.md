# Long Integer
A long integer is a data type used to store real numbers. It has a higher range than [Integer](./CS50x_Integer.md). It cannot store decimal values.

- Size (bytes): At least 4, usually 8 (system dependent) 
- Format specifier: %li

# Example
```C
int main(void){
    long a = 2000000000000;
    long b = 2000000000000;
    long c = a + b;

    printf("%li\n, c");
}
```
**Output**
> *4000000000000*.

## Long Long
If even more space is necessary
Using an `int` instead of a `long` that number would likely overflow int's range and become a negative number.

***Important: Long integer's range is system dependent***


